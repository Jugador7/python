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


#Identify the HTML tags that contain the data you want to extract.
#Use BeautifulSoup methods to extract the data from the HTML tags.
#Print the extracted data

