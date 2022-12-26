import streamlit as st

def run_home_app():
    st.subheader('해당 사이트는 IMDB의 평가를 기반으로 --??테스트??--')
    st.subheader('역대 최고의 영화에 대한 정보를 제공합니다.')
    st.text('데이터 출처 :')
    st.text('https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows')

    st.title('')
    st.title('👑 Top 1000 Movies by IMDB Rating dkdjkdjdjdjdjdj')
    st.write('(상위 1000개의 영화 중 데이터가 미흡한 영화는 제외되었습니다.)')
    st.title('')
    st.subheader('IMDB 공식 유튜브 최신 영상')
    link_imdb = 'https://www.youtube.com/watch?v=-vvx2DmmDNI'
    st.video(link_imdb, format='video/mp4')
    st.text('')
    st.write("'IMDb'의 최신 정보는 공식 홈페이지에서 확인할 수 있습니다.")
    st.text('https://www.imdb.com/')