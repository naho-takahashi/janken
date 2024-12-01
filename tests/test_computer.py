import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'source'))
import computer

class TestComputerPon(unittest.TestCase):

    @patch('computer.random.choice', return_value='グー')
    def test_computer_pon_guu(self, mock_choice):
        result = computer.computer_pon()
        self.assertEqual(result, 'グー')

    @patch('computer.random.choice', return_value='チョキ')
    def test_computer_pon_choki(self, mock_choice):
        result = computer.computer_pon()
        self.assertEqual(result, 'チョキ')

    @patch('computer.random.choice', return_value='パー')
    def test_computer_pon_paa(self, mock_choice):
        result = computer.computer_pon()
        self.assertEqual(result, 'パー')

if __name__ == '__main__':
    unittest.main()