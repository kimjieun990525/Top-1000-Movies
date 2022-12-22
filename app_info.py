import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 차트에 한글 출력될 수 있도록 하는 명령------------
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')
# -------------------------------------------------
# 위 코드는 ec2에 한글 폰트가 설치되어 있어야 하고,
# 파이썬에서 한글 사용이 가능하도록 먼저 셋팅해야 한다.
# https://luvris2.tistory.com/119

def run_info_app():

    st.title('EDA : 데이터 분석 자료')

    df = pd.read_csv('imdb_movie_top_1000.csv')
    df.isna().sum()
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)


    Genre_list = 'War','Mystery','Crime','History','Animation','Fantasy','Action','Romance','Adventure','Sport','Sci-Fi','Drama','Thriller','Biography','Comedy','Musical','Western','Family','Film-Noir','Music','Horror'

    st.title('')
    st.title('')
    st.subheader('장르별 영화 정보')
    user_list = st.multiselect('보고싶은 영화의 장르를 선택하세요. (중복 선택 가능)',Genre_list)
    select_info = df[df['Genre'].str.contains(user_list) ]
    # 기본 출력 (제목, 평점, 장르)
    basic_info = select_info[ ['Series_Title','IMDB_Rating','Meta_score','Genre'] ] 
    status = st.radio('정렬 기준 선택', ['제목 기준', 'IMDB_Rating 기준', 'Meta_score 기준'])
    if status == '제목 기준' :
        st.dataframe( basic_info.sort_values('Series_Title') )
    elif status == 'IMDB_Rating 기준' :
        if status1 = st.radio('순서를 선택하세요.', ['오름차순', '내림차순'])
        st.dataframe( df.sort_values('petal_length', ascending=False ) )
    elif status == 'Meta_score 기준' :
        st.dataframe( df.sort_values('petal_length', ascending=False ) )




    st.dataframe(df)

