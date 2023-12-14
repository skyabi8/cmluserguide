import pandas as pd
import joblib
import sklearn

def prediction(args):
    Receiving_Currency = args['Receiving_Currency']
    Payment_Currency = args['Payment_Currency']
    Payment_Format = args['Payment_Format']
    Amount_Received = args['Amount_Received']
    Amount_Paid = args['Amount_Paid']
    
    # load model dan encoder
    with open('/home/cdsw/DeployModel/encoder.pkl', 'rb') as file:
        encoder = joblib.load(file)
    with open('/home/cdsw/DeployModel/model.pkl', 'rb') as file_2:
        model = joblib.load(file_2)
    
    # membuat data input
    data_input = {'Receiving Currency': [Receiving_Currency],
        'Payment Currency': [Payment_Currency],
        'Payment Format': [Payment_Format],
        'Amount Received': [Amount_Received],
        'Amount Paid': [Amount_Paid]}
    df_input= pd.DataFrame(data_input)
    
    # encoding
    list_encode= ['Receiving Currency','Payment Currency','Payment Format']
    encoded_input = encoder.transform(df_input[list_encode]).toarray()
    encoded_input = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(list_encode))
    encoded_input = pd.concat([df_input[['Amount Received','Amount Paid']], encoded_input], axis=1)
    
    # predicting
    pred = model.predict(encoded_input)
    if pred == 1:
        hasil = "Pencucian Uang" 
    else:
        hasil = "Bukan pencucian uang"
    
    return hasil
#    print('Input data: ')
#    print(f'Receiving Currency: {Receiving_Currency}')
#    print(f'Payment Currency: {Payment_Currency}')
#    print(f'Payment Format: {Payment_Format}')
#    print(f'Amount Received: {Amount_Received}')
#    print(f'Amount Paid: {Amount_Paid}')
#    print(f'PREDIKSI:{hasil}')
