# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 22:09:37 2022

@author: Ramad
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title("Hello!")

heart_deases= pd.read_csv("C:/Users/Ramad/Desktop/heart_deases_2020.csv")

heart_deases.head()
heart_deases_sort=heart_deases.sort_values(by=["AgeCategory","SleepTime","MentalHealth","PhysicalHealth","BMI"], ascending=True)

st.title("How many hours do you sleep per day?")
x=st.slider('A number between 0-12', min_value=(0), max_value=(12))
st.write('Sleeping hours:', x)

st.title("Do you smoke?")
z=["YES","NO"]
y=st.radio('Navigation',z)

st.title("The following graphs represent different studies conducted on people with different health statuses:")


st.title("First graph:")
health_issue1=px.histogram(heart_deases_sort, x="GenHealth", y="PhysicalHealth", histfunc="sum", color="HeartDisease", title='GenHealth: Excellent has the lower PhysicalHealth and with no HeartDisease')
st.plotly_chart(health_issue1)
st.markdown('To avoid heart disease problems, you should always stay in excellent health and physical shape.')


st.title("Second graph:")
health_issue2= px.pie(heart_deases_sort, values='MentalHealth', names='KidneyDisease', title='Kidney Diseas: No accounts for the majority of Mental Health')
st.plotly_chart(health_issue2)



st.title("Third graph:")
health_issue3=px.scatter(heart_deases_sort,x="BMI", y="PhysicalHealth",color="Sex", hover_name="Diabetic", size="MentalHealth", title='Physical Health, Mental Health, Diabetic, By BMI')
st.plotly_chart(health_issue3)




st.title("Fourth graph:")
health_issue4=px.scatter(heart_deases_sort,x="BMI", y="PhysicalHealth", color="Smoking", animation_frame="SleepTime", hover_name="GenHealth", size="MentalHealth",log_x=True, range_x=[20,60], range_y=[-1,35])
st.plotly_chart(health_issue4)



st.title("Fifth graph:")
health_issue5=px.box(heart_deases_sort, x="AgeCategory", y="HeartDisease", orientation="h", color="Smoking", notched=True)
st.plotly_chart(health_issue5)






