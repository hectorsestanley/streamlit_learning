# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function for the Home Page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the multi-page Streamlit app!")
    st.write("Navigate to the pages using the sidebar.")

# Function for the Data Page
def data_page():
    st.title("Data Page")
    st.write("This is the data page. Here's a sample dataframe:")
    
    # Generating a sample dataframe
    df = pd.DataFrame({
        'A': np.random.rand(50),
        'B': np.random.rand(50),
        'C': np.random.randint(0, 100, 50)
    })
    
    st.write(df)

# Function for the Visualization Page
def visualization_page():
    st.title("Visualization Page")
    st.write("Here's a sample plot:")

    # Generating random data for plotting
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)
    
   
