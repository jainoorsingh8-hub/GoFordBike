# **Project Name**    - Exploratory Data Analysis of the Ford GoBike Bike Sharing System (2018)

# **Project Type**    - EDA
# **Contribution**    - Individual
# **Team Member 1 **  - Jainoor Singh Saini

# **Project Summary -**
# The Ford GoBike Sharing System is a bicycle-sharing service that provides an eco-friendly, convenient, and affordable mode of transportation for daily commuters and casual riders. This project focuses on performing Exploratory Data Analysis (EDA) on the Ford GoBike trip data collected throughout the year 2018. The dataset contains detailed information about individual bike trips, including trip duration, start and end timestamps, station details, user type, member gender, birth year, and bike-sharing status.
# The primary objective of this project is to understand rider behavior, identify travel patterns, and generate meaningful business insights that can help improve the efficiency and effectiveness of the bike-sharing service. To achieve this, the monthly datasets are combined into a single dataset, followed by data cleaning, handling missing values, removing duplicates, and creating new features such as ride duration in minutes, rider age, month, weekday, and hour of the trip.
# Exploratory Data Analysis is then performed using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn. Various univariate, bivariate, and multivariate visualizations are created to study ride frequency, trip duration, user demographics, station popularity, hourly and monthly ride trends, and relationships between different variables. Correlation analysis and outlier detection are also carried out to better understand the characteristics of the dataset.
# The analysis aims to answer important business questions such as identifying the busiest months and hours, comparing ride behavior between Subscribers and Customers, analyzing gender-wise usage patterns, determining the most popular bike stations, and understanding factors that influence trip duration. These insights can help the company optimize bike availability, improve station management, plan maintenance schedules, and design targeted marketing campaigns for different customer segments.
# Overall, this project demonstrates how Exploratory Data Analysis can transform raw transportation data into valuable business intelligence. The findings can support data-driven decision-making, improve operational efficiency, enhance customer satisfaction, and contribute to the sustainable growth of the Ford GoBike Sharing System.

# Problem Statement
# The Ford GoBike Sharing System generates a large amount of trip data every day, including ride duration, start and end stations, trip timings, user demographics, and membership details. However, raw data alone does not provide meaningful insights that can support business decisions. Understanding customer travel behavior, peak usage periods, station demand, and rider demographics is essential for improving operational efficiency and customer satisfaction.
# The challenge is to analyze the 2018 Ford GoBike trip data to identify trends, usage patterns, and factors that influence bike-sharing demand. By performing Exploratory Data Analysis (EDA), the project aims to uncover hidden patterns, detect data quality issues, and answer key business questions related to user behavior, station popularity, trip duration, and seasonal demand.
# The insights obtained from this analysis can help optimize bike distribution, improve station management, enhance customer experience, and support strategic planning for future growth of the bike-sharing service.

# **Define Your Business Objective?**
# The primary business objective of this project is to analyze the Ford GoBike Sharing System data to gain actionable insights into customer usage patterns and operational performance.
# The specific objectives are:
# - To understand customer riding behavior across different months, weekdays, and hours of the day.
# - To identify the busiest stations and peak riding periods for efficient bike allocation.
# - To compare riding patterns between Subscribers and Customers.
# - To analyze the impact of demographic factors such as gender and age on bike usage.
# - To study trip duration and identify factors influencing longer or shorter rides.
# - To detect missing values, duplicates, and outliers to improve data quality.
# - To generate meaningful visualizations and business insights that support data-driven decision-making.
# - To provide recommendations that help improve operational efficiency, customer satisfaction, resource planning, and future business growth.

# The findings from this Exploratory Data Analysis will enable the Ford GoBike Sharing System to optimize bike availability, improve station utilization, enhance service quality, and design effective marketing strategies based on customer behavior.

# Import Required Libraries
# Data Manipulation Libraries
import pandas as pd
import numpy as np

# Data Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# File Handling Libraries
import glob
import os

# Date and Time Library
from datetime import datetime

# Ignore Warning Messages
import warnings
warnings.filterwarnings('ignore')

# ==========================================================
# Visualization Settings
# ==========================================================

# Set Seaborn theme
sns.set_style("whitegrid")

