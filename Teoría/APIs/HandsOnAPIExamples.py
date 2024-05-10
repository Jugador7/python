get_cell()
get_city()
get_dob()
get_email()
get_first_name()
get_full_name()
get_gender()
get_id()
get_id_number()
get_id_type()
get_info()
get_last_name()
get_login_md5()
get_login_salt()
get_login_sha1()
get_login_sha256()
get_nat()
get_password()
get_phone()
get_picture()
get_postcode()
get_registered()
get_state()
get_street()
get_username()
get_zipcode()

!pip install randomuser

from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(10)

some_list

name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users()

df1 = pd.DataFrame(get_users())  

#Now we have a *pandas* dataframe that can be used for any testing purposes that the tester might have.

##############################################################################

#Fruityvice:

import requests
import json

data = requests.get("https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

pd.DataFrame(results)


#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.

df2 = pd.json_normalize(results)

df2

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])



