import numpy as np
from climlab.solar.orbital import OrbitalTable
from climlab.solar.insolation import daily_insolation

DAYS_IN_YEAR = 365
YEARS_IN_SIMULATION = 20


class InsolationCalculator(object):
    def __init__(self, latitude):
        self.latitude = latitude
        self.temps = []

    def calculate_days_average(self, day):
        years = np.linspace(-20, 0, 20)
        orb = OrbitalTable.interp(kyear=years)
        return daily_insolation(lat=self.latitude, day=day, orb=orb)
