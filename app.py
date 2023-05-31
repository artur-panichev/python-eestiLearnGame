import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb+srv://kortex:53364277@eesti-learn.3ssguyr.mongodb.net/");

db = client["eesti-learn"];
table = db["users"];

col1, col2 = st.columns(2);

def auth(login, password):
    if not table.find_one({"login": login, "password": password}):
        st.error('Не верный логин или пароль!');
        return;
    st.success('Авторизован!');

with col1:
    st.title('Авторизация')
    authLogin = st.text_input('Логин', key='authL')
    authPassword = st.text_input('Пароль', key='authP', type="password")
    authBtn = st.button('Войти', key='authBtn')
    
    if authBtn:
        auth(authLogin, authPassword)

def reg(login, password, password2):
    if not 4 < len(login) < 13:
        st.error('Логин должен быть длиннее 4-х символов и короче 13');
        return;
    if not password == password2:
        st.error('Повторный пароль отличается от первого');
        return;
    if not 8 < len(password) < 65:
        st.error(f'Длинна пароля должна быть больше 8 символов и короче 65. Вы ввели {len(password)} символов');
        return;
    if table.find_one({"login": login}):
        st.error('Логин занят');
        return;
    table.insert_one({"login": login, "password": password, "lvl": 0});
    st.success('Зарегестрирован!');

with col2:
    st.title('Регистрация');
    regLogin = st.text_input('Логин', key='regL');
    regPassword = st.text_input('Пароль', key='regP', type="password");
    regPassword2 = st.text_input('Повтор пароля', key='regP2', type="password");
    regBtn = st.button('Зарегестрироваться', key='regBtn');
    
    if regBtn:
        reg(regLogin, regPassword, regPassword2);