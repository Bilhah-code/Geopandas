#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import geopandas as gpd
from shapely.geometry import point
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import os


# In[3]:


kenya = gpd.read_file(r"C:\Users\B.Murage\Desktop\Trials\Data\kenya.shp")

kenya.head()


# In[4]:


kenya.plot()


# In[5]:


# Show the plot
plt.show()


# In[6]:


ax= kenya.plot(figsize=(5, 5))
ax.axis('off')


# In[7]:


plt.show()


# In[8]:


print(kenya['COUNTIES'].unique())  # Check all unique county names


# In[9]:


# Filter the GeoDataFrame to get Elgeyo/Marakwet
Marakwet = kenya.loc[kenya['COUNTIES'] == 'Elgeyo/Marakwet'].copy().reset_index(drop=True)
Marakwet.plot(figsize=(5, 5))
plt.show()


# In[10]:


Marakwet.to_file("C:/Users/B.Murage/Desktop/Trials/Data/ma.shp")


# In[11]:


kenya.plot(column='AREA_SQKM')


# In[12]:


#Chloropleth map
plt.show()


# In[13]:


Region = ['Laikipia', 'Nyeri', 'Meru', 'Kirinyaga', 'Nyandarua', "Murang'a", 'Embu', 'Tharaka-Nithi','Kiambu']
kenya.loc[kenya['COUNTIES'].isin(Region)].plot()


# In[14]:


plt.show()


# In[15]:


# Provide the full path with the .csv extension
csv_file = r"C:\Users\B.Murage\Downloads\2019-population_census-report-per-county.csv"

# Load the CSV into a DataFrame
df = pd.read_csv(csv_file)

# Display the first few rows
print(df.head())


# In[16]:


# Check correct county column in shapefile
county_column = "COUNTIES"  # Update if different

# Filter selected counties
kenya_selected = kenya[kenya[county_column].isin(Region)]

# Plot selected counties
kenya_selected.plot(figsize=(12, 12))
plt.title("Selected Counties")
plt.show()


# In[17]:


# Load CSV file with population density data
csv_file = r"C:\Users\B.Murage\Downloads\2019-population_census-report-per-county.csv"
df = pd.read_csv(csv_file)
# Check available columns in CSV
print("CSV Columns:", df.columns)


# In[18]:


# Select relevant columns
df = df[['County', 'Population Density']]

# Merge population density data with shapefile
kenya_selected = kenya_selected.merge(df, left_on=county_column, right_on='County', how='left')


# In[19]:


# Plot the choropleth map
fig, ax = plt.subplots(figsize=(10, 8))
kenya_selected.plot(column='Population Density', cmap='OrRd', linewidth=0.8, edgecolor='black',
                    legend=True,ax=ax)

# Add title
ax.set_title("Population Density of Selected Counties (2019 Census)", fontsize=14)
ax.set_axis_off()


# In[20]:


# Show the map
plt.show()


# In[21]:


# Dissolve the counties into one by combining the geometries
kenya_dissolved = kenya_selected.dissolve(by='COUNTRY')
# Plot the dissolved map without boundaries
fig, ax = plt.subplots(figsize=(10, 8))
kenya_dissolved.plot(ax=ax, color='lightblue', edgecolor='black')  # 'edgecolor' set to 'none' removes boundaries

# Add title and show the plot
ax.set_title("Merged Counties", fontsize=14)
plt.show()


# In[25]:


# Provide the full path to the shapefile
shapefile_path = "C:/Users/B.Murage/Desktop/Rivers/Rivers.shp"


# Read the shapefile into a GeoDataFrame
rivers = gpd.read_file(shapefile_path)

# Display the first few rows of the GeoDataFrame
print(rivers.head())

# Plot the rivers
rivers.plot()
plt.title("Rivers in Kenya")
plt.show()


# In[35]:


# Reproject rivers to match kenya_dissolved CRS
if rivers.crs != kenya_dissolved.crs:
    rivers = rivers.to_crs(kenya_dissolved.crs)
# Perform the clip
clipped_rivers = gpd.clip(rivers, kenya_dissolved)
# Display the clipped result
clipped_rivers.plot(figsize=(8,8 ))
plt.show()


# In[ ]:




