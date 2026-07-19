import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Ford GoBike Dashboard",
    page_icon="🚴",
    layout="wide"
)

st.title("🚴 Ford GoBike Data Analysis Dashboard")
st.markdown("### Exploratory Data Analysis using Python & Streamlit")

# -----------------------------------
# Load Dataset
# -----------------------------------
import os
import glob
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    # Folder where app.py is located
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Read all CSV files in the project folder
    csv_files = glob.glob(os.path.join(base_path, "*.csv"))

    if not csv_files:
        st.error("No CSV files found!")
        st.stop()

    # Read all CSV files
    df_list = []

    for file in csv_files:
        temp = pd.read_csv(file)
        df_list.append(temp)

    # Merge all files
    df = pd.concat(df_list, ignore_index=True)

    # Convert datetime columns
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    # Feature Engineering
    df["duration_min"] = df["duration_sec"] / 60
    df["hour"] = df["start_time"].dt.hour
    df["weekday"] = df["start_time"].dt.day_name()
    df["month"] = df["start_time"].dt.month_name()
    df["member_age"] = 2018 - df["member_birth_year"]

    return df


# Load dataset
df = load_data()
# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Dataset",
        "Univariate Analysis",
        "Bivariate Analysis",
        "Correlation",
        "Conclusion"
    ]
)

# -----------------------------------
# HOME
# -----------------------------------

if page=="Home":

    st.header("Project Overview")

    col1,col2,col3,col4=st.columns(4)

    col1.metric("Total Trips",len(df))
    col2.metric("Stations",df["start_station_name"].nunique())
    col3.metric("Subscribers",df[df.user_type=="Subscriber"].shape[0])
    col4.metric("Customers",df[df.user_type=="Customer"].shape[0])

    st.write(df.head())

# -----------------------------------
# DATASET
# -----------------------------------

elif page=="Dataset":

    st.header("Dataset")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    st.write(df.shape)

    st.subheader("Missing Values")

    st.write(df.isnull().sum())

# -----------------------------------
# UNIVARIATE
# -----------------------------------

elif page=="Univariate Analysis":

    st.header("Trip Duration Distribution")

    fig=px.histogram(
        df,
        x="duration_min",
        nbins=50
    )

    fig.update_xaxes(range=[0,60])

    st.plotly_chart(fig,use_container_width=True)

    st.header("Trips by User Type")

    fig=px.histogram(
        df,
        x="user_type",
        color="user_type"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.header("Trips by Gender")

    fig=px.histogram(
        df,
        x="member_gender",
        color="member_gender"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------------
# BIVARIATE
# -----------------------------------

elif page=="Bivariate Analysis":

    st.header("Trip Duration by User Type")

    fig=px.box(
        df,
        x="user_type",
        y="duration_min",
        color="user_type"
    )

    fig.update_yaxes(range=[0,60])

    st.plotly_chart(fig,use_container_width=True)

    st.header("Average Duration by Gender")

    fig=px.bar(
        df.groupby("member_gender")["duration_min"]
        .mean()
        .reset_index(),
        x="member_gender",
        y="duration_min",
        color="member_gender"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------------
# CORRELATION
# -----------------------------------

elif page=="Correlation":

    st.header("Correlation Heatmap")

    corr=df.select_dtypes("number").corr()

    fig,ax=plt.subplots(figsize=(10,7))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

# -----------------------------------
# CONCLUSION
# -----------------------------------

else:

    st.header("Business Insights")

    st.success("""
• Subscribers contribute the highest number of trips.

• Peak usage occurs during office commuting hours.

• Weekdays have significantly higher trips.

• Bike demand varies across months.

• Short rides dominate the dataset.

• Optimize bike availability during peak hours.

• Launch weekend offers to improve ridership.

• Expand subscriber membership.
""")
