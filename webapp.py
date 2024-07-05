import streamlit as st
import pandas as pd

st.write("Hello Web App")
data_df = pd.read_csv('training_task_tickets_final.csv')
st.dataframe(data_df)

piccount_df = data_df.groupby(["PIC","Status"]).count()['Task Name'].reset_index()
st.dataframe(piccount_df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("1 รอดำเนินการ",len(data_df[data_df['Status'] == "1 รอดำเนินการ"]))
col2.metric("2 ขั้นตอน A",len(data_df[data_df['Status'] == "2 ขั้นตอน A"]))
col3.metric("3 ขั้นตอน B",len(data_df[data_df['Status'] == "3 ขั้นตอน B"]))
col4.metric("4 เสร็จสิ้น",len(data_df[data_df['Status'] == "4 เสร็จสิ้น"]))

st.bar_chart(piccount_df,x='PIC',y='Task Name',color='Status')

