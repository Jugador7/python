import pandas as pd

import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

#To read a CSV (Comma-Separated Values) file in Python using the Pandas library, you can use the pd.read_csv() function. Here's the syntax to read a CSV file:

import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

#Importing series in pandas
import pandas as pd
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

#Accesing data
print(s[2])     # Access the element with label 2 (value 30)

print(s.iloc[3]) # Access the element at position 3 (value 40)

print(s[1:4])   # Access a range of elements by label

#Series Attributes and Methods
#values: Returns the Series data as a NumPy array.
#index: Returns the index (labels) of the Series.
#shape: Returns a tuple representing the dimensions of the Series.
#size: Returns the number of elements in the Series.
#mean(), sum(), min(), max(): Calculate summary statistics of the data.
#unique(), nunique(): Get unique values or the number of unique values.
#sort_values(), sort_index(): Sort the Series by values or index labels.
#isnull(), notnull(): Check for missing (NaN) or non-missing values.
#apply(): Apply a custom function to each element of the Series.

#Creating a DataFrame from a Dictionary
import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

#Columna Selection

print(df['Name'])  # Access the 'Name' column
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label

print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows


unique_dates = df['Age'].unique() #Finding unique elements

#You can filter data in a DataFrame based on conditions using inequality operators.
#For instance, you can filter albums released after a certain year.
high_above_102 = df[df['Age'] > 25]

#saving dataframe to a file
df.to_csv('trading_data.csv', index=False)

#shape: Returns the dimensions (number of rows and columns) of the DataFrame.
#info(): Provides a summary of the DataFrame, including data types and non-null counts.
#describe(): Generates summary statistics for numerical columns.
#head(), tail(): Displays the first or last n rows of the DataFrame.
#mean(), sum(), min(), max(): Calculate summary statistics for columns.
#sort_values(): Sort the DataFrame by one or more columns.
#groupby(): Group data based on specific columns for aggregation.
#fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
#apply(): Apply a function to each element, row, or column of the DataFrame.

#Define a dictionary 'x'

y = {'Student': ['David','Samuel', 'Terry', 'Evan'], 'Age': [27, 24, 22, 32], 'Country': ['UK', 'Canada', 'China', 'USA'], 
      'Course':['Python', 'Data Structures', 'Machine Learning', 'Web Development'],'Marks': [85, 72, 89, 76]}

#casting the dictionary to a DataFrame
df1 = pd.DataFrame(y)

#display the result df
df1

# Get the Student column as a series Object

x = df1['Student']
x
