import unittest
from script import generate_data

class TestGenerateData(unittest.TestCase):
    def test_data_length(self):
        """Test that the function returns the correct number of rows"""
        data = generate_data(10)
        self.assertEqual(len(data), 10)
        
    def test_data_format(self):
        """Test that the function returns data in the correct format"""
        data = generate_data(1)
        self.assertIsInstance(data[0][0], int)
        self.assertIsInstance(data[0][1], str)

    def test_data_range(self):
        """Test that the function returns data with the correct range"""
        data = generate_data(1)
        self.assertGreaterEqual(data[0][0], 1000)
        self.assertLessEqual(data[0][0], 9999)

    def test_data_string_length(self):
        """Test that the function returns data with the correct string length"""
        data = generate_data(1)
        self.assertEqual(len(data[0][1]), 10)

if __name__ == '__main__':
    unittest.main()
