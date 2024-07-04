#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2

import pandas as pd
import matplotlib.pylab as plt

The functions below will download the dataset into your browser:

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

file_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

await download(file_path, "usedcars.csv")
file_name="usedcars.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(file_name, names = headers)

#filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
#df = pd.read_csv(filepath, header=headers)    # Utilize the same header list defined above

# To see what the data set looks like, we'll use the head() method.
df.head()

# Identify and handle missing values


### Identify missing values
#<h4>Convert "?" to NaN</h4>
#In the car data set, missing data comes with the question mark "?".
#We replace "?" with NaN (Not a Number), Python's default missing value marker for reasons of computational speed and convenience. Use the function: 
# <pre>.replace(A, B, inplace = True) </pre>
#to replace A by B.

import numpy as np

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

#<h4>Evaluating for Missing Data</h4>

missing_data = df.isnull()
missing_data.head(5)

#<h4>Count missing values in each column</h4>
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

#Deal with missing data
#How should you deal with missing data?

#Drop data
#a. Drop the whole row
#b. Drop the whole column
#Replace data
#a. Replace it by mean
#b. Replace it by frequency
#c. Replace it based on other functions

#Replace by mean:

#"normalized-losses": 41 missing data, replace them with mean
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
#"stroke": 4 missing data, replace them with mean
#Calculate the mean vaule for "stroke" column
avg_stroke = df["stroke"].astype("float").mean(axis = 0)
print("Average of stroke:", avg_stroke) # replace NaN by mean value in "stroke" column
df["stroke"].replace(np.nan, avg_stroke, inplace = True)
#"bore": 4 missing data, replace them with mean
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)
#"horsepower": 2 missing data, replace them with mean
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
#"peak-rpm": 2 missing data, replace them with mean
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

#Replace by frequency:

#"num-of-doors": 2 missing data, replace them with "four".
#Reason: 84% sedans are four doors. Since four doors is most frequent, it is most likely to occur

#Drop the whole row:

#"price": 4 missing data, simply delete the whole row
#Reason: You want to predict price. You cannot use any data entry without price data for prediction; therefore any row now without price data is not useful to you.