# Set default figure size
plt.rcParams["figure.figsize"] = (12, 6)

# Display all columns
pd.set_option('display.max_columns', None)

# Display maximum rows while inspecting data
pd.set_option('display.max_rows', 100)

# Display width
pd.set_option('display.width', 1000)

# ==========================================================
# Confirmation Message
# ==========================================================

print("=" * 60)
print("✅ All Required Libraries Imported Successfully")
print("=" * 60)


# DATASET LOADING

# Absolute path to your dataset folder
folder_path = r"C:\Users\pabla\OneDrive\Desktop\FordGoBike"

# Find all CSV files
csv_files = sorted(glob.glob(os.path.join(folder_path, "*.csv")))

print(f"Total CSV files found: {len(csv_files)}")
print(csv_files)

# Merge all datasets
df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

print("Dataset Shape:", df.shape)

# DISPLAY THE FIRST FIVE ROWS OF DATASET

print(df.head())

### Dataset Rows & Columns count

rows, columns = df.shape

print("=" * 50)
print("Dataset Rows & Columns Count")
print("=" * 50)
print(f"Total Rows    : {rows:,}")
print(f"Total Columns : {columns}")
print("=" * 50)

# DATASET INFORMATION

print("=" * 60)
print("Dataset Information")
print("=" * 60)

# Display dataset information
df.info()

# Dataset Duplicate Value Count

duplicate_count = df.duplicated().sum()

print("=" * 60)
print("Duplicate Value Count")
print("=" * 60)
print(f"Total Duplicate Rows : {duplicate_count}")
print("=" * 60)

# Missing Values/Null Values Count

missing_values = df.isnull().sum()

# Calculate percentage of missing values
missing_percentage = (missing_values / len(df)) * 100

# Create a DataFrame
missing_df = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage (%)': missing_percentage.round(2)
})

# Display only columns having missing values
missing_df = missing_df[missing_df['Missing Values'] > 0]

print("=" * 70)
print("Missing Values / Null Values Count")
print("=" * 70)
print(missing_df.sort_values(by='Missing Values', ascending=False))

# Visualizing the missing values

plt.figure(figsize=(12,6))

missing_df.sort_values(by='Missing Values', ascending=False)['Missing Values'].plot(
    kind='bar',
    color='skyblue'
)

plt.title("Missing Values Count by Column")
plt.xlabel("Columns")
plt.ylabel("Missing Values")
plt.xticks(rotation=45)

plt.show()

# What did you know about your dataset?

# After performing the initial exploration of the Ford GoBike dataset, the following observations were made:

# - The dataset contains **1,863,721 trip records** with **16 features** describing each bike ride.
# - It includes information related to trip duration, trip start and end time, station details, bike ID, user type, member gender, birth year, and bike-sharing status.
# - The dataset contains a combination of **numerical**, **categorical**, and **date/time** variables.
# -No duplicate records were found in the dataset, indicating that each trip is unique.
# - A few columns contain missing values, primarily in rider demographic information (`member_gender`, `member_birth_year`) and station information (`start_station_id`, `start_station_name`, `end_station_id`, and `end_station_name`).
# - The `start_time` and `end_time` columns are stored as **object** data types and need to be converted into **datetime** format to extract useful features such as month, day, hour, and weekday.
# - The dataset is large enough to perform meaningful exploratory data analysis and identify riding trends, customer behavior, station popularity, and temporal patterns.
# - Before visualization, the missing values and data types should be handled appropriately to ensure accurate analysis.

# Overall, the dataset is rich in trip-level information and provides sufficient data to answer important business questions related to customer usage patterns, operational efficiency, and bike-sharing demand.

# Dataset Columns

# Display all column names
print("=" * 60)
print("Dataset Columns")
print("=" * 60)

for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

# Dataset Describe

print("=" * 70)
print("Statistical Summary of Numerical Features")
print("=" * 70)
# Display summary statistics
df.describe(include='all')

# Check Unique Values for Each Variable

# Count unique values in each column
unique_values = pd.DataFrame({
    "Column Name": df.columns,
    "Unique Values": df.nunique().values
})

unique_values

