import streamlit as st
from PIL import Image
import time

progress_text = "Здоровье противника"
my_bar = st.progress(100, text=progress_text)
image = Image.open('Untitled.png')

st.image(image, caption='Снегровик')
title = st.text_input('"Слово на русском"')

my_bar2 = st.progress(0, text="Здоровье")

for percent_complete in range(100, 0, -10):
    time.sleep(2)
    my_bar2.progress(percent_complete, text="Здоровье")



