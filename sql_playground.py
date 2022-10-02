from pandasql import sqldf
import pandas as pd
import streamlit

file = st.file_uploader('Upload CSV HERE', 'csv', accept_multiple_files=True)
database = {} #database of dataframes key is name value is DF

def add_to_database(name):
    
        pd.read_csv(file)
        database[]
        st.dataframe(df)
        r,c = df.shape
        st.text("# of rows:{}".format(r))
        st.text("# of columns:{}".format(c))



if file != None:
    pd.read_csv(file)
    database[]
    st.dataframe(df)
    r,c = df.shape
    st.text("# of rows:{}".format(r))
    st.text("# of columns:{}".format(c))

