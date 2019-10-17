import numpy as np
from climlab.solar.orbital import OrbitalTable
from climlab.solar.insolation import daily_insolation
from functools import reduce
from multiprocessing import Process, Manager

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

    def _append_daily_average(self, shared_list, day):
        shared_list.append(self.daily_average(day))

    def daily_average(self, day):
        insolation_data = self._daily_insolation(day)
        acc = reduce((lambda x, y: x + y), insolation_data)
        return acc / len(insolation_data)

    def daily_average_for_year(self):
        with Manager() as manager:
            shared_list = manager.list()
            processes = []
            for day in range(1, DAYS_IN_YEAR + 1):
                p = Process(target=(self._append_daily_average),
                            args=(shared_list, day))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            return list(shared_list)

    def yearly_average(self):
        daily_insolation = self.daily_average_for_year()
        acc = reduce((lambda x, y: x + y), daily_insolation)
        return acc / DAYS_IN_YEAR
