Creating maps and visualizing Geospatial data
Estimated time needed: 30 minutes

Objectives
After completing this lab you will be able to:

Create maps and visualize geospatial data with Folium
Introduction
In this lab, we will learn how to create maps for different objectives. To do that, we will part ways with Matplotlib and work with another Python visualization library, namely Folium. What is nice about Folium is that it was developed for the sole purpose of visualizing geospatial data. While other libraries are available to visualize geospatial data, such as plotly, they might have a cap on how many API calls you can make within a defined time frame. Folium, on the other hand, is completely free.

Table of Contents
Exploring Datasets*
Importing Libraries
Introduction to Folium
Map with Markers
Choropleth Maps
Exploring Datasets
Toolkits: This lab heavily relies on pandas and Numpy for data wrangling, analysis, and visualization. The primary plotting library we will explore in this lab is Folium.

Datasets:

San Francisco Police Department Incidents for the year 2016 - Police Department Incidents from San Francisco public data portal. Incidents derived from San Francisco Police Department (SFPD) Crime Incident Reporting system. Updated daily, showing data for the entire year of 2016. Address and location has been anonymized by moving to mid-block or to an intersection. Note: this dataset no longer exists on the original website since systems updates in the department. The link included will take you to the page explaining the change of system since this exercise was created.

Immigration to Canada from 1980 to 2013 - International migration flows to and from selected countries - The 2015 revision from United Nation's website. The dataset contains annual data on the flows of international migrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals. For this lesson, we will focus on the Canadian Immigration data and use the already cleaned dataset.

You can refer to the lab on data pre-processing wherein this dataset is cleaned for a quick refresh your Pandas skill Data pre-processing with Pandas

Importing Libraries 
Import Primary Modules:

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
Let's install Folium
Folium is not available by default. So, we first need to install it before we are able to import it.

#!pip3 install folium==0.5.0
import folium
​
print('Folium installed and imported!')
Folium installed and imported!
Introduction to Folium 
Folium is a powerful Python library that helps you create several types of Leaflet maps. The fact that the Folium results are interactive makes this library very useful for dashboard building.

From the official Folium documentation page:

Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium.

Folium makes it easy to visualize data that's been manipulated in Python on an interactive Leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing Vincent/Vega visualizations as markers on the map.

The library has a number of built-in tilesets from OpenStreetMap, Mapbox, Cartodb and supports custom tilesets with Mapbox or Cloudmade API keys. Folium supports both GeoJSON and TopoJSON overlays, as well as the binding of data to those overlays to create choropleth maps with color-brewer color schemes.

Generating the world map is straightforward in Folium. You simply create a Folium Map object, and then you display it. What is attractive about Folium maps is that they are interactive, so you can zoom into any region of interest despite the initial zoom level.

# define the world map
world_map = folium.Map()

# display world map
world_map
# define the world map
world_map = folium.Map()
​
# display world map
world_map

