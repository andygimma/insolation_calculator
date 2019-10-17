import numpy as np
from climlab.solar.orbital import OrbitalTable
from climlab.solar.insolation import daily_insolation
from functools import reduce

DAYS_IN_YEAR = 365
YEARS_IN_SIMULATION = 20


class InsolationCalculator(object):
    def __init__(self, latitude):
        self.latitude = latitude
        self.temps = []

    def _daily_insolation(self, day):
        years = np.linspace(-YEARS_IN_SIMULATION, 0, YEARS_IN_SIMULATION)
        orb = OrbitalTable.interp(kyear=years)
        i = daily_insolation(lat=self.latitude, day=day, orb=orb)
        return i.to_dict()['data']

    def daily_average(self, day):
        insolation_data = self._daily_insolation(day)
        acc = reduce((lambda x, y: x + y), insolation_data)
        return acc / len(insolation_data)
