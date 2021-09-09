## taken from
## https://gist.github.com/k0emt/1187769
## last accessed 09.09.21, 10:29
__author__ = 'k0emt'

import unittest
from Experiment import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world')

if __name__ == '__main__':
    unittest.main()
