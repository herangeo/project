import streamlit as st
import pandas as pd

def main():
    st.title("Simple CSV File Explorer")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        st.write("### Data Preview")
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        st.write("### Basic Statistics")
        st.write(df.describe())

        st.write("### Column Names")
        st.write(df.columns.tolist())

        st.write("### Data Types")
        st.write(df.dtypes)

if __name__ == "__main__":
    main()
