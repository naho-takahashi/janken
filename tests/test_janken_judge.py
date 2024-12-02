import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
import unittest
from janken_judge import judge

class TestJankenJudge(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(judge('グー', 'グー'), 'draw')
        self.assertEqual(judge('チョキ', 'チョキ'), 'draw')
        self.assertEqual(judge('パー', 'パー'), 'draw')

    def test_player_win(self):
        self.assertEqual(judge('チョキ', 'グー'), 'player_win')
        self.assertEqual(judge('パー', 'チョキ'), 'player_win')
        self.assertEqual(judge('グー', 'パー'), 'player_win')

    def test_computer_win(self):
        self.assertEqual(judge('グー', 'チョキ'), 'computer_win')
        self.assertEqual(judge('チョキ', 'パー'), 'computer_win')
        self.assertEqual(judge('パー', 'グー'), 'computer_win')

if __name__ == '__main__':
    unittest.main()