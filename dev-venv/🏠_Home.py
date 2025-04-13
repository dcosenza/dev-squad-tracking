import streamlit as st
import pandas as pd
import numpy as np
from supabase import client, create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase: client = create_client(supabase_url, supabase_key)

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.sidebar.success("Select a page above")


st.header("Project Status")

def get_team_members():
    response = supabase.table('team_members').select('*').execute()
    return response.data

st.write('### Team Members:')
team = get_team_members()
print(team)
if team:
    for people in team:
        st.write(f"-{people['first_name']} ")
else:
    st.write("No people available")