import unittest
from vehicle import Vehicle, ElectricVehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("Toyota", "Camry", 2020)

    def test_initialization(self):
        self.assertEqual(self.vehicle.brand, "Toyota")
        self.assertEqual(self.vehicle.model, "Camry")
        self.assertEqual(self.vehicle.year, 2020)
        self.assertEqual(self.vehicle.gaz_tank_size, 45)
        self.assertEqual(self.vehicle.fuel_level, 0)

    def test_fuel_up(self):
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is empty and can not move.")
        self.vehicle.fuel_level = 20
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")

    def test_drive(self):
        self.assertEqual(self.vehicle.drive, "The Camry is now driving.")


class TestElectricVehicle(unittest.TestCase):
    def setUp(self):
        self.e_vehicle = ElectricVehicle("Tesla", "Model S", 2022)

    def test_initialization(self):
        self.assertEqual(self.e_vehicle.brand, "Tesla")
        self.assertEqual(self.e_vehicle.model, "Model S")
        self.assertEqual(self.e_vehicle.year, 2022)
        self.assertEqual(self.e_vehicle.battery_size, 85)
        self.assertEqual(self.e_vehicle.charge_level, 0)

    def test_charge(self):
        self.assertEqual(self.e_vehicle.charge, "The vehicle is now charged.")

    def test_fuel_up(self):
        self.assertEqual(self.e_vehicle.fuel_up, "This vehicle has no fuel tank!")


if __name__ == '__main__':
    unittest.main()