# Display unique values for each column

for column in df.columns:
    print("=" * 70)
    print(f"Column Name : {column}")
    print(f"Number of Unique Values : {df[column].nunique()}")
    print(df[column].unique()[:20])   # Displays first 20 unique values
    print()


# ==========================================================
# Data Wrangling / Data Cleaning
# ==========================================================

# Create a copy of the original dataset
df_clean = df.copy()

print("="*60)
print("Starting Data Cleaning...")
print("="*60)

# ----------------------------------------------------------
# 1. Remove Duplicate Rows
# ----------------------------------------------------------

duplicates = df_clean.duplicated().sum()
print(f"Duplicate Rows Before Removing : {duplicates}")

df_clean.drop_duplicates(inplace=True)

print(f"Dataset Shape After Removing Duplicates : {df_clean.shape}")

# ----------------------------------------------------------
# 2. Convert Date Columns
# ----------------------------------------------------------

df_clean['start_time'] = pd.to_datetime(df_clean['start_time'])
df_clean['end_time'] = pd.to_datetime(df_clean['end_time'])

# ----------------------------------------------------------
# 3. Create Ride Duration in Minutes
# ----------------------------------------------------------

df_clean['duration_min'] = df_clean['duration_sec'] / 60

# ----------------------------------------------------------
# 4. Extract Date Features
# ----------------------------------------------------------

df_clean['year'] = df_clean['start_time'].dt.year
df_clean['month'] = df_clean['start_time'].dt.month_name()
df_clean['day'] = df_clean['start_time'].dt.day
df_clean['weekday'] = df_clean['start_time'].dt.day_name()
df_clean['hour'] = df_clean['start_time'].dt.hour

# ----------------------------------------------------------
# 5. Calculate Member Age
# ----------------------------------------------------------

df_clean['member_age'] = 2018 - df_clean['member_birth_year']

# ----------------------------------------------------------
# 6. Remove Invalid Ages
# ----------------------------------------------------------

df_clean = df_clean[
    (df_clean['member_age'] >= 15) &
    (df_clean['member_age'] <= 90)
]

# ----------------------------------------------------------
# 7. Remove Negative or Zero Ride Duration
# ----------------------------------------------------------

df_clean = df_clean[df_clean['duration_min'] > 0]

# ----------------------------------------------------------
# 8. Handle Missing Values
# ----------------------------------------------------------

print("\nMissing Values Before Cleaning")
print(df_clean.isnull().sum())

# Drop rows with missing demographic information
df_clean.dropna(
    subset=[
        'member_gender',
        'member_birth_year'
    ],
    inplace=True
)

print("\nMissing Values After Cleaning")
print(df_clean.isnull().sum())

# ----------------------------------------------------------
# Final Dataset Shape
# ----------------------------------------------------------

print("\nFinal Dataset Shape")
print(df_clean.shape)

print("\nData Cleaning Completed Successfully.")


# What all manipulations have you done and insights you found?

# During the data wrangling and preprocessing stage, several transformations were performed to prepare the dataset for accurate analysis and visualization.
# **Data Manipulations Performed:**

#- Combined all 12 monthly Ford GoBike datasets into a single DataFrame.
#- Removed duplicate records to ensure data consistency.
#- Converted the `start_time` and `end_time` columns from object type to datetime format.
#- Created new features including:
# - **Ride Duration (minutes)**
#  - **Ride Year**
#  - **Ride Month**
#  - **Ride Day**
#  - **Ride Weekday**
#  - **Ride Hour**
#  - **Member Age**
#- Removed records with invalid member ages (less than 15 years or greater than 90 years).
#- Removed trips with zero or negative ride duration.
#- Identified missing values across all columns.
#- Removed rows containing missing values in important demographic fields such as `member_gender` and `member_birth_year`.
#- Created a cleaned dataset (`df_clean`) for all further analysis and visualizations.

# **Insights Found:**

#- The dataset contains a large number of bike trips, making it suitable for meaningful exploratory analysis.
#- Most missing values are present in rider demographic and station-related columns.
#- Date and time features provide opportunities to analyze riding patterns by month, weekday, and hour.
#- Rider age can be derived from the birth year, allowing demographic analysis.
#- Removing invalid ages and incomplete demographic records improves the reliability of the analysis.
#- The cleaned dataset is well-structured and ready for univariate, bivariate, and multivariate analysis to generate business insights.



