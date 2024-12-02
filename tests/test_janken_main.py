import sys
import os
import unittest
from unittest.mock import patch
source_path = os.path.join(os.path.dirname(__file__), '..', 'source')
sys.path.append(os.path.abspath(source_path))
from unittest import TestCase
from unittest.mock import patch
import janken_main

class TestJankenMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['グー', 'チョキ', 'パー'])
    def test_main(self, mock_input):
        @patch('janken_judge.judge', side_effect=['player_win', 'computer_win', 'draw'])
        def test_main(self, mock_input, mock_computer_pon, mock_judge):
            with patch('builtins.print') as mock_print:
                janken_main.main()
                mock_print.assert_any_call("あなたの勝ちです！")
                mock_print.assert_any_call("コンピューターの勝ちです！")
                mock_print.assert_any_call("あいこです！ 再度対決！")

if __name__ == '__main__':
    unittest.main()