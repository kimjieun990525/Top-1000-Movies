from streamlit_option_menu import option_menu

import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_info import run_info_app



def main() :

    with st.sidebar:
        choose = option_menu("MENU", ["Home", "EDA", "Film Information"],
                            icons=['house', 'activity', 'menu-app'],
                            menu_icon="app", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "#B5D4E8", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#28568E"},
        }
        )
    
    
    if choose == 'Home':
        run_home_app()
    elif choose == 'EDA' :
        run_eda_app()
    elif choose == 'Film Information' :
        run_info_app()


if __name__ == '__main__' :
    main()



