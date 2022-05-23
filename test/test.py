import unittest

from chapter_15.rolling_dice.die import Die


class Test(unittest.TestCase):

    def test_die_roll(self):
        '''掷色子'''
        die =  Die()
        for i in range(1000):
            num = die.roll()
            self.assertTrue(1 <= num <=6)

