import networkx as nx
import osmnx as ox
from shapely.geometry import LineString, mapping
import geopandas as gpd
import ipyleaflet
from ipyleaflet import *
import folium
import requests
from folium import plugins
import pandas as pd
import numpy as np
import openrouteservice as openrouteservice
from openrouteservice import client
import streamlit_folium as st_folium
from streamlit_folium import *

st.set_page_config(
    page_title="Huff Model",
    page_icon= "📍",
)

st.title("Huff Model")

st.sidebar.title("Huff Model")
st.sidebar.write("The Huff Model is a form of spatial interaction model that calculates the probability any given customer will choose to shop at a store based on a combination of the store's attractiveness (commonly square footage or product offerings), the distance to that store, and the combined attractiveness of other competing stores.")

api_key = '5b3ce3597851110001cf62480ac62be4cc3747a890840c0cfde8bd1d'
ors = client.Client(key=api_key)
m = folium.Map(location=(-33.9289920, 18.4173960), zoom_start=10)


@st.cache
def geocode(query):
    parameters = {
        'api_key': '5b3ce3597851110001cf62480ac62be4cc3747a890840c0cfde8bd1d',
        'text' : query
    }

    response = requests.get(
         'https://api.openrouteservice.org/geocode/search',
         params=parameters)
    if response.status_code == 200:
        data = response.json()
        if data['features']:
            x, y = data['features'][0]['geometry']['coordinates']
            return (y, x)

# @st.cache
def buff(res):
    point = [res[0], res[1]]
    params_iso = {'profile': 'driving-car', 'range': [900], 'locations' : [point[::-1]]}
    r = ors.isochrones(**params_iso)
    folium.features.GeoJson(r).add_to(m)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('First Location')
    address = st.text_input('Enter an address.', key = 1)
    if address:
        results = geocode(address)
        if results:
            st.write('Geocoded Coordinates: {}, {}'.format(results[0], results[1]))
            buff(results)
            folium.Marker(
                    results,
                    popup= 'First Location',
                    icon=folium.Icon(color='green', icon='crosshairs', prefix='fa')
                    ).add_to(m)
        else:
            results = (-34.09987, 18.85273)
    else:
        results = (-34.09987, 18.85273)
        buff(results)
        folium.Marker(
                results,
                popup= 'First Location',
                icon=folium.Icon(color='green', icon='crosshairs', prefix='fa')
                ).add_to(m)
with col2:
    st.subheader('Second Location')
    address1 = st.text_input('Enter an address.', key = 2)
    if address1:
        results1 = geocode(address1)
        if results1:
            st.write('Geocoded Coordinates: {}, {}'.format(results1[0], results1[1]))
            buff(results1)
            folium.Marker(
                    results1,
                    popup='Second Location',
                    icon=folium.Icon(color='green', icon='crosshairs', prefix='fa')
                    ).add_to(m)

        else:
            results1 = (-33.93514743516671, 18.676218389656704)
    else:
        results1 = (-33.93514743516671, 18.676218389656704)
        buff(results1)
        folium.Marker(
                results1,
                popup='Second Location',
                icon=folium.Icon(color='green', icon='crosshairs', prefix='fa')
                ).add_to(m)
with col3:
    st.subheader('Third Location')
    address2 = st.text_input('Enter an address.', key = 3)
    if address2:
        results2 = geocode(address2)
        if results2:
            st.write('Geocoded Coordinates: {}, {}'.format(results2[0], results2[1]))
            buff(results2)
            folium.Marker(
                    results2,
                    popup='Third Location',
                    icon=folium.Icon(color='green', icon='crosshairs', prefix='fa')
                    ).add_to(m)

        else:
            results2 = (-33.90905058860111, 18.564177161133983)
    else:
        results2 = (-33.90905058860111, 18.564177161133983)
        buff(results2)
        folium.Marker(
                results2,
                popup='Third Location',
                icon=folium.Icon(color='green', icon='crosshairs', prefix='fa')
                ).add_to(m)
wards = gpd.read_file('/home/explore-student/t27-s3bucket/Data/Wards.zip')
#The population data is in csv file and contains data on population and income
population = pd.read_csv('/home/explore-student/t27-s3bucket/Data/Popdata.csv')
type_dict = {'WARD_NAME': 'int64'}
type_dict1 = {'WARD_NAME': 'int64',
             'Population_Density (People/Sq Km)': 'float64'}
