# brazil-public-healthcare-analytics
Analytics projects about Brazil's Public Healthcare

## Brazil Vaccination Coverage Analysis
### Data Source
DATASUS - Vaccination Coverage
## Methodology
Data extraction, cleaning, transformation and analysis using Python, PostgreSQL and SQL.
## Data Pipeline

The project uses a Python ETL pipeline:

- Extract: reads raw DATASUS CSV files
- Transform: cleans and normalizes vaccination data
- Load: stores analytical tables in PostgreSQL

## Technologies
Python: Pandas, SQLAlquemy
SQL: PostgreSQL

## Environment Setup

1. Copy .env.example to .env
2. Add your local database credentials
3. Run the ETL pipeline
4. Start the API server