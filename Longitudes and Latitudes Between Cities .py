#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import pandas package   
import pandas as pd  
import numpy as np 
    
# Define a dictionary containing  data  
data = pd.read_csv(r'C:\Users\aambundo\Desktop\flights.csv') 
    
# Convert the dictionary into DataFrame  
data = df
    
# Observe the result  
df  
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim 
   
# declare an empty list to store 
# latitude and longitude of values  
# of city column 
longitude = [] 
latitude = [] 
   
# function to find the coordinate 
# of a given city  
def findGeocode(city): 
       
    # try and catch is used to overcome 
    # the exception thrown by geolocator 
    # using geocodertimedout   
    try: 
          
        # Specify the user_agent as your 
        # app name it should not be none 
        geolocator = Nominatim(user_agent="your_app_name") 
          
        return geolocator.geocode(city) 
      
    except GeocoderTimedOut: 
        return findGeocode(city)     
  
 # each value from city column 
# will be fetched and sent to 
# function find_geocode    
for i in (df[" From_City "]): 
      
    if findGeocode(i) != None: 
           
        loc = findGeocode(i) 
          
        # coordinates returned from  
        # function is stored into 
        # two separate list 
        latitude.append(loc.latitude) 
        longitude.append(loc.longitude) 
       
    # if coordinate for a city not 
    # found, insert "NaN" indicating  
    # missing value  
    else: 
        latitude.append(np.nan) 
        longitude.append(np.nan)

    # now add this column to dataframe 
df["From_City_Longitude"] = longitude 
df["From_City_Latitude"] = latitude 
  
df 


# In[36]:


get_ipython().system(u' pip install plotly')


# In[40]:


import pandas as pd  
import numpy as np 
#import plotly.plotly as py
import plotly.offline as ol

from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim 


   
# declare an empty list to store 
# latitude and longitude of values  
# of city column 
longitude = [] 
latitude = [] 
   
# function to find the coordinate 
# of a given city  
def findGeocode(city): 
       
    # try and catch is used to overcome 
    # the exception thrown by geolocator 
    # using geocodertimedout   
    try: 
          
        # Specify the user_agent as your 
        # app name it should not be none 
        geolocator = Nominatim(user_agent="your_app_name") 
          
        return geolocator.geocode(city) 
      
    except GeocoderTimedOut: 
        return findGeocode(city)     
  
 # each value from city column 
# will be fetched and sent to 
# function find_geocode    
for i in (df[" To_City "]): 
      
    if findGeocode(i) != None: 
           
        loc = findGeocode(i) 
          
        # coordinates returned from  
        # function is stored into 
        # two separate list 
        latitude.append(loc.latitude) 
        longitude.append(loc.longitude) 
       
    # if coordinate for a city not 
    # found, insert "NaN" indicating  
    # missing value  
    else: 
        latitude.append(np.nan) 
        longitude.append(np.nan)

    # now add this column to dataframe 
df["To_City_Longitude"] = longitude 
df["To_City_Latitude"] = latitude 

#data.drop(["Longitude", "Latitude"], axis = 1, inplace = True) 

# Calculate the distance (great circle distance) between the origin and destination airports
#df["Distance"] = ''
  
#for index, row in df.iterrows():
    #df.loc[df.index==index, "Distance"] = dist(row.From_City_Latitude, row.From_City_Longitude, row.To_City_Latitude, row.To_City_Longitude)/1000
df


# In[ ]:




