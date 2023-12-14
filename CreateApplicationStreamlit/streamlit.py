import streamlit as st
import requests
import json

def run ():
    # membuat title
    st.title('Prediksi Pencucian Uang')
    # membuat form
    with st.form(key= 'form_parameter'):
        Receiving_Currency = st.selectbox(
                        'Receiving Currency',
                        ('US Dollar', 'Euro', 'UK Pound', 'Bitcoin', 'Yen', 'Yuan',
                        'Canadian Dollar', 'Rupee', 'Australian Dollar', 'Ruble', 'Shekel',
                        'Brazil Real', 'Mexican Peso', 'Swiss Franc', 'Saudi Riyal'))
        Payment_Currency = st.selectbox(
                        'Payment Currency',
                        ('US Dollar', 'Euro', 'UK Pound', 'Bitcoin', 'Yen', 'Yuan',
                        'Canadian Dollar', 'Rupee', 'Australian Dollar', 'Ruble', 'Shekel',
                        'Brazil Real', 'Mexican Peso', 'Swiss Franc', 'Saudi Riyal'))
        Payment_Format = st.selectbox(
                        'Payment Format',
                        ('Reinvestment', 'Cheque', 'Credit Card', 'ACH', 'Wire', 'Cash','Bitcoin'))
        Amount_Received = st.number_input('Amount Received', min_value=0, value=0)
        Amount_Paid = st.number_input('Amount Paid', min_value= 0, value=0)
        st.markdown('---')
        submitted = st.form_submit_button('Predict')

        # membuat data input
        data_input = {
                "Receiving_Currency": Receiving_Currency,
                "Payment_Currency": Payment_Currency,
                "Payment_Format": Payment_Format,
                "Amount_Received": Amount_Received,
                "Amount_Paid": Amount_Paid
                        }
    
    # Mengubah objek request_data menjadi string JSON
    request_json = json.dumps(data_input)
    
    # Request API
    r = requests.post('<haha hihi>', 
                  data='{"accessKey":"<haha hihi>","request":'+ request_json +'}', 
                  headers={'Content-Type': 'application/json'})
    if submitted:
        st.write(r.json()['response'])
   
        
if __name__ == '__main__':
    run()
