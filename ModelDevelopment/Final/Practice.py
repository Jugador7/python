Objectives
In this project, you will:

Load the data as a pandas dataframe
Clean the data, taking care of the blank entries
Run exploratory data analysis (EDA) and identify the attributes that most affect the charges
Develop single variable and multi variable Linear Regression models for predicting the charges
Use Ridge regression to refine the performance of Linear regression models.
Setup
For this lab, we will be using the following libraries:

skillsnetwork to download the data
pandas for managing the data.
numpy for mathematical operations.
sklearn for machine learning and machine-learning-pipeline related functions.
seaborn for visualizing the data.
matplotlib for additional plotting tools.
The following required libraries are not pre-installed in the Skills Network Labs environment. You will need to run the following cell to install them:

import piplite
await piplite.install('seaborn')
Importing Required Libraries
We recommend you import all required libraries in one place (here):

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split

Download the dataset to this lab environment
Run the cell below to load the dataset to this lab environment.

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv'
await download(filepath, "insurance.csv")
file_name="insurance.csv"
df = pd.read_csv(file_name)
Note: This version of the lab is working on JupyterLite, which requires the dataset to be downloaded to the interface.While working on the downloaded version of this notebook on their local machines(Jupyter Anaconda), the learners can simply skip the steps above, and simply use the URL directly in the pandas.read_csv() function. You can uncomment and run the statements in the cell below.

#filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv'
#df = pd.read_csv(filepath, header=None)
  
Task 1 : Import the dataset¶
