CREATE TABLE msa_imp (
  geoid int,
  lon double precision,
  lat double precision
  );

\copy msa_imp FROM 'msa.csv' DELIMITER ',' CSV HEADER;
