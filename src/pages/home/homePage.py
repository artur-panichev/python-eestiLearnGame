import streamlit as st;

class HomePage:
    def __init__(self):
        
        with open('./src/pages/home/style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
        st.header('Home page');
        for i in range(1,5):
            st.header(f'Глава: {i}');
            col = st.columns(4)
            for j,e in enumerate(col):
                with e:
                    st.write(f'Уровень: {j}');
                    st.write('Статус: не завершен');
                    st.button('Начать', key=f'{i},{j}');