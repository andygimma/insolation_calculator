# Insolation Calculator

Insolation is the solar radiation that reaches the earth's surface, measured in W/m2.

This module allows a user to check for the average solar radiation at a specific latitude over a given number of years.

Most of the work has been done by the [climlab](https://climlab.readthedocs.io/en/latest/). This a wrapper class that I hope to use more often in the future.

## Specs

### InsolationCalculator(latitude: float)

#### daily_average(day: int) -> float

Returns the daily average insolation on a given day. The latitude is supplied in the constructor of the class.

#### daily_average_for_year(day: int) -> list

Runs daily_average() for each day in the year. Returns a list of the daily insolation for all 365 days.

#### yearly_average() -> float

Runs daily_average() for each day in the year. Returns the average insolation of all days in the year.
