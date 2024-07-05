import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(generate_soundex(""), "")
        self.assertEqual(generate_soundex("G"), "G000")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Pfister"), "P236")


if __name__ == '__main__':
 unittest.main()
