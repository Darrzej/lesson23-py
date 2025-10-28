import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")

st.header("Add Developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)

if st.button ("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post("http://localhost:8000/developers/", json = dev_data)
    st.json(response.json())

st.header("Add Project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_area("Project description")
proj_lang = st.text_input("Languages used")
lead_dev_name = st.text_input("Developer name")
lead_dev_exp = st.number_input("Experience of the Developer (Years)", min_value=0, max_value=50, value=0)

if st.button("Create Project"):
    lead_dev_data = {"name":lead_dev_name, "Experience":lead_dev_exp}
    proj_data = {
        "title":proj_title,
        "Description":proj_desc,
        "Languages":proj_lang.split(","),
        "Lead Developer":lead_dev_data

    }
    response = requests.post("http://localhost:8000/projects/", json = proj_data)
    st.json(response.json())
