import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips_df = pd.read_csv(url)

st.title("Визуализация данных о чаевых")
st.write("Датасет tips.csv")
st.dataframe(tips_df)

fig, ax = plt.subplots()
sns.histplot(data=tips_df, x="tip", ax=ax)
st.subheader("Распределение суммы чаевых")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(data=tips_df, x="total_bill", y="tip", ax=ax)
st.subheader("Связь между общей суммой счета и размером чаевых")
st.pyplot(fig)
