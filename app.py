import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_info import run_info_app



def main() :

    menu = ['Home', 'EDA', 'Film Information']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'Film Information' :
        run_info_app()


if __name__ == '__main__' :
    main()



