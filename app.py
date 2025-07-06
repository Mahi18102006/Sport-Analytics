import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sports Analytics", layout="centered")

st.markdown("""
    <style>
    .stApp {
    background-color: #f0f4f7;
    padding: 20px;
    border-radius: 10px;
    }
    h1 {
        color: #0d3b66;
    } 
    </style>
    """,unsafe_allow_html=True)

df = pd.read_csv("Sport_Data.csv")

st.title("🏏 Sports Analytics")

if st.checkbox("📄 Show Raw Data"):
    st.dataframe(df)

chart_type = st.selectbox("📊 Choose Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])

metric = st.selectbox("📈 Select Metric", ["Runs", "Wickets", "Matches"])

sorted_df = df.sort_values(by=metric, ascending=False)

if chart_type == "Bar Chart":
    st.subheader(f"📊 Bar Chart - Top {metric}")
    fig, ax = plt.subplots()
    ax.barh(sorted_df["Player"], sorted_df[metric], color="skyblue")
    ax.set_xlabel(metric)
    ax.set_title(f"Top {metric}")
    ax.invert_yaxis()
    st.pyplot(fig)
elif chart_type == "Line Chart":
    st.subheader(f"📈 Line Chart - {metric} by Player")
    fig, ax = plt.subplots()
    ax.plot(sorted_df["Player"], sorted_df[metric], marker='o', linestyle='-', color="orange")
    ax.set_ylabel(metric)
    ax.set_title(f"{metric} by Player")
    ax.set_xticklabels(sorted_df["Player"], rotation=45)
    st.pyplot(fig)

elif chart_type == "Pie Chart":
    st.subheader(f"Pie Chart - {metric} Distribution")
    fig, ax = plt.subplots()
    ax.pie(sorted_df[metric], labels=sorted_df["Player"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
