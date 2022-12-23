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

    st.title('🍥 Film Info : 영화 상세 정보')

    df = pd.read_csv('imdb_movie_top_1000.csv')
    df.isna().sum()
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)


    Genre_list = 'War','Mystery','Crime','History','Animation','Fantasy','Action','Romance','Adventure','Sport','Sci-Fi','Drama','Thriller','Biography','Comedy','Musical','Western','Family','Film-Noir','Music','Horror'

    st.title('')
    st.subheader('▶ 장르별 영화 정보')
    user_list = st.multiselect('보고싶은 영화의 장르를 선택하세요. (중복 선택 가능)',Genre_list)
    user = '|'.join(user_list)
    select_info = df[df['Genre'].str.contains(user) ]
    
    # 기본 출력 (제목, 평점, 장르)
    basic_info = select_info[ ['Series_Title','IMDB_Rating','Meta_score','Genre'] ]
    

    # 정렬 기준 선택지
    status = st.radio('정렬 기준 선택', ['','제목 기준', 'IMDB_Rating 기준', 'Meta_score 기준'])
    
    if status == '제목 기준' :
        df1 = basic_info.sort_values('Series_Title')
        st.dataframe( df1.reset_index().drop('index', axis=1) )
    
    elif status == 'IMDB_Rating 기준' :
        st.write('')
        st.write('** IMDB_Rating **')
        st.text(' IMDB 사이트에서 평가된 영화 점수')
        status1 = st.radio('순서를 선택하세요.', ['높은 점수', '낮은 점수'])
        if status1 == '높은 점수' :
            df1 = basic_info.sort_values('IMDB_Rating', ascending=False)
            st.dataframe( df1.reset_index().drop('index', axis=1) )
        elif status1 == '낮은 점수' :
            df1 = basic_info.sort_values('IMDB_Rating', ascending=True)
            st.dataframe( df1.reset_index().drop('index', axis=1) )
    
    elif status == 'Meta_score 기준' :
        st.write('** Meta_score **')
        st.text(' 북미의 영화, TV 프로그램, 게임 및 음악 리뷰 모음 집계 사이트인 메타크리틱(Metacritic)에서')
        st.text('각종 신문이나 잡지 등의 매체에서 올라온 리뷰들을 통계화하여 집계한 점수')
        st.write('')
        status1 = st.radio('순서를 선택하세요.', ['높은 점수', '낮은 점수'])
        if status1 == '높은 점수' :
            df1 = basic_info.sort_values('Meta_score', ascending=False)
            st.dataframe( df1.reset_index().drop('index', axis=1) )
        elif status1 == '낮은 점수' :
            df1 = basic_info.sort_values('Meta_score', ascending=True)
            st.dataframe( df1.reset_index().drop('index', axis=1) )
    else :
        st.dataframe(basic_info.reset_index().drop('index', axis=1))


    st.title('')
    st.subheader('- 상기 목록에 대한 상세 정보')
    if st.checkbox('1단계 : 제목/인물 검색하기') :
        user_search = st.text_input('상기 영화 목록에서 영화의 제목 또는 관련된 인물을 검색을 할 수 있습니다.')
        if user_search :
            # 검색 (제목, 인물 중에서 해당 텍스트가 포함된 것을 검색한다. 대소문자 구분 X)
            search_info = select_info[ ['Series_Title', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4'] ]
            search_info2 = search_info[search_info['Series_Title'].str.contains(user_search, case=False) |
                    search_info['Director'].str.contains(user_search, case=False) |
                    search_info['Star1'].str.contains(user_search, case=False) |
                    search_info['Star2'].str.contains(user_search, case=False) |
                    search_info['Star3'].str.contains(user_search, case=False) |
                    search_info['Star4'].str.contains(user_search, case=False)]
            st.dataframe(search_info2.reset_index().drop('index', axis=1))
            st.text('')

            if st.checkbox('2단계 : 영화 선택하기') :
                box_data = search_info2['Series_Title'].values
                user_select = st.selectbox('영화를 선택하면 상세 정보를 확인할 수 있습니다.', box_data)
                select_result = df.loc[df['Series_Title'] == user_select, ]
                st.title('')
                st.write('영화 정보 -------------------------------------------------------------------------------------------------------------')
                st.header(select_result['Series_Title'].values[0])
                st.write('* 개봉년도 : ', str(select_result['Released_Year'].values[0]))
                st.write('* 상영시간 : ', select_result['Runtime'].values[0])
                st.write('* 감독 : ', select_result['Director'].values[0])
                st.write('* 주연 : ', select_result['Star1'].values[0], ', ', select_result['Star2'].values[0],
                ', ', select_result['Star3'].values[0], ', ', select_result['Star4'].values[0], )
                st.subheader('')
                st.subheader('[ 줄거리 ]')
                st.write(select_result['Overview'].values[0])
                str(select_result['Overview'].values[0])
                st.subheader('')
                st.image(select_result['Poster_Link'].values[0])




            
        
    
    



