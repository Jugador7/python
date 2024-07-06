Importing Required Libraries
We recommend you import all required libraries:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

The functions below will download the dataset into your browser:

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

file_path= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"

await download(file_path, "laptops.csv")
file_name="laptops.csv"

df = pd.read_csv(file_name, header=0)

#filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
#df = pd.read_csv(filepath, header=None)

Verify loading by displaying the dataframe summary using `dataframe.info()`

print(df.info())

df.head()

Note that we can update the `Screen_Size_cm` column such that all values are rounded to nearest 2 decimal places by using `numpy.round()`

df[['Screen_Size_cm']] = np.round(df[['Screen_Size_cm']],2)
df.head()

