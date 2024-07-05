import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")
    def test_single_character(self):
        self.assertEqual(generate_soundex("G"), "G000")
    def test_other_cases(self):
        self.assertEqual(generate_soundex("Saravanan"), "S615")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Air"), "A600")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Ashcroft"), "A261")
        self.assertEqual(generate_soundex("Pfister"), "P236")
        self.assertEqual(generate_soundex("A23F"), "A100")
        self.assertEqual(generate_soundex("AEIOU"), "A000")

if __name__ == '__main__':
 unittest.main()
