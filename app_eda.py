import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

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


def run_eda_app():


    st.title('▶  EDA : 데이터 분석 자료  ◀')

    df = pd.read_csv('imdb_movie_top_1000.csv')

    df.isna().sum()
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)

    st.title('')
    st.title(' IMDB 란 ?')
    st.text("'Internet Movie Database'의 약자로, 미국의 영화 정보 모음 사이트드다.")
    st.text('현재 아마존닷컴의 자회사이며 하위 서비스로 박스오피스 모조가 있다.')
    st.text('콜 니덤(Col Needham)이라는 프로그래머가 영화 《죠스》를 본 뒤에 영화 매니아가 되어서')
    st.text('인터넷 사업 초창기이던 1990년에 사이트를 개설한 것이 시초다. 1998년 4월 아마존닷컴이')
    st.text('IMDb를 인수하고, 2008년 아마존닷컴이 박스오피스 모조를 인수하면서 IMDb에 합병하였다.')

    st.title('')
    st.title('')
    st.header('역대 상위권 작품에 가장 많이 참여한 감독')
    st.write('체크박스를 클릭하면 각 감독이 참여한 영화를 확인할 수 있습니다.')
    if st.checkbox('[ 1위 ~ 10위 확인하기 ]') :
        if st.checkbox( '1위 : 스티븐 스필버그 (13개)') :
            df_1 = df.loc[ df['Director']== 'Steven Spielberg', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('2위 : 마틴 스코세이지 (10개)') :
            df_1 = df.loc[ df['Director']== 'Martin Scorsese', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('3위 : 알프레드 히치콕 (9개)') :
            df_1 = df.loc[ df['Director']== 'Alfred Hitchcock', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('4위 : 크리스토퍼 놀란 (8개)') :
            df_1 = df.loc[ df['Director']== 'Christopher Nolan', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('5위 : 데이빗 핀처 (8개)') :
            df_1 = df.loc[ df['Director']== 'David Fincher', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('6위 : 쿠엔틴 타란티노 (8개)') :
            df_1 = df.loc[ df['Director']== 'Quentin Tarantino', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('7위 : 클린트 이스트우드 (8개)') :
            df_1 = df.loc[ df['Director']== 'Clint Eastwood', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('8위 : 로브 라이너 (7개)') :
            df_1 = df.loc[ df['Director']== 'Rob Reiner', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('9위 : 우디 앨런 (7개)') :
            df_1 = df.loc[ df['Director']== 'Woody Allen', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))
        elif st.checkbox('10위 : 미야자키 하야오 (7개)') :
            df_1 = df.loc[ df['Director']== 'Hayao Miyazaki', ]
            st.dataframe(df_1[['Series_Title','IMDB_Rating','Meta_score','Genre']].set_index('Series_Title'))

# ---------------------------------------------------------------------------

 
    st.title('')
    st.title('')
    st.header('Top.1000 영화의 장르 비중')
    st.write('체크박스를 클릭하면 어떤 장르가 영화에서 비중을 많이 차지하는지 그래프를 볼 수 있습니다.')
    if st.checkbox('[ 그래프 확인하기 ]') :
        st.image('genre_bar2.png')




# ---------------------------------------------------------------------------

    st.title('')
    st.write('[ 컬럼 설명 ]')
    st.write('* Series_Title : Name of the movie (영화 제목)')
    st.write('* Released_Year : Year at which that movie released (개봉 년도)')
    st.write('* Runtime : Total runtime of the movie (러닝 타임)')
    st.write('* Genre : Genre of the movie (영화 장르)')
    st.write('* Overview : mini story/ summary (영화 줄거리)')
    st.write('* IMDB_Rating : Rating of the movie at IMDB site (IMDB 사이트의 영화 등급)')
    st.write('* Meta_score : Score earned by the movie (영화 점수)')
    st.write('* Director : Name of the Director (감독명)')
    st.write('* Star : Name of the Stars (배우 이름)')
    st.write('* Noofvotes : Total number of votes (평가 참여자 수)')
    st.write('* Gross - Money earned by that movie (영화 수익 = $)')
