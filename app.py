#python -m streamlit run ./app.py
import streamlit as st;

import sys
sys.path.append("./src/pages/home")
from homePage import *;
homePage = HomePage();