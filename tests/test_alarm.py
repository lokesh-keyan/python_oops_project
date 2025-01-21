from unittest.mock import Mock, patch
from TirePressure.alarm import Alarm
from TirePressure.sensor import Sensor

def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on

class StubSensor:
    def sample_pressure(self):
        return 15

def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor = StubSensor())
    alarm.check()
    assert alarm.is_alarm_on

def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    alarm = Alarm(stub_sensor)
    assert not alarm.is_alarm_on

# def test_alarm_with_high_pressure_value():
#     with patch('alarm.Sensor') as test_sensor_class:
#         test_sensor_instance = Mock()
#         test_sensor_instance.sample_pressure.return_value = 22
#         test_sensor_class.return_value = test_sensor_instance

#         alarm = Alarm()
#         alarm.check()

#         assert alarm.is_alarm_on

