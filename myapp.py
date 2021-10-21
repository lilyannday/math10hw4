#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 01:26:17 2021

@author: ydl1
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#Question 1
st.title("My App")

#Question 2
st.markdown("[Kaileen Chiu](https://github.com/kaileenc)")
st.markdown("[Lilyann Day](https://github.com/lilyannd)")

#Question 3
uploaded_file = st.file_uploader("file upload",['csv'])

#Question 4
#we want to convert the file to a pandas df
#But there will be an error if we don't have an uploaded file first
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    # if x is an empty string make it numpy's not a number 
    #otherwise, leave x alone
#Question 5
    df = df.applymap(lambda x: np.nan if x == " " else x)

#Question 6
    #see Week 3 Friday lecture!
    #Let c be the column name
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
        
    #Now, let's make a list of all the columns that can be made numeric
    
    good_cols = [c for c in df.columns if can_be_numeric(c)]
    
#Question 7
#Replace columns in df that can be made numeric with their numeric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)

#Question 8
#Select x-axis and y-axis from st.selectbox
    x_axis = st.selectbox("Choose an x-value",good_cols)
    y_axis = st.selectbox("Choose an y-value",good_cols)
    
#Question 9
    number_of_rows = st.slider("Choose number of rows to plot", 0, len(df.index)-1)
#Question 10
    st.write(f"This is the number of rows that will be plotted: {number_of_rows}")
#Question 11

    f = alt.Chart(df.iloc[:number_of_rows]).mark_circle().encode(
        x = x_axis, y = y_axis ,tooltip = [x_axis, y_axis])
    
    st.altair_chart(f, use_container_width=True)
    
#Question 12
    chart_data = pd.DataFrame(df[good_cols])
    st.bar_chart(chart_data)