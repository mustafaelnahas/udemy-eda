# importing libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# credits
st.title("Udemy Courses | EDA")
st.text('Developed By: @MustafaOthman')

# loading & inspecting data
df = pd.read_csv('udemy_courses.csv')
df.drop(df[df['level'] == '52'].index, axis=0, inplace=True)
st.dataframe(df.head())

col1, col2 = st.columns(2)

with col1:
    # Number of Subscribers per Subject
    st.subheader("Number of Subscribers per Subject")
    option = st.selectbox("Select an option to split visuals",['is_paid','level'])
    fig = px.bar(data_frame=df, x=df['subject'], color=option)
    st.plotly_chart(fig)

with col2:
    # Number of subscribers per year
    st.subheader("Number of Subscribers per Year")
    fig = px.pie(names = df.groupby('year')['num_subscribers'].sum().index,
                values = df.groupby('year')['num_subscribers'].sum().values)
    st.plotly_chart(fig)

# Number of courses per Level
st.subheader("Number of Courses per Level")
fig = px.bar(data_frame = df, x = 'level', color='subject')
st.plotly_chart(fig)

# correlation
st.subheader("Correlation")
fig = px.imshow(df.corr(),text_auto =True)
st.plotly_chart(fig)