# ==========================================================
# Chart 1 : Distribution of Trip Duration
# ==========================================================

plt.figure(figsize=(12,6))

sns.histplot(
    data=df_clean,
    x='duration_min',
    bins=50,
    kde=True,
    color='royalblue'
)

plt.title('Distribution of Trip Duration', fontsize=16)
plt.xlabel('Trip Duration (Minutes)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.xlim(0, 60)      # Focus on rides up to 60 minutes
plt.grid(alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A histogram is the most suitable visualization for understanding the distribution of a continuous numerical variable such as trip duration. It clearly shows how frequently different ride durations occur and helps identify skewness, peaks, and possible outliers in the data.

# What is/are the insight(s) found from the chart?
#  Most bike rides are of short duration.
#  The highest number of trips fall within the first few minutes.
#  The distribution is positively skewed, indicating that longer trips are much less common.
#  A small number of rides have exceptionally long durations, suggesting the presence of outliers.

# Will the gained insights help create a positive business impact?
#  Yes. Since most customers use the bikes for short trips, the company can optimize bike availability at high-demand stations and ensure rapid bike turnover. This information can also help in planning maintenance schedules and pricing strategies for short-distance commuters.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. Extremely long-duration trips may indicate delayed bike returns, misuse of the service, or system issues.


# ==========================================================
# Chart 2 : Distribution of User Types
# ==========================================================

plt.figure(figsize=(8,6))

sns.countplot(
    data=df_clean,
    x='user_type',
    hue='user_type',
    palette='Set2',
    legend=False
)

plt.title('Distribution of User Types', fontsize=16)
plt.xlabel('User Type', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)

# Display count labels on bars
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container, fmt='%d')

plt.grid(axis='y', alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A count plot is the most appropriate chart for visualizing the frequency of categorical variables. It clearly shows the number of trips made by each user type, making comparisons simple and effective.

# What is/are the insight(s) found from the chart?
#  The majority of trips are made by **Subscribers**.
#  Customers contribute a significantly smaller number of trips.
#  This indicates that regular members are the primary users of the bike-sharing service.

# Will the gained insights help create a positive business impact?
#  Yes. Since Subscribers generate most of the trips, the company should focus on retaining existing members by improving service quality and introducing loyalty rewards. Additionally, targeted promotions can encourage Customers to upgrade to subscription plans, increasing recurring revenue.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. The relatively low number of Customer trips suggests that occasional users may not be converting into long-term subscribers. If this trend continues, the company may miss opportunities to grow its subscriber base and maximize revenue.


# ==========================================================
# Chart 3 : Distribution of Member Gender
# ==========================================================

plt.figure(figsize=(8,6))

sns.countplot(
    data=df_clean,
    x='member_gender',
    hue='member_gender',
    palette='viridis',
    legend=False
)

plt.title('Distribution of Member Gender', fontsize=16)
plt.xlabel('Member Gender', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)

# Display count labels on bars
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container)

plt.grid(axis='y', alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A count plot is the most suitable visualization for comparing the frequency of different categories in a categorical variable. It clearly shows the number of trips made by members of each gender.

# What is/are the insight(s) found from the chart?
#  Male members account for the highest number of bike trips.
#  Female members contribute a smaller share of total trips.
#  The "Other" gender category represents only a small percentage of users.
#  This indicates that the current user base is predominantly male.

# Will the gained insights help create a positive business impact?
#  Yes. Understanding the gender distribution helps the company design targeted marketing campaigns and customer engagement strategies. If female participation is comparatively lower, the company can introduce initiatives such as safety campaigns, promotional offers, or community events to encourage more female riders and broaden the customer base.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. A significant imbalance in gender participation suggests that the bike-sharing service may not be equally attractive or accessible to all user groups. If this imbalance persists, the company may miss opportunities to increase ridership by expanding its appeal to underrepresented demographics.



# ==========================================================
# Chart 4 : Number of Trips by Month
# ==========================================================

# Arrange months in calendar order
month_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

plt.figure(figsize=(12,6))

sns.countplot(
    data=df_clean,
    x='month',
    hue='month',
    order=month_order,
    palette='crest',
    legend=False
)

plt.title('Number of Trips by Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)

plt.xticks(rotation=45)

# Display count labels
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container, fontsize=8)

plt.grid(axis='y', alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A count plot is ideal for comparing the number of trips across different months. It helps identify seasonal trends, periods of high demand, and months with lower bike usage.

# What is/are the insight(s) found from the chart?
#  Bike usage varies across different months of the year.
#  Some months record significantly higher trip volumes, indicating peak demand.
#  Lower trip counts in certain months may be influenced by weather conditions, holidays, or seasonal commuting patterns.
#  The chart helps identify periods when bike-sharing services experience the highest and lowest demand.

# Will the gained insights help create a positive business impact?
#  Yes. Monthly trip analysis enables the company to forecast demand, allocate bikes more efficiently, schedule maintenance during low-demand periods, and launch marketing campaigns during slower months to increase ridership.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. Months with consistently lower trip volumes may indicate reduced customer engagement due to seasonal factors or operational challenges. If demand remains low during these periods without corrective measures, it can negatively impact revenue and fleet utilization.


# ==========================================================
# Chart 5 : Number of Trips by Weekday
# ==========================================================

# Arrange weekdays in correct order
weekday_order = [
    'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday'
]

plt.figure(figsize=(10,6))

sns.countplot(
    data=df_clean,
    x='weekday',
    order=weekday_order,
    hue='weekday',
    palette='mako',
    legend=False
)

plt.title('Number of Trips by Weekday', fontsize=16)
plt.xlabel('Weekday', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)

plt.xticks(rotation=30)

# Display count labels
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container, fontsize=8)

plt.grid(axis='y', alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A count plot is ideal for comparing the number of trips across different weekdays. It helps identify weekly travel patterns and shows how bike usage changes between weekdays and weekends.

# What is/are the insight(s) found from the chart?
#  Bike usage varies across the days of the week.
#  Weekdays generally record a higher number of trips than weekends.
#  This suggests that many users rely on the bike-sharing service for daily commuting.
#  Weekend trip patterns may indicate more recreational or leisure rides.

# Will the gained insights help create a positive business impact?
#  Yes. Understanding weekday demand helps the company optimize bike availability, staffing, and maintenance schedules. Additional bikes can be deployed during high-demand weekdays, while promotional campaigns can encourage more weekend usage.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. If weekend demand remains consistently lower than weekday demand, it may result in underutilization of bikes during those periods. The company may need to introduce weekend discounts, family ride packages, or special events to improve bike usage and revenue.



# ==========================================================
# Chart 6 : Number of Trips by Hour of the Day
# ==========================================================

plt.figure(figsize=(12,6))

sns.countplot(
    data=df_clean,
    x='hour',
    hue='hour',
    palette='viridis',
    legend=False
)

plt.title('Number of Trips by Hour of the Day', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)

# Display count labels
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container, fontsize=7, rotation=90)

plt.grid(axis='y', alpha=0.3)

plt.show()


# Why did you pick the specific chart?
#  A count plot is the most suitable visualization for comparing the number of bike trips across different hours of the day. It helps identify peak usage periods, daily travel patterns, and customer commuting behavior.

# What is/are the insight(s) found from the chart?
#  Bike usage is not evenly distributed throughout the day.
#  The highest number of trips typically occurs during morning and evening hours, corresponding to office commuting times.
#  Ride activity is comparatively lower during late-night and early-morning hours.
#  The chart indicates that the bike-sharing service is widely used for daily commuting rather than overnight travel.

# Will the gained insights help create a positive business impact?
#  Yes. Identifying peak demand hours enables the company to optimize bike distribution, staffing, and maintenance schedules. Additional bikes can be deployed during busy hours to improve availability and customer satisfaction, while maintenance can be scheduled during low-demand periods.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. Low demand during certain hours of the day may result in idle bikes and reduced fleet utilization. If bikes remain unused for long periods, operational efficiency decreases. The company can address this by offering off-peak discounts or promotional pricing to encourage usage during quieter hours.


# ==========================================================
# Chart 7 : Trip Duration by User Type
# ==========================================================

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df_clean,
    x='user_type',
    y='duration_min',
    hue='user_type',
    palette='Set2',
    legend=False
)

plt.title('Trip Duration by User Type', fontsize=16)
plt.xlabel('User Type', fontsize=12)
plt.ylabel('Trip Duration (Minutes)', fontsize=12)

# Limit y-axis for better visualization
plt.ylim(0, 60)

plt.grid(axis='y', alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A box plot is ideal for comparing the distribution of a numerical variable across different categories. It displays the median, quartiles, spread, and potential outliers, making it easy to compare trip durations between Subscribers and Customers.

# What is/are the insight(s) found from the chart?
#  Customers generally have longer trip durations than Subscribers.
#  Subscribers tend to take shorter and more consistent trips, indicating regular commuting behavior.
#  Customers show greater variation in ride duration, suggesting they often use bikes for leisure or occasional travel.
#  The presence of outliers indicates that a few users take exceptionally long trips.

# Will the gained insights help create a positive business impact?
#  Yes. Understanding ride duration by user type enables the company to create targeted pricing and membership plans. Subscribers can be offered commuter-focused benefits, while Customers can be encouraged to convert into Subscribers through promotional offers and membership discounts.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. Longer ride durations by Customers may reduce bike availability for other users during peak hours. If not managed properly, this could increase waiting times, reduce customer satisfaction, and lower overall fleet efficiency.



# ==========================================================
# Chart 8 : Average Trip Duration by Member Gender
# ==========================================================

plt.figure(figsize=(8,6))

sns.barplot(
    data=df_clean,
    x='member_gender',
    y='duration_min',
    hue='member_gender',
    estimator=np.mean,
    palette='viridis',
    legend=False
)

plt.title('Average Trip Duration by Member Gender', fontsize=16)
plt.xlabel('Member Gender', fontsize=12)
plt.ylabel('Average Trip Duration (Minutes)', fontsize=12)

# Display average values on bars
ax = plt.gca()
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f')

plt.grid(axis='y', alpha=0.3)

plt.show()

# Why did you pick the specific chart?
#  A bar chart is suitable for comparing the average trip duration across different gender categories. It provides a clear visual comparison of how ride duration varies among male, female, and other members.

# What is/are the insight(s) found from the chart?
#  The average trip duration differs across gender groups.
#  Male and female members may exhibit different riding patterns.
#  The "Other" category may show greater variation due to a relatively smaller number of users.
#  These differences help understand customer behavior across demographic groups.

# Will the gained insights help create a positive business impact?
#  Yes. Analyzing ride duration by gender helps the company understand customer preferences and design targeted marketing campaigns, promotional offers, and customer engagement strategies. These insights can also support initiatives aimed at increasing participation among underrepresented user groups.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. If one demographic group consistently shows lower usage or shorter ride durations, it may indicate lower engagement with the bike-sharing service. Without targeted initiatives to improve participation, the company could miss opportunities to expand its customer base and increase overall ridership.



# ==========================================================
# Chart 9 : Correlation Heatmap
# ==========================================================

# Select only numerical columns
numerical_df = df_clean.select_dtypes(include=['int64', 'float64'])

# Calculate correlation matrix
correlation_matrix = numerical_df.corr()

# Plot heatmap
plt.figure(figsize=(12,8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Numerical Features", fontsize=16)

plt.show()

# Why did you pick the specific chart?
#  A correlation heatmap is useful for understanding the relationship between multiple numerical variables simultaneously. It helps identify positive, negative, or weak correlations, making it easier to detect patterns, dependencies, and potential multicollinearity among features.

#What is/are the insight(s) found from the chart?
#  Most numerical variables show weak to moderate correlations, indicating that they capture different aspects of the bike-sharing data.
#  Start and end station coordinates (latitude and longitude) are likely to exhibit relatively strong positive correlations because trips occur within the same geographic service area.
#  Member age generally has a weak correlation with trip duration, suggesting that age alone is not a strong predictor of ride length.
#  The heatmap highlights which variables are closely related and which operate independently.

# Will the gained insights help create a positive business impact?
#  Yes. Correlation analysis helps identify the most influential variables affecting customer behavior. These insights support feature selection for predictive models, improve operational decision-making, and help the company focus on factors that have the greatest impact on bike usage and service efficiency.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. If strong correlations indicate redundancy between variables, retaining all of them in predictive models may increase complexity without improving performance. Additionally, variables with very weak relationships may contribute little to business decision-making and can be reviewed during feature selection for future analytics projects.



# ==========================================================
# Chart 10 : Pair Plot 
# ==========================================================

# Take a random sample for faster plotting
pairplot_df = df_clean[
    [
        'duration_min',
        'member_age',
        'start_station_latitude',
        'start_station_longitude'
    ]
].dropna().sample(3000)

sns.pairplot(
    pairplot_df,
    diag_kind='hist'
)

plt.show()

# Why did you pick the specific chart?
#  A pair plot is an effective multivariate visualization that displays pairwise relationships between numerical variables. It combines scatter plots and distribution plots, making it easy to identify trends, clusters, correlations, and potential outliers across multiple features.

# What is/are the insight(s) found from the chart?
#  Most variable pairs show weak linear relationships.
#  The diagonal plots reveal the distribution of each numerical variable.
#  A few outliers can be observed, particularly in trip duration and member age.
#  Station latitude and longitude values are concentrated within a limited geographic range, reflecting the service area of the bike-sharing system.

# Will the gained insights help create a positive business impact?
#  Yes. Pair plots help identify relationships between important numerical features, supporting feature selection, anomaly detection, and predictive modeling. These insights enable the company to better understand customer behavior and improve operational planning.

# Are there any insights that lead to negative growth? Justify with a specific reason.
#  Yes. The presence of outliers and weak relationships between certain variables suggests that some features may contribute little to predictive analysis. Ignoring these issues may reduce the accuracy of forecasting models and lead to less effective business decisions.




## **5. Solution to Business Objective**
## What do you suggest the client to achieve Business Objective ?
# Explain Briefly.

# Based on the exploratory data analysis of the Ford GoBike dataset, the following recommendations are suggested to help the company achieve its business objectives:
"""
1. **Increase Bike Availability During Peak Hours**
   - Most trips occur during morning and evening commuting hours.
   - Deploy more bikes and ensure docking stations are well-stocked during these peak periods to reduce shortages and improve customer satisfaction.

2. **Improve Weekend Ridership**
   - Weekend usage is lower than weekday usage.
   - Introduce weekend discounts, family ride packages, and promotional campaigns to encourage more recreational rides.

3. **Expand the Subscriber Base**
   - Subscribers account for the majority of bike trips.
   - Offer special discounts, referral programs, and free trial memberships to convert occasional customers into long-term subscribers.

4. **Optimize Station Management**
   - Analyze high-demand stations and redistribute bikes accordingly.
   - Schedule regular maintenance and ensure bike availability at the busiest locations to improve operational efficiency.

5. **Target Underrepresented Customer Groups**
   - Male riders make up the largest share of users.
   - Launch targeted marketing campaigns, safety initiatives, and community events to encourage greater participation from female and other underrepresented rider groups.

6. **Use Seasonal Demand for Planning**
   - Monthly and weekday trends indicate fluctuations in bike usage.
   - Plan maintenance during low-demand periods and increase bike availability during months with higher demand.

7. **Monitor Long-Duration Trips**
   - A small number of trips have exceptionally long durations.
   - Investigate these rides to identify potential misuse, delayed returns, or operational issues, helping improve fleet availability.

8. **Leverage Data for Future Analytics**
   - Continue collecting and analyzing trip data to forecast demand, optimize bike distribution, and support data-driven business decisions using predictive analytics.
"""

# Conclusion
#  The analysis shows that the Ford GoBike system is primarily used for daily commuting, with Subscribers contributing the majority of trips. By optimizing fleet distribution, increasing customer engagement, expanding the subscriber base, and using data-driven operational strategies, the company can improve customer satisfaction, increase ridership, and enhance overall business performance.
