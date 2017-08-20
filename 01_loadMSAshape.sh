# run locally only because heroku doesn't have shp2pgsql

# download the shapefile
mkdir -p data
wget -O data/msa.zip http://www2.census.gov/geo/tiger/GENZ2016/shp/cb_2016_us_cbsa_500k.zip
unzip data/msa.zip -d data

# push to psql
db=$(echo $DATABASE_URL | grep -o -P '[a-z]([^\/]+)$')
shp2pgsql -s 4326 data/cb_2016_us_cbsa_500k.shp | psql -d $db

# generate csv with msa lat lon
psql -f msa_export.sql

# psql -c "\copy msa.csv TO 'msa_exp' DELIMITER ',' CSV HEADER;"
