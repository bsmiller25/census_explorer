# census_explorer

Create an online tool that generates two or more interactive visualizations of the most recent population estimate and/or median income for the 100 largest US cities, utilizing the census API.

Hosted at: https://evening-plains-96107.herokuapp.com/

## Programs

### app.py 

Python script that uses flask to serve the front-end. Handles census api and postgis integration.

### templates/index.html

Interactive Leaflet map and canvisjs column chart for the population data

### 01_loadMSAshape.sh

Run locally only: Downloads shapefile for the MSAs. Loads them to postgis database. 

Heroku issue: shp2pgsql did not work on heroku. To solve this, locally, I take the centroid of the msa geometries and export the lat/lons to a csv. The csv is then loaded to psql.

### msa_export.sql

Does the first part of solving the Heroku issue. Outputs msa.csv

### heroku_msa.sql

Creates psql table from msa.csv. This works on Heroku.

