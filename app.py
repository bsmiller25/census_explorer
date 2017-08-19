from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import requests
import sqlalchemy as sql 
import os
app = Flask(__name__)


@app.route('/')
def index():
    '''
    The main page of this webtool.
    '''
    # sql connection
    engine = sql.create_engine(os.getenv('DATABASE_URL'))
    
    # read in msa shapes
    query = 'SELECT geoid, \
                    ST_X(ST_Centroid(geom)) as lon,\
                    ST_Y(ST_Centroid(geom)) as lat\
             FROM cb_2016_us_cbsa_500k;'
    msa = pd.read_sql_query(query, engine)

    #
    url = 'https://api.census.gov/data/2016/pep/population?get=POP,GEONAME&for=metropolitan+statistical+area/micropolitan+statistical+area:*'
    pops = {d[2]: d[:2] for d in requests.get(url).json()}
    
    return render_template('index.html',
                           title = 'Census Explorer',
                           pops = pops
                           )
