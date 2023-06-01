import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from pymongo import MongoClient
from strgen import StringGenerator as SG
import datetime
import dateutil

date = str(datetime.datetime.now())
dt = dateutil.parser.parse(date)
print(dt + datetime.timedelta(days=1))

client = MongoClient("mongodb+srv://kortex:53364277@eesti-learn.3ssguyr.mongodb.net/");

db = client["eesti-learn"];
table = db["users"];
def regPage():
    col1, col2 = st.columns(2);

    def auth(login, password):
        if not table.find_one({"login": login, "password": password}):
            st.error('Не верный логин или пароль!');
            return;

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

        secret = SG("[\p\w]{32}").render();
        table.insert_one({"login": login, "password": password, "lvl": 0, "secret": secret, "keydate": str(datetime.datetime.now())});
        cookies['a-cookie'] = secret
        cookies.save()

    with col2:
        st.title('Регистрация');
        regLogin = st.text_input('Логин', key='regL');
        regPassword = st.text_input('Пароль', key='regP', type="password");
        regPassword2 = st.text_input('Повтор пароля', key='regP2', type="password");
        regBtn = st.button('Зарегестрироваться', key='regBtn');
        
        if regBtn:
            reg(regLogin, regPassword, regPassword2);
            
cookies = EncryptedCookieManager(
    prefix="gamecookie/",
    password=os.environ.get("COOKIES_PASSWORD", "327TG8TFD92YGD29FY3284YF"),
)


def autoAuth():
    try:
        secret = cookies['a-cookie'];
        if(secret == 'None'):
            regPage();
            return;
        user = table.find_one({"secret": secret});
        if not user:
            regPage();
            return;
        
        tokenExpire = dateutil.parser.parse(user["keydate"]) + datetime.timedelta(days=1)
        nowDate = datetime.datetime.now();
        print('_'*20)
        print(tokenExpire)
        print(nowDate)
        if not tokenExpire > datetime.datetime.now():
            regPage();
            return;
        logout = st.button('Logout', key='logoutBtn')
        if logout:
            cookies['a-cookie'] = 'None';
            cookies.save()
            st.experimental_rerun()
    except:
        regPage();
autoAuth()