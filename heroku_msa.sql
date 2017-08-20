CREATE TABLE msa_exp (
  geoid int,
  lon double precision,
  lat double precision
  );

\copy msa_exp FROM 'msa.csv' DELIMITER ',' CSV HEADER;
