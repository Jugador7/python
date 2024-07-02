import pandas as pd
import numpy as np
#The functions below will download the dataset into your browser:

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"

await download(file_path, "laptops.csv")
file_name="laptops.csv"

df = pd.read_csv(file_name)

df = pd.read_csv(file_name, header=None)
print(df.head())

headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
df.columns = headers
print(df.head(10))

df.replace('?',np.nan, inplace = True)

df.dtypes

df.describe(include="all")

print(df.info())