wards = wards.astype(type_dict)
population = population.astype(type_dict1)
new_gpd = pd.merge(population, wards, on = 'WARD_NAME', how = 'right')
new_gpd = new_gpd[['OBJECTID', 'WARD_NAME', 'Total_Poplation', 'Households', 'Population_Density (People/Sq Km)', 'Average_Annual_Household_Income (Rands)', 'Average_annual_retail_spend (Rands)', 'geometry']]
new_gpd = gpd.GeoDataFrame(new_gpd)
#create a copy of the dataframe
Cen_gpd = new_gpd.copy()
#ensure the copy is a geopandas dataframe
Cen_gpd = gpd.GeoDataFrame(Cen_gpd)
#extract the geometries
cen = Cen_gpd['geometry']
#change the crs of the geometries to ensure accurate calculation of centroids, calculate the cntroids for each ward
centroids = cen.to_crs('epsg:3395').centroid
#convert the centroids back to a format that functions with geopandas
centroids = centroids.to_crs('epsg:4326')
#replace the existing geometries column with the centroid points
Cen_gpd['geometry'] = centroids
Cen_gpd = Cen_gpd[['OBJECTID', 'WARD_NAME', 'Total_Poplation', 'Households', 'Population_Density (People/Sq Km)', 'Average_Annual_Household_Income (Rands)', 'Average_annual_retail_spend (Rands)', 'geometry']]

#create an empty list to store the centroid cordinates
cor_list = []
#loop through the centroids to capture the longitude and latitude and append to the empty list
for i in range(0, len(Cen_gpd)):
  lat_i = Cen_gpd['geometry'][i].y
  lon_i = Cen_gpd['geometry'][i].x
  list_corr = [lon_i, lat_i]
  cor_list.append(list_corr)
#add the cordinates to the centroids dataframe
Cen_gpd['Cor'] = cor_list
w_names = Cen_gpd['WARD_NAME']

lct1 = [results]
lct2 = [results1]
lct3 = [results2]
location1 = list(reversed(lct1[-1]))
location2 = list(reversed(lct2[-1]))
location3 = list(reversed(lct3[-1]))
loca1 = [location1]
loca2 = [location2]
loca3 = [location3]

def huff():
    # Provide your personal API key for use at a later stage in the app
    #Instruct openroute service to use the api key provided
    api_key = '5b3ce3597851110001cf62480ac62be4cc3747a890840c0cfde8bd1d'
    ors = client.Client(key=api_key)
    apartments = {'first': {'location': location1},
                  'second': {'location': location2},
                  'third': {'location': location3}
                  }

    # Request of isochrones with 15 minute walking.
    params_iso = {'profile': 'foot-walking',
                  'range': [900],
                  'attributes': ['total_pop']  # Get population count for isochrones
                  }

    for name, apt in apartments.items():
        params_iso['locations'] = [apt['location']]  # Add apartment coords to request parameters
        apt['iso'] = ors.isochrones(**params_iso)
    #Create empty lists to save the location and the values of the parameter search within the isochrones
    names = []
    values = []
    # Common request parameters
    params_poi = {'request': 'pois',
                  'sortby': 'distance'}

    # POI categories according to
    # https://giscience.github.io/openrouteservice/documentation/Places.html
    categories_poi = {'Taxi stops': [607],
                      'Parking Available': [601],
                      'Competitors': [518]}
    #Save the  the store
    cats = list(categories_poi.keys())

    for name, apt in apartments.items():
        apt['categories'] = dict()  # Store in pois dict for easier retrieval
        params_poi['geojson'] = apt['iso']['features'][0]['geometry']
        #print("\n{} location".format(name))
        names.append("{} location".format(name))#add the names of our location to the names list

        for typ, category in categories_poi.items():
            params_poi['filter_category_ids'] = category
            apt['categories'][typ] = dict()
            apt['categories'][typ]['geojson'] = ors.places(**params_poi)['features']  # Actual POI request
            #print(f"\t{typ}: {len(apt['categories'][typ]['geojson'])}")
            values.append(len(apt['categories'][typ]['geojson']))#Add the values to the list
    def getrows(l):
      n = len(cats)
      return [l[i:i + n] for i in range(0, len(l), n)]
    values = getrows(values)
    locations_df = pd.DataFrame(values, columns = cats, index = names)
    def negative(df):
      lis = df['Competitors']
      lis = lis * -1
      df['Competitors'] = lis
      lis1 = df.sum(axis='columns').values.tolist()
      xmin = min(lis1)
      xmax=max(lis1)
      for i, x in enumerate(lis1):
        lis1[i] = (x-xmin) / (xmax-xmin)
      lis1 = [x + 1 for x in lis1]
      df['Attractiveness']  = lis1
      return df

    scaled = negative(locations_df)
    cordinates1 = list(loca1) + cor_list
    cordinates2 = list(loca2) + cor_list
    cordinates3 = list(loca3) + cor_list
    dest = [0]
    ors = client.Client(key=api_key)
    matrix1 = ors.distance_matrix(locations = cordinates1, destinations = dest, metrics = ['duration', 'distance'], units = 'km')
    matrix2 = ors.distance_matrix(locations = cordinates2, destinations = dest, metrics = ['duration', 'distance'], units = 'km')
    matrix3 = ors.distance_matrix(locations = cordinates3, destinations = dest, metrics = ['duration', 'distance'], units = 'km')
    def flatten(l):
      list_l = [item for sublist in l for item in sublist]
      list_l = list_l[1:]
      return list_l
    loc1_dist = flatten(matrix1['distances'])
    loc2_dist = flatten(matrix2['distances'])
    loc3_dist = flatten(matrix3['distances'])
    Dist_dict = {'WARD_NAME' : w_names,
                 'first location': loc1_dist,
                 'second location': loc2_dist,
                 'third location': loc3_dist}
    distances = pd.DataFrame(Dist_dict)
    distances = distances.set_index('WARD_NAME')
    keys = [(x, y) for x in w_names for y in names]
    neum = {}
    for key in keys:
      neum[key]= scaled.loc[key[1], ['Attractiveness']][0]/distances.loc[key[0],key[1]]**2
    Pijs={}
    for key in keys:
        Pijs[key]= neum[key]/sum([v for k,v in neum.items() if k[0]== key[0]])
    pop_gpd = new_gpd.copy()
    pop_gpd  = pop_gpd.set_index('WARD_NAME')
    ### expected_per_key
    exp_key={}

    for key in keys:
        exp_key[key]= Pijs[key]* pop_gpd.loc[key[0],'Average_annual_retail_spend (Rands)']
    exp_store= {}
    for store in names:
        exp_store[store]= sum([v for k,v in exp_key.items() if k[1]==store])
    o2 = new_gpd['geometry'].to_list()
    exp_locations = {'WARD_NAME' : w_names}
    for store in names:
        exp_locations[store]= [v for k,v in Pijs.items() if k[1]==store]
    # for store in names:
    #     pop_gpd[store]= [v for k,v in exp_key.items() if k[1]==store]
    indices1 = exp_locations.keys()
    global expected
    expected = pd.DataFrame(exp_locations)
    global bins
    bins = list(expected['first location'].quantile([0, 0.25, 0.5, 0.75, 1]))
    global bins1
    bins1 = list(expected['second location'].quantile([0, 0.25, 0.5, 0.75, 1]))
    global bins2
    bins2 = list(expected['third location'].quantile([0, 0.25, 0.5, 0.75, 1]))
    #expected  = expected.set_index('WARD_NAME')
    expected['geometry'] = o2
    expected = gpd.GeoDataFrame(expected)
    expected.crs = "EPSG:4326"
    indices = exp_store.keys()
    stores_df = pd.Series(exp_store).to_frame('Expected Annual Sales')
    return stores_df
