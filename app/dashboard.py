import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up base directory and file path
base_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_dir, "data", "job_data.csv")

# Check if data file exists
if not os.path.exists(data_path):
    st.error("🚫 CSV file not found. Please make sure 'data/job_data.csv' exists.")
    st.stop()

# Load data
df = pd.read_csv(data_path)

# Skill keywords to extract from job summary
keywords = ['Python', 'SQL', 'Tableau', 'Excel', 'Power BI']
for kw in keywords:
    df[kw] = df['summary'].str.contains(kw, case=False, na=False)

# Page title
st.title("📊 U.S. Data Job Market Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filters")
locations = ["All"] + sorted(df["location"].dropna().unique().tolist())
location = st.sidebar.selectbox("Select location", options=locations)
skills = st.sidebar.multiselect("Filter by required skills", options=keywords)

# Filter data
filtered = df.copy()
if location != "All":
    filtered = filtered[filtered["location"] == location]
for skill in skills:
    filtered = filtered[filtered[skill]]

# Display filtered data
st.subheader(f"Showing {len(filtered)} jobs for location: {location}, with skills: {', '.join(skills) or 'All'}")
st.dataframe(filtered)

# Download button
st.download_button(
    label="📥 Download Filtered Jobs as CSV",
    data=filtered.to_csv(index=False),
    file_name='filtered_jobs.csv',
    mime='text/csv'
)

# Check for empty filtered result
if filtered.empty:
    st.warning("⚠️ No job postings match the selected filters.")
    st.stop()

# Top Job Titles
st.subheader("🏷️ Top Job Titles")
top_titles = filtered["title"].value_counts().head(10).sort_values()
fig, ax = plt.subplots()
top_titles.plot(kind="barh", ax=ax)
ax.set_xlabel("Count")
st.pyplot(fig)

# Top Hiring Companies
st.subheader("🏢 Top Hiring Companies")
top_companies = filtered["company"].value_counts().head(10).sort_values()
fig2, ax2 = plt.subplots()
top_companies.plot(kind="barh", ax=ax2)
ax2.set_xlabel("Count")
st.pyplot(fig2)

# Skill Mentions
st.subheader("🛠️ Skill Mentions in All Job Descriptions")
skill_counts = df[keywords].sum().sort_values(ascending=False)
fig3, ax3 = plt.subplots()
skill_counts.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Mentions")
st.pyplot(fig3)
