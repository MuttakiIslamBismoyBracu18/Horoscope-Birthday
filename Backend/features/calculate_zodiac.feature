Feature: Zodiac Calculation
  In order to provide users with their zodiac signs
  As a web application
  I want to calculate zodiac signs based on birthdays

  Scenario: User enters a valid birthday
    Given the user has entered their birthday as "06/11/1998"
    When the user requests their zodiac sign
    Then the zodiac sign "Gemini" should be returned
