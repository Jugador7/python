!pip install pandas==1.3.3
!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y 
!pip install lxml==4.6.4
!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Steps for extracting the data¶
#Send an HTTP request to the web page using the requests library.

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text
print(data)

#Parse the HTML content of the web page using BeautifulSoup.
soup = BeautifulSoup(data, 'html5lib')

#Identify the HTML tags that contain the data you want to extract.
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

#Use BeautifulSoup methods to extract the data from the HTML tags.

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

#Print the extracted data
netflix_data.head()



# Extracting data using `pandas` library

read_html_pandas_data = pd.read_html(url)
#Or you can convert the BeautifulSoup object to a string.
read_html_pandas_data = pd.read_html(str(soup))

#Because there is only one table on the page, just take the first table in the returned list.
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()



