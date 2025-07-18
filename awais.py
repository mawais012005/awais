from PIL import Image
import streamlit as st

image = Image.open("awais.jpg")  # yeh file aapke folder mein honi chahiye
st.image(image, caption="Muhammad Awais", width=300)
