# Vaccination Analytics API

## GET /vaccines

Purpose:
Returns vaccination metrics by vaccine

Response:
[
    {
        vaccine,
        average_coverage
    }
]

## GET /states

Purpose:
Returns vaccination metrics by state

Response:
[
    {
        state,
        average_coverage
    }
]

## GET /coverage/{state}

Purpose:
Returns historical vaccination coverage data for a specified state

Parameter:
state: Brazilian state code (e.g. SP, RJ)

Response:
[
    {
        year,
        state,
        average_coverage
    }
]