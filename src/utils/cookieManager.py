import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager


cookies = EncryptedCookieManager(
    prefix="gamecookie/",
    password=os.environ.get("COOKIES_PASSWORD", "1bsdj198j1hw1hd0e29f1whdbe1gd2e97ey1"),
)
if not cookies.ready():
    st.stop()

try:
    st.write("Current cookies:", cookies['a-cookie'])
except:
    st.write("Current cookies:", 'None')
value = st.text_input("New value for a cookie")
if st.button("Change the cookie"):
    cookies['a-cookie'] = value
    if st.button("No really, change it now"):
        cookies.save()