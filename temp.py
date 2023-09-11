import streamlit as st
import pandas as pd
import seaborn as sns
st.title("Data Analysis")
st.subheader("Data Analysis using Python")
upload = st.file_uploader("Upload your database (in csv format)")
if upload is not None:\
    data=pd.read_csv(upload)
    
if upload is not None:
    if st.checkbox("Preview Database"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            

if upload is not None:
    if st.checkbox("Datatypes of each column"):
        st.text("DAtta types")
        st.write(data.dtypes)

if upload is not None:
    data_shape=st.radio("What dimension you want to check?",('Rows','Columns'))                
    if data_shape=='Rows':
        st.text('Number of rows:')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of columns:")
        st.write(data.shape[1])

if upload is not None:
    test = data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!.No missing values")

if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset contais Some Duplicated values")
        dup=st.selectbox("Do you want to remove duplicated values",("Select One",'Yes','No'))
        if dup == 'Yes':
            data= data.drop_duplicates()
            st.text("Duplicated values removed")
        if dup == 'No':
            st.text("No problem")
            
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))            
if st.button("About App"):
    st.text("Bulit with streamlit")
    st.text("Thanks to Streamlit") 
if st.checkbox("By:"):
    st.success("Virat verma")               