import unittest
from datetime import datetime
from main import calculate_life_path_number, count_leap_years, get_zodiac_sign

class BoundaryValueTest(unittest.TestCase):

    def test_calculate_life_path_number_boundaries(self):
        
        test_cases = [
            (datetime(1999, 12, 31), 8),
            (datetime(2000, 1, 1), 4),
            (datetime(2000, 1, 1), 4), 
            (datetime(2001, 1, 1), 5),
            (datetime(1980, 1, 1), 2),
            (datetime(1980, 1, 2), 3),
            (datetime(1982, 12, 31), 9),
            (datetime(1983, 1, 1), 5),
            (datetime(1990, 4, 22), 9),
            (datetime(1990, 4, 23), 1),
            (datetime(2000, 12, 31), 9),
            (datetime(2001, 1, 1), 5),
            (datetime(2010, 5, 5), 4),
            (datetime(2010, 5, 6), 5),
        ]
        for birth_date, expected in test_cases:
             self.assertEqual(calculate_life_path_number(birth_date.month, birth_date.day, birth_date.year), expected)
        
    def test_count_leap_years_boundaries(self):
        test_cases = [
            (1899, 1901, 0), 
            (2000, 2004, 2),
            (1900, 1904, 1),
            (2096, 2104, 2),
            (1896, 1904, 2),
            (1996, 2004, 3),
            (1900, 1901, 0), # No leap year in this range
            (1999, 2001, 1), # The year 2000 is a leap year
            (2003, 2005, 1), # The year 2004 is a leap year
            (2096, 2104, 2), # Century leap year not included
            (2099, 2101, 0), # No leap year
            (2100, 2105, 1), # Only 2104 is a leap year
            (1992, 2000, 3), # 1992, 1996, and 2000 are leap years
        ]
        for year1, year2, expected in test_cases:
            self.assertEqual(count_leap_years(year1, year2), expected)

    def test_get_zodiac_sign_boundaries(self):
        test_cases = [
            ((3, 20), 'Pisces'),  # The last day of Pisces
            ((3, 21), 'Aries'),   # The first day of Aries
            ((4, 19), 'Aries'),   # The last day of Aries
            ((4, 20), 'Taurus'),  # The first day of Taurus
            ((5, 20), 'Taurus'),  # The last day of Taurus
            ((5, 21), 'Gemini'),  # The first day of Gemini
            ((6, 20), 'Gemini'),  # The last day of Gemini
            ((6, 21), 'Cancer'),  # The first day of Cancer
            ((7, 22), 'Cancer'),  # The last day of Cancer
            ((7, 23), 'Leo'),     # The first day of Leo
            ((8, 22), 'Leo'),     # The last day of Leo
            ((8, 23), 'Virgo'),   # The first day of Virgo
            ((9, 22), 'Virgo'),   # The last day of Virgo
            ((9, 23), 'Libra'),   # The first day of Libra
            ((10, 22), 'Libra'),  # The last day of Libra
            ((10, 23), 'Scorpio'),# The first day of Scorpio
            ((11, 21), 'Scorpio'),# The last day of Scorpio
            ((11, 22), 'Sagittarius'), # The first day of Sagittarius
            ((12, 21), 'Sagittarius'), # The last day of Sagittarius
            ((12, 22), 'Capricorn'),   # The first day of Capricorn
            ((2, 18), 'Aquarius'),
            ((2, 28), 'Pisces'),
        ]
        for (month, day), expected_sign in test_cases:
            self.assertEqual(get_zodiac_sign(month, day), expected_sign)

if __name__ == '__main__':
    unittest.main()
