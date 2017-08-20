CREATE TABLE msa_exp (
  geoid int,
  lon numeric,
  lat numeric
  );

\copy msa.csv TO 'msa_exp' DELIMITER ',' CSV HEADER;
