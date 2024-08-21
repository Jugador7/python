Practice Assignment - Part 1: Analyzing wildfire activities in Australia

Objectives
After completing this lab you will be able to:

Use visualization libraries such as Matplotlib, Pandas, Seaborn and Folium to create informative plots and charts
Setup
For this lab, we will be using the following libraries:

pandas for managing the data.
numpy for mathematical operations.
seaborn for visualizing the data.
matplotlib for additional plotting tools.

Installing Required Libraries
The following required libraries are pre-installed in the Skills Network Labs environment. However, if you run this notebook commands in a different Jupyter environment (e.g. Watson Studio or Ananconda), you will need to install these libraries by removing the # sign before %pip in the code cell below.

# All Libraries required for this lab are listed below. The libraries pre-installed on Skills Network Labs are commented.
#%pip install -qy pandas==1.3.4 numpy==1.21.4 seaborn==0.9.0 matplotlib==3.5.0 folium
# Note: If your environment doesn't support "%pip install", use "!mamba install"
%pip install seaborn
%pip install folium
Importing Required Libraries
We recommend you import all required libraries in one place (here):

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
%matplotlib inline

Dataset
Historical Wildfires

This wildfire dataset contains data on fire activities in Australia starting from 2005. Additional information can be found here.

Variables

Region: the 7 regions
Date: in UTC and provide the data for 24 hours ahead
Estimated_fire_area: daily sum of estimated fire area for presumed vegetation fires with a confidence > 75% for a each region in km2
Mean_estimated_fire_brightness: daily mean (by flagged fire pixels(=count)) of estimated fire brightness for presumed vegetation fires with a confidence level > 75% in Kelvin
Mean_estimated_fire_radiative_power: daily mean of estimated radiative power for presumed vegetation fires with a confidence level > 75% for a given region in megawatts
Mean_confidence: daily mean of confidence for presumed vegetation fires with a confidence level > 75%
Std_confidence: standard deviation of estimated fire radiative power in megawatts
Var_confidence: Variance of estimated fire radiative power in megawatts
Count: daily numbers of pixels for presumed vegetation fires with a confidence level of larger than 75% for a given region
Replaced: Indicates with an Y whether the data has been replaced with standard quality data when they are available (usually with a 2-3 month lag). Replaced data has a slightly higher quality in t
                                                                                                        
Importing Data
from js import fetch
import io

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv"
resp = await fetch(URL)
text = io.BytesIO((await resp.arrayBuffer()).to_py())
df = pd.read_csv(text)
print('Data read into a pandas dataframe!')

Data read into a pandas dataframe!
Let's look at some samples rows from the dataset we loaded:

Let's verify the column names and the data type of each variable

df.columns

#data type
df.dtypes

Notice the type of 'Date' is object, lets convert it to 'datatime' type and also lets extract 'Year' and 'Month' from date and include in the dataframe as separate columns

import datetime as dt

df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Month'] = pd.to_datetime(df['Date']).dt.month

Verify the columns again

#verify the columns again
df.dtypes


Practice Tasks
TASK 1.1: Let's try to understand the change in average estimated fire area over time
(use pandas to plot)

    plt.figure(figsize=(12, 6))
    # Grouping the data by 'Year' and calculating the mean of 'Estimated_fire_area'
    df_new = df.groupby('Year')['Estimated_fire_area'].mean()
    # Plotting the data
    df_new.plot(x=df_new.index, y=df_new.values)
    plt.xlabel('Year')
    plt.ylabel('Average Estimated Fire Area (km²)')
    plt.title('Estimated Fire Area over Time')
    plt.show()

TASK 1.2: You can notice the peak in the plot between 2010 to 2013. Lets narrow down our finding, by plotting the estimated fire area for year grouped together with month.

    # Grouping the data by both 'Year' and 'Month', and calculating the mean of 'Estimated_fire_area'
    df_new = df.groupby(['Year','Month'])['Estimated_fire_area'].mean()
    # Plotting the data
    df_new.plot(x=df_new.index, y=df_new.values)
    plt.xlabel('Year, Month')
    plt.ylabel('Average Estimated Fire Area (km²)')
    plt.title('Estimated Fire Area over Time')
    plt.show()

This plot represents that the estimated fire area was on its peak after 2011, April and before 2012. You can verify on google/news, this was the time of maximum wildfire hit in Austrailia

