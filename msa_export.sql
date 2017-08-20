CREATE TABLE msa_exp AS (
SELECT geoid,
       ST_X(ST_Centroid(geom)) as lon,
       ST_Y(ST_Centroid(geom)) as lat
FROM cb_2016_us_cbsa_500k
);

\copy msa_exp TO 'msa.csv' DELIMITER ',' CSV HEADER;
