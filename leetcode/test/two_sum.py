import unittest
from ..leetcode.two_sum import TwoSum

test_cases = [
    {
        'nums': [2, 7, 11, 15],
        'target': 9,
        'expected': [0, 1],
    },
    {
        'nums': [3, 2, 4],
        'target': 6,
        'expected': [1, 2],
    },
]


class TwoSumTests(unittest.TestCase):
    """Tests for TwoSum."""
    def setUp(self):
        self.solver = TwoSum()

    def test_function_runs(self):
        for case in test_cases:
            self.assertEqual(self.solver.run(case['nums'], case['target']), case['expected'])


if __name__ == '__main__':
    unittest.main()
