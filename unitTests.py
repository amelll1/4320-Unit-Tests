import unittest
from inputValidation import validate_symbol, validate_chart_type,validate_time_series

class TestInputValidation(unittest.TestCase):
    def test_validate_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))  
        #These next three should be invalid
        self.assertFalse(validate_symbol("aapl"))  
        self.assertFalse(validate_symbol("AAP"))   
        self.assertFalse(validate_symbol("AAPL123")) 

    def test_validate_chart_type(self):
        self.assertTrue(validate_chart_type('1'))  
        self.assertTrue(validate_chart_type('2'))  
        self.assertFalse(validate_chart_type('3'))  

    
    def test_validate_time_series(self):
        self.assertTrue(validate_time_series('1'))  
        self.assertTrue(validate_time_series('2'))  
        self.assertTrue(validate_time_series('3'))  
        self.assertTrue(validate_time_series('4'))  
        self.assertFalse(validate_time_series('5')) 


