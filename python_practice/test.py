import unittest
import random
import sys
from primes import is_prime
from primes_gold import is_prime_gold

class Test(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(is_prime(0), False)

    def test_one(self):
        self.assertEqual(is_prime(1), False)
        
    def test_two(self):
        self.assertEqual(is_prime(2), True)
    def test_random(self):
        for i in range(100):
            with self.subTest(i=i):
                number = random.randint(0, 10000)
                self.assertEqual(is_prime(number), is_prime_gold(number))
           
         

if __name__ == '__main__':
    unittest.main()