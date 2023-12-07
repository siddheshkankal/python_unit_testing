import unittest
from security_system import SecuritySystem
from camera import Camera
from sensor import Sensor
from alarm import Alarm
 
 
class TestSecuritySystem(unittest.TestCase):
    def setUp(self):
        self.cameras = [
            Camera('Front Door'),
            Camera('Back Door'),
            Camera('Garage'),
        ]
        self.sensors = [Sensor('Window Sensor'), Sensor('Motion Sensor')]
        self.alarms = [Alarm('Main Alarm'), Alarm('Backup Alarm')]
        self.system = SecuritySystem(
            self.cameras, self.sensors, self.alarms
        )
 
    def test_arm(self):
        self.system.arm()
        self.assertTrue(self.system.armed)
 
    def test_disarm(self):
        self.system.armed = True
        self.system.disarm()
        self.assertFalse(self.system.armed)
 
    def test_notify_authorities(self):
        self.system.armed = True
        self.assertEqual(
            self.system.notify_authorities(),
            'Notifying authorities of a security breach...',
        )
 
        self.system.armed = False
        self.assertEqual(
            self.system.notify_authorities(), 'System is not armed.'
        )
 
    def test_detect_breach(self):
        self.assertFalse(self.system.detect_breach())
 
        self.system.armed = True
        self.system.sensors[0].breach_detected = True
        self.assertTrue(self.system.detect_breach())