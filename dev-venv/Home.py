import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import duckdb
import numpy as np
import plotly.express as px
from supabase import client, create_client
import os
from dotenv import load_dotenv

load_dotenv()

# Set display options to show all columns
pd.set_option('display.max_columns', None)

### Import Supabase Credentials ####

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

#### Create Supabase Client ####

supabase: client = create_client(supabase_url, supabase_key)

#### Here we create all the functions we need to interact with Supabase and create app logic ####

# Function to retriveve team members #
def get_team_members():
    response = supabase.table('team_members').select('*').execute()
    df = pd.DataFrame(response.data)
    return df

# Function to retriveve projects #
def get_projects():
    response = supabase.table('projects').select('*').execute()
    df = pd.DataFrame(response.data)
    return df

# Function to retriveve teams and projects #
def get_projects_team_members():
    response = supabase.table('projects_team_members').select('*').execute()
    df = pd.DataFrame(response.data)
    return df

# Function to perform DuckDB analysis on the dataframe
def analyze_project_status(df):
    # Initialize DuckDB connection
    con = duckdb.connect(database=':memory:')
    
    # Register the DataFrame as a view in DuckDB
    con.register('projects_team_members', df)




#### Here we create the layout of the page, which will use the previously created functions ####

st.set_page_config(
    page_title="Home",
    layout= "wide"
)
st.sidebar.success("Select a page above")

col1, col2, col3 = st.columns(3)

with col1:
    st.text("First Column")
    
with col2:
    st.text("Second Column")
    
with col3:
    st.text("Third Column")


