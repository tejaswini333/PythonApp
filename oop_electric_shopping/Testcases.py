import unittest
from oop_electric_shopping.Admin import User

class Test_authenticate(unittest.TestCase):

    def setUp(self):
        self.service = User()

    def test_valid_username(self):
        self.assertEqual(self.service.create_user("isadmin","Y"),"valid admin user")

    def test_valid_username_password(self):
        self.assertEqual(self.service.create_user("isadmin", "111"), "Admin created successfully")

    def test_invalid_username_password(self):
        self.assertEqual(self.service.create_user("isadmin", "777"), "Admin created successfully")

    def test_valid_N_username(self):
        self.assertEqual(self.service.create_user("isadmin", "N"), "N user created successfully")

if __name__ == '__main__':
    unittest.main()
