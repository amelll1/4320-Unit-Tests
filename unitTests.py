import unittest
from inputValidation import validate_symbol

class TestInputValidation(unittest.TestCase):
    def test_validate_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))  
        #These next three should be invalid
        self.assertFalse(validate_symbol("aapl"))  
        self.assertFalse(validate_symbol("AAP"))   
        self.assertFalse(validate_symbol("AAPL123")) 
