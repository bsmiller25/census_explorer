CREATE TABLE msa_exp (
  geoid int,
  lon numeric,
  lat numeric
  );

\copy msa_exp FROM 'msa.csv' DELIMITER ',' CSV HEADER;