stores_df = huff()
bins = list(expected['first location'].quantile([0, 0.25, 0.5, 0.75, 1]))
bins1 = list(expected['second location'].quantile([0, 0.25, 0.5, 0.75, 1]))
bins2 = list(expected['third location'].quantile([0, 0.25, 0.5, 0.75, 1]))

map2 = folium.Map(location=([-33.9289920, 18.4173960]), zoom_start=10)

tab1, tab2 = st.tabs(["Buffers", "Huff Model"])
with tab1:
   folium_static(m, width=800)
   st.dataframe(stores_df)

with tab2:
   option = st.selectbox('Select location to display', ('first location', 'second location', 'third location'))
   if option == 'first location':
       folium.Choropleth(geo_data=expected, data=expected, columns=['WARD_NAME',"first location"],
                         key_on = 'feature.properties.WARD_NAME',
                         Highlight= True,
                         fill_color='YlGnBu',
                         fill_opacity=0.7,
                         line_opacity=.1,
                         legend_name="first location",
                         bins = bins,
                         name = "first location"
       ).add_to(map2)
       folium_static(map2, width=800)
       st.dataframe(stores_df)
   if option == 'second location':
       folium.Choropleth(geo_data=expected, data=expected, columns=['WARD_NAME',"second location"],
                         key_on = 'feature.properties.WARD_NAME',
                         Highlight= True,
                         fill_color='YlGnBu',
                         fill_opacity=0.7,
                         line_opacity=.1,
                         legend_name="second location",
                         bins = bins1,
                         name = "second location"
       ).add_to(map2)
       folium_static(map2, width=800)
       st.dataframe(stores_df)
   if option == 'third location':
       folium.Choropleth(geo_data=expected, data=expected, columns=['WARD_NAME',"third location"],
                         key_on = 'feature.properties.WARD_NAME',
                         Highlight= True,
                         fill_color='YlGnBu',
                         fill_opacity=0.7,
                         line_opacity=.1,
                         legend_name="third location",
                         bins = bins2,
                         name = "third location"
       ).add_to(map2)
       folium_static(map2, width=800)
       st.dataframe(stores_df)
