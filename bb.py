import streamlit as st

st.title('Авторизация')
authLogin = st.text_input('Логин', key='authL')
authPassword = st.text_input('Пароль', key='authP')
if st.button('Войти', key='authBtn'):
    print('Авторизация:')
    print(f'Логин: {authLogin}')
    print(f'Пароль: {authPassword}')

st.title('Регистрация')
regLogin = st.text_input('Логин', key='regL')
regPassword = st.text_input('Пароль', key='regP')
regPassword2 = st.text_input('Повтор пароля', key='regP2')
if st.button('Войти', key='regBtn'):
    print('Регистрация:')
    print(f'Логин: {regLogin}')
    print(f'Пароль: {regPassword}')
    print(f'Повтор пароля: {regPassword2}')