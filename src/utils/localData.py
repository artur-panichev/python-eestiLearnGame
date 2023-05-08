import streamlit as st;
import json;

defaultData = {
    "token": 0
}
def loadData():
    localData = st.experimental_get_query_params();
    data = json.loads(localData['data'][0]);
    return data

def saveData():
    st.experimental_set_query_params(
        data=json.dumps(data)
    );

try:
    data = loadData();
except:
    data = defaultData;
    saveData();
    
st.write(str(data.get('token')))