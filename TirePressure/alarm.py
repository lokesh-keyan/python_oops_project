from TirePressure.sensor import Sensor

class Alarm:
    def __init__(self, sensor=None):
        self.low_pressure_threshold = 17
        self.high_pressure_threshold = 21
        self.sensor = self.sensor = sensor if sensor else Sensor()
        self._is_alarm_on = False

    def check(self):
        pressure = self.sensor.sample_pressure()
        if pressure < self.low_pressure_threshold or self.high_pressure_threshold < pressure:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on