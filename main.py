import streamlit as st
import numpy as np
import pickle

st.title("Iris Flower Classification App")
with open("model.pkl", "rb") as f:
    lr_model = pickle.load(f)
sl = st.slider("Insert a sepal Length", 0, 100, 25)
sw = st.slider("Insert a sepal Width", 0, 100, 25)
pl = st.slider("Insert a petal Length", 0, 100, 25)
pw = st.slider("Insert a petal Width", 0, 100, 25)
# pred = lr_model.predict(np.array([[sl, sw, pl, pw]]))
# st.write("The flower is :", pred[0])

if st.button("predict"):
    pred = lr_model.predict(np.array([[sl,sw,pl,pw]]))
    st.write("the flower is :",pred[0])