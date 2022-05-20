from pyparsing import col
from sqlalchemy import column
import streamlit as st
import pandas as pd

def run_eda() :
        st.subheader('EDA 화면표시')

        df = pd.read_csv('data2/iris.csv')

        # 컬럼이름을 보여주시고, 여러 컬럼을 선택가능하도록 하여, 선택한 컬럼들만 화면에 보여주기
        column_list = st.multiselect('컬럼선택',df.columns)

        if len(column_list) != 0 :
            st.dataframe(df[column_list])


        # 상관계수를 구하여 화면에 보여주기
            st.dataframe(df[column_list].corr())