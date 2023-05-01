import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my-photo.jpg", width=300)

with col2:
    st.title("Bubai Bal")
    content = """Bubai Bal, AWS Solution Architect. Over 12 years of experience on architecting application and 
    cloud, helping customers on digital transformations and modernizations. Passionate about learning new 
    technologies and evolving patterns. Enjoys family time, gardening and travelling. """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me."""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
