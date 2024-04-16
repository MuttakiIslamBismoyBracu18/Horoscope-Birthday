import unittest
from datetime import datetime
from main import calculate_life_path_number, count_leap_years, get_zodiac_sign

class TestApp(unittest.TestCase):

    def test_calculate_life_path_number(self):
        test_cases = [
            (datetime(1990, 12, 25), 2),  # 1+9+9+0+1+2+2+5 = 29 -> 2+9 = 11 -> 1+1 = 2
            (datetime(2000, 1, 1), 4),    # 2+0+0+0+1+1+1 = 4
            (datetime(1985, 10, 23), 2),  # 1+9+8+5+1+0+2+3 = 29 -> 2+9 = 11 -> 1+1 = 2
            (datetime(2000, 1, 1), 4),
            (datetime(1995, 5, 17), 1),  # 1+9+9+5+5+1+7 = 37 -> 3+7 = 10 -> 1+0 = 1
            (datetime(1988, 12, 29), 4),  # 1+9+8+8+1+2+2+9 = 40 -> 4+0 = 4
            (datetime(2002, 2, 2), 8),  # 2+0+0+2+2+2 = 8
            (datetime(1990, 6, 25), 5),  # 1+9+9+0+6+2+5 = 32 -> 3+2 = 5
            (datetime(2021, 3, 7), 6),  # 2+0+2+1+3+7 = 15 -> 1+5 = 6
            (datetime(1964, 7, 12), 3),  # 1+9+6+4+7+1+2 = 30 -> 3+0 = 3
            (datetime(1975, 11, 5), 2),  # 1+9+7+5+1+1+5 = 29 -> 2+9 = 11 -> 1+1 = 2
            (datetime(1942, 8, 23), 2),  # 1+9+4+2+8+2+3 = 29 -> 2+9 = 11 -> 1+1 = 2
            (datetime(1983, 4, 14), 3),  # 1+9+8+3+4+1+4 = 30 -> 3+0 = 3
            (datetime(2007, 9, 18), 9),  # 2+0+0+7+9+1+8 = 27 -> 2+7 = 9
            (datetime(2012, 12, 21), 2),  # 2+0+1+2+1+2+2+1 = 11 -> 1+1 = 2
            (datetime(1980, 3, 5), 8),   # 1+9+8+0+3+5 = 26 -> 2+6 = 8
            (datetime(1945, 5, 29), 8),  # 1+9+4+5+5+2+9 = 35 -> 3+5 = 8
            (datetime(1999, 1, 1), 3),   # 1+9+9+9+1+1 = 30 -> 3+0 = 3
        ]
        for birth_date, expected in test_cases:
            self.assertEqual(calculate_life_path_number(birth_date.month, birth_date.day, birth_date.year), expected)

    def test_count_leap_years(self):
        test_cases = [
            (2000, 2020, 6),  # 2000, 2004, 2008, 2012, 2016, 2020
            (1990, 2000, 3),  # 1992, 1996, 2000
            (1985, 1985, 0),  # No leap year
            (2000, 2020, 6),
            (1990, 2000, 3),
            (1985, 1985, 0),
            (1960, 1969, 3),
            (1900, 2000, 25),
            (1800, 1900, 24),
            (1600, 1700, 25),  # 1600 is a leap year
            (2001, 2021, 5),
            (2020, 2020, 1),   # Only one leap year
            (2000, 2004, 2),   # Two leap years, including a century leap year
            (1996, 2000, 2),
            (1988, 1992, 2),
            (1952, 1960, 3),
            (1904, 1912, 3),
            (1888, 1896, 3),
        ]
        for year1, year2, expected in test_cases:
            self.assertEqual(count_leap_years(year1, year2), expected)

    def test_get_zodiac_sign(self):
        test_cases = [
            ((1, 20), 'Aquarius'),
            ((2, 18), 'Aquarius'),
            ((2, 19), 'Pisces'),
            ((3, 20), 'Pisces'),
            ((3, 21), 'Aries'),
            ((4, 19), 'Aries'),
            ((4, 20), 'Taurus'),
            ((5, 20), 'Taurus'),
            ((5, 21), 'Gemini'),
            ((6, 20), 'Gemini'),
            ((6, 21), 'Cancer'),
            ((7, 22), 'Cancer'),
            ((7, 23), 'Leo'),
            ((8, 22), 'Leo'),
            ((8, 23), 'Virgo'),
            ((9, 22), 'Virgo'),
            ((9, 23), 'Libra'),
            ((10, 22), 'Libra'),
            ((10, 23), 'Scorpio'),
            ((11, 21), 'Scorpio'),
            ((11, 22), 'Sagittarius'),
            ((12, 21), 'Sagittarius'),
            ((12, 22), 'Capricorn'),
            ((1, 19), 'Capricorn'),
            ((1, 20), 'Aquarius'), 
            ((2, 18), 'Aquarius'), 
            ((2, 19), 'Pisces'),  
            ((3, 20), 'Pisces'), 
            ((2, 29), 'Pisces'),  
            ((6, 21), 'Cancer'),  
            ((11, 22), 'Sagittarius'),
            ((12, 22), 'Capricorn'),
            ((4, 20), 'Taurus'),  
            ((8, 23), 'Virgo'),  
        ]
        for (month, day), expected_sign in test_cases:
            with self.subTest(month=month, day=day):
                self.assertEqual(get_zodiac_sign(month, day), expected_sign)

if __name__ == '__main__':
    unittest.main()