TASK 1.3: Let's have an insight on the distribution of mean estimated fire brightness across the regions
use the functionality of seaborn to develop a barplot
before starting with the plot, why not know the regions mentioned in the dataset?.
Make use of unique() to identify the regions in the dataset (apply it on series only

df['Region'].unique()

# Creating a bar plot using seaborn to visualize the distribution of mean estimated fire brightness across regions
plt.figure(figsize=(10, 6))
# Using seaborn's barplot function to create the plot
sns.barplot(data=df, x='Region', y='Mean_estimated_fire_brightness')
plt.xlabel('Region')
plt.ylabel('Mean Estimated Fire Brightness (Kelvin)')
plt.title('Distribution of Mean Estimated Fire Brightness across Regions')
plt.show()

TASK 1.4: Let's find the portion of count of pixels for presumed vegetation fires vary across regions
we will develop a pie chart for this

# Creating a pie chart to visualize the portion of count of pixels for presumed vegetation fires across regions
plt.figure(figsize=(10, 6))
# Grouping the data by region and summing the counts
region_counts = df.groupby('Region')['Count'].sum()
# Creating the pie chart using plt.pie function
# Labels are set to the region names, and autopct is used to display percentage
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%')
plt.title('Percentage of Pixels for Presumed Vegetation Fires by Region')
plt.axis('equal')
plt.show()

TASK 1.5: See the percentage on the pie is not looking so good as it is overlaped for Region SA, TA, VI

#TODO
temp = df.set_index("Region")["Count"]

temp = temp.groupby("Region").sum()

temp.plot(kind='pie',
          figsize=(10, 6),
          autopct='%1.1f%%', 
          startangle=90,    
          shadow=True,       
          labels=None,
          pctdistance=1.12
         )
# scale the title up by 12% to match pctdistance
plt.title('Count of pixels for presumed vegetation fires across regions', y=1.12, fontsize = 15) 

plt.axis('equal') 

# add legend
region_counts = temp
plt.legend(labels=[(i,round(k/region_counts.sum()*100,2)) for i,k in zip(region_counts.index, region_counts)], loc='upper left', fontsize=7)

plt.show()

TASK 1.6: Let's try to develop a histogram of the mean estimated fire brightness
Using Matplotlib to create the histogram

# Creating a histogram to visualize the distribution of mean estimated fire brightness
plt.figure(figsize=(10, 6))
# Using plt.hist to create the histogram
# Setting the number of bins to 20 for better visualization
plt.hist(x=df['Mean_estimated_fire_brightness'], bins=20)
plt.xlabel('Mean Estimated Fire Brightness (Kelvin)')
plt.ylabel('Count')
plt.title('Histogram of Mean Estimated Fire Brightness')
plt.show()

TASK 1.7: What if we need to understand the distribution of estimated fire brightness across regions? Lets use the functionality of seaborn and pass region as hue
# Creating a histogram to visualize the distribution of mean estimated fire brightness across regions using Seaborn
# Using sns.histplot to create the histogram
# Specifying the DataFrame (data=df) and the column for the x-axis (x='Mean_estimated_fire_brightness')
# Adding hue='Region' to differentiate the distribution across regions
sns.histplot(data=df, x='Mean_estimated_fire_brightness', hue='Region')
plt.show()


looks better!, now include the parameter multiple='stack' in the histplot() and see the difference. Include labels and titles as well
# Creating a stacked histogram to visualize the distribution of mean estimated fire brightness across regions using Seaborn
# Using sns.histplot to create the stacked histogram
# Specifying the DataFrame (data=df) and the column for the x-axis (x='Mean_estimated_fire_brightness')
# Adding hue='Region' to differentiate the distribution across regions
# Setting multiple='stack' to stack the histograms for different regions
sns.histplot(data=df, x='Mean_estimated_fire_brightness', hue='Region', multiple='stack')
plt.show()

TASK 1.8: Lets try to find if there is any correlation between mean estimated fire radiative power and mean confidence level?

    # Creating a scatter plot to visualize the relationship between mean estimated fire radiative power and mean  confidence using Seaborn
    plt.figure(figsize=(8, 6))
    # Using sns.scatterplot to create the scatter plot
    # Specifying the DataFrame (data=df) and the columns for the x-axis (x='Mean_confidence') and y-axis            (y='Mean_estimated_fire_radiative_power')
    sns.scatterplot(data=df, x='Mean_confidence', y='Mean_estimated_fire_radiative_power')
    plt.xlabel('Mean Estimated Fire Radiative Power (MW)')
    plt.ylabel('Mean Confidence')
    plt.title('Mean Estimated Fire Radiative Power vs. Mean Confidence')
    plt.show()

TASK 1.9: Let's mark these seven regions on the Map of Australia using Folium¶

we have created a dataframe for you containing the regions, their latitudes and longitudes.
For australia use [-25, 135] as location to create the map

region_data = {'region':['NSW','QL','SA','TA','VI','WA','NT'], 'Lat':[-31.8759835,-22.1646782,-30.5343665,-42.035067,-36.5986096,-25.2303005,-19.491411], 
               'Lon':[147.2869493,144.5844903,135.6301212,146.6366887,144.6780052,121.0187246,132.550964]}
reg=pd.DataFrame(region_data)
reg

# instantiate a feature group 
aus_reg = folium.map.FeatureGroup()

# Create a Folium map centered on Australia
Aus_map = folium.Map(location=[-25, 135], zoom_start=4)

# loop through the region and add to feature group
for lat, lng, lab in zip(reg.Lat, reg.Lon, reg.region):
    aus_reg.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            popup=lab,
            radius=5, # define how big you want the circle markers to be
            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
Aus_map.add_child(aus_reg)
