import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    return data

data = load_data('DataAnalyst.csv')

# Title and description
st.title('Data Analyst Job Visualization Tool')
st.write('Explore data analyst job listings with various filters and visualizations.')

# Sidebar filters
st.sidebar.header('Filter Options')
location = st.sidebar.multiselect('Select Location', options=data['Location'].unique())
company = st.sidebar.multiselect('Select Company', options=data['Company Name'].unique())
sector = st.sidebar.multiselect('Select Sector', options=data['Sector'].unique())

# Apply filters
if location:
    data = data[data['Location'].isin(location)]
if company:
    data = data[data['Company Name'].isin(company)]
if sector:
    data = data[data['Sector'].isin(sector)]

# Show data
st.write('### Job Listings Data', data)

# Visualization 1: Salary Estimate Distribution
st.write('### Salary Estimate Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Salary Estimate'].dropna(), kde=True, ax=ax)
st.pyplot(fig)

# Visualization 2: Average Rating by Company
st.write('### Average Rating by Company')
avg_rating = data.groupby('Company Name')['Rating'].mean().sort_values(ascending=False)
st.bar_chart(avg_rating)

# Visualization 3: Job Counts by Location
st.write('### Job Counts by Location')
job_counts = data['Location'].value_counts()
st.bar_chart(job_counts)

# Visualization 4: Company Size Distribution
st.write('### Company Size Distribution')
fig, ax = plt.subplots()
sns.countplot(y='Size', data=data, order=data['Size'].value_counts().index)
st.pyplot(fig)

# Visualization 5: Jobs by Sector
st.write('### Jobs by Sector')
fig, ax = plt.subplots()
sns.countplot(y='Sector', data=data, order=data['Sector'].value_counts().index)
st.pyplot(fig)

# Footer
st.write('App created by Vedant Karmankar')
