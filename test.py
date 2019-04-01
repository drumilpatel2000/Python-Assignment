import unittest
from Assignment import Person,scrap 
from Exception import DataException

class PersonError(unittest.TestCase):
    
    global Ayush
    Ayush = Person('ayush.jain','Ayush Jain', ['IMG'], 'XYZ' ) 

    def test_username(self):
        self.assertEqual('ayush.jain', Ayush.username)

    def test_name(self):
        self.assertEqual('Ayush Jain', Ayush.name)

    def test_city(self):
        self.assertEqual('XYZ', Ayush.city)

    def test_work(self):
        self.assertEqual(['IMG'], Ayush.work)
    
    global Error
    Error = Person()
    
    def test_work_null(self):
        with self.assertRaises(Exception):
            Error.work
    
    def test_username_null(self):
        with self.assertRaises(Exception):
            Error.username

    def test_invalid(self):
        scrap('swapnil.negi09')
        self.assertEqual('My name is Swapnil Negi and my current city is Roorkee', scrap('swapnil.negi09'))
            
if __name__ == '__main__':
    unittest.main()