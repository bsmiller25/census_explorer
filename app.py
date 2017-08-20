from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import requests
import sqlalchemy as sql 
import os
from df_to_geojson import df_to_geojson
app = Flask(__name__)


@app.route('/')
def index():
    '''
    The main page of this webtool.
    '''
    # sql connection
    engine = sql.create_engine(os.getenv('DATABASE_URL'))
    
    # read in msa shapes
    # query = 'SELECT geoid, \
    #                 ST_X(ST_Centroid(geom)) as lon,\
    #                 ST_Y(ST_Centroid(geom)) as lat\
    #          FROM cb_2016_us_cbsa_500k;'
    query = 'SELECT * FROM msa_imp;'
    msa = pd.read_sql_query(query, engine)
    
    # api
    url = 'https://api.census.gov/data/2016/pep/population?get=POP,GEONAME&for=metropolitan+statistical+area/micropolitan+statistical+area:*'
    pops = requests.get(url).json()
    pops_df = pd.DataFrame(pops[1:], columns=['pop', 'name', 'msa'])
    pops_df = pops_df.merge(msa, left_on='msa', right_on='geoid')
    pops_df['pop'] = round(pops_df['pop'].astype('int')/1000000, 2)
    pops_df = pops_df.sort_values('pop', ascending=False)[:100]
    
    pops_gj = df_to_geojson(pops_df, properties=['name', 'pop'], lat='lat', lon='lon')
    return render_template('index.html',
                           title = 'Census Explorer',
                           pops = pops_gj
                           )
