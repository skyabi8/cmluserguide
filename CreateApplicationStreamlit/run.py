import os
os.system('pip install altair==4.2.2')
os.system('pip install streamlit')

port_cdsw = int(os.getenv('CDSW_PUBLIC_PORT'))
port_cdsw = str(port_cdsw)


os.system('streamlit run CreateApplicationStreamlit/streamlit.py --server.address 127.0.0.1 --server.port ' + port_cdsw )