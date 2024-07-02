# uncomment the lines below if you need to install specific version of libraries if using this notebook 
# in an environment where these libraries are not installed 
#! mamba install pandas==1.3.3  -y
#! mamba install numpy=1.21.2 -y

# import pandas library
import pandas as pd
import numpy as np

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

file_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

await download(file_path, "auto.csv")
file_name="auto.csv"

df = pd.read_csv(file_name)


#Note: This version of the lab is working on JupyterLite, which requires the dataset to be downloaded to the interface.While working on the downloaded version of this notebook on their local machines(Jupyter Anaconda), the learners can simply skip the steps above, and simply use the URL directly in the pandas.read_csv() function. You can uncomment and run the statements in the cell below.
#filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
#df = pd.read_csv(filepath, header=None)


# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

print("The last 10 rows of the dataframe") 
df.tail(10)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
df.columns

df1=df.replace('?',np.NaN)

df=df1.dropna(subset=["price"], axis=0)
df.head(20)
#Here, axis=0 means that the contents along the entire row will be dropped wherever the entity 'price' is found to be NaN

#Now, you have successfully read the raw data set and added the correct headers into the data frame.

print(df.columns)

df.to_csv("automobile.csv", index=False)

df.dtypes

print(df.dtypes)

df.describe()

# describe all the columns in "df" 
df.describe(include = "all")

# Write your code below and press Shift+Enter to execute 
df[['length','compression-ratio']].describe()

This method prints information about a data frame including the index dtype and columns, non-null values and memory usage.
# look at the info of "df"
df.info

