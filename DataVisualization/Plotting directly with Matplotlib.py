#Import Primary Modules:
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

# use the inline backend to generate the plots within the browser
%matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt

# check for latest version of Matplotlib
print('Matplotlib version: ', mpl.__version__) # >= 2.0.0

Fetching Data
Dataset: Immigration to Canada from 1980 to 2013 - International migration flows to and from selected countries - The 2015 revision from United Nation's website.
In this lab, we will focus on the Canadian Immigration data and use the already cleaned dataset and can be fetched from here.

You can refer to the lab on data pre-processing wherein this dataset is cleaned for a quick refresh your Panads skill Data pre-processing with Pandas

from js import fetch
import io

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv"
resp = await fetch(URL)
text = io.BytesIO((await resp.arrayBuffer()).to_py())
df_can = pd.read_csv(text)
print('Data read into a pandas dataframe!')

Let's find out how many entries there are in our dataset.

# print the dimensions of the dataframe
print(df_can.shape)

Set the country name as index - useful for quickly looking up countries using .loc method.

df_can.set_index('Country', inplace=True)

# Let's view the first five elements and see how the dataframe was changed
df_can.head()

Notice now the country names now serve as indices.

print('data dimensions:', df_can.shape)
data dimensions: (195, 38)

# finally, let's create a list of years from 1980 - 2013
# this will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))
#years = np.arange(1980,2014)

Line Plot
fig = plt.figure(figsize=(10, 10))

# Add the first subplot (top-left)
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(total_immigrants)
ax1.set_title('Plot 1 - Line Plot')

# Add the second subplot (top-right)
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(total_immigrants.index, total_immigrants)
ax2.set_title('Plot 2 - Scatter plot')

# Add the third subplot (bottom-left)
ax3 = fig.add_subplot(2, 2, 3)
ax3.hist(df_dns)
ax3.set_title('Plot3 - Histogram') 
ax3.set_xlabel('Number of Immigrants')
ax3.set_ylabel('Number of Years')

# Add the fourth subplot (bottom-right)
ax4 = fig.add_subplot(2, 2, 4)
ax4.pie(total_immigrants[0:5], labels=years[0:5], 
       colors = ['gold','blue','lightgreen','coral','cyan'],
       autopct='%1.1f%%')
ax4.set_aspect('equal')  
ax4.set_title('Plot 5 - Pie Chart')

#Adding a Title for the Overall Figure
fig.suptitle('Four Plots in a Figure Example', fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()


# Show the figure
plt.show()

Click here for a sample python solution
    # Create a figure with Four axes - two rows, two columns
    fig = plt.figure(figsize=(10, 10))

    # Add the first subplot (top-left)
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(total_immigrants)
    ax1.set_title('Plot 1 - Line Plot')

    # Add the second subplot (top-right)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(total_immigrants.index, total_immigrants)
    ax2.set_title('Plot 2 - Scatter plot')

    # Add the third subplot (bottom-left)
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.hist(df_dns)
    ax3.set_title('Plot3 - Histogram') 
    ax3.set_xlabel('Number of Immigrants')
    ax3.set_ylabel('Number of Years')

    # Add the fourth subplot (bottom-right)
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.pie(total_immigrants[0:5], labels=years[0:5], 
           colors = ['gold','blue','lightgreen','coral','cyan'],
           autopct='%1.1f%%')
    ax4.set_aspect('equal')  
    ax4.set_title('Plot 5 - Pie Chart')

    #Adding a Title for the Overall Figure
    fig.suptitle('Four Plots in a Figure Example', fontsize=15)

    # Adjust spacing between subplots
    fig.tight_layout()


    # Show the figure
    plt.show()
