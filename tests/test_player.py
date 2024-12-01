import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'source'))
from player import player_pon

class TestPlayerPon(unittest.TestCase):
    def test_input_1_returns_goo(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(player_pon(), "グー")

    def test_input_2_returns_choki(self):
        with patch('builtins.input', return_value='2'):
            self.assertEqual(player_pon(), "チョキ")

    def test_input_3_returns_paa(self):
        with patch('builtins.input', return_value='3'):
            self.assertEqual(player_pon(), "パー")

    def test_invalid_input_prompts_again(self):
        with patch('builtins.input', side_effect=['0', '1']):
            self.assertEqual(player_pon(), "グー")