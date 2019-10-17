# Insolation Calculator

Insolation is the solar radiation that reaches the earth's surface, measured in W/m2.

This module allows a user to check for the average solar radiation at a specific latitude over a given number of years.

Most of the work has been done by the [climlab](https://climlab.readthedocs.io/en/latest/). This a wrapper class that I hope to use more often in the future.

## Testing

`$ python runtests.py`

## Run locally

1. Create a virtual environment
1. `$ pip install -r`
1. Open a python interpreter
1. Run the following:

### Example code

```
>>> from insolation_calculator.insolation_calculator import InsolationCalculator
>>> calc = InsolationCalculator(latitude=6.23)
>>> print(calc.daily_average(1)) # Average insolation on new year's day
>>> print(calc.daily_average_for_year())
>>> print(calc.yearly_average())
```

## Specs

### class InsolationCalculator(latitude: float)

#### def daily_average(day: int) -> float

Returns the daily average insolation on a given day. The latitude is supplied in the constructor of the class.

#### def daily_average_for_year() -> list

Runs daily_average() for each day in the year. Returns a list of the daily insolation for all 365 days.

#### def yearly_average() -> float

Runs daily_average() for each day in the year. Returns the average insolation of all days in the year.
