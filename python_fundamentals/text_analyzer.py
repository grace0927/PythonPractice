import os
import unittest


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raise:
        IOError: If `filename` does not exist or can't be read

    Returns: The number of lines in the file
    """
    lines = 0
    chars = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return lines, chars


class TextAnalyzerTests(unittest.TestCase):
    """Tests for the `analyze_text` function."""
    def setUp(self):
        """Fixture that creates a file for the text method to use."""
        self.filename = 'source/text_analyzer_test_file.txt'
        with open(self.filename, mode='w', encoding='utf-8') as f:
            f.write('Merrill Edge is a streamlined investment service'
                    'that gives you access to the investment insights'
                    'of Merrill Lynch with the convenience of Bank of America banking.\n'
                    'We\'ll help you pursue your goals with easy-to-use tools,'
                    'independent research and simple flat-rate pricing')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 2)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 267)

    def test_no_file_error(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foo')

    def test_no_file_deletion(self):
        """Check that the function doesn't delete the file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()
