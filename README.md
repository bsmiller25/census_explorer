# census_explorer

Create an online tool that generates two or more interactive visualizations of the most recent population estimate and/or median income for the 100 largest US cities, utilizing the census API.

## Approach

Use Python with Flask to server an HTML file using Leaflet and CanvasJS to display an interactive map and an interactive bar chart. The geometry data (http://www2.census.gov/geo/tiger/GENZ2016/shp/cb_2016_us_cbsa_500k.zip) is stored in a PostGIS database based on MSA. The population data is collected via the Census Population API (https://api.census.gov/data/2016/pep/population.html) by Python and passed as a GeoJSON object. The GeoJSON object is then parsed and rendered as the webmap and the bar chart. 

Hosted at: https://evening-plains-96107.herokuapp.com/

To run locally:  

run: bash 01_loadMSAshape.sh  

export DATABASE_URL='postgresql:///[database]'  
for me:  
export DATABASE_URL='postgresql:///ben'  

Then: export FLASK_APP='app.py' flask run

OR if hosting on heroku

heroku local web

## Programs

### 01_loadMSAshape.sh

Run locally only.

This downloads the MSA shapefile, stores it in a PostGIS table, calculates the centroids, exports the csv, and creates the new table from the csv. The csv is git controlled and sent to heroku where it can be loaded.

This awkwardness handles a Heroku issue I encountered: shp2pgsql did not work on heroku.

### app.py 

Python script that uses flask to serve the front-end. Handles census api and postgis integration.

### templates/index.html

Interactive Leaflet map and canvisjs column chart for the population data

### msa_export.sql

Does the first part of solving the Heroku issue. Outputs msa.csv

### heroku_msa.sql

Contains codes for creating the MSA lat/lon table on heroku. 

