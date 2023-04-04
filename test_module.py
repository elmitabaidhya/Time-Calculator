import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):

  def test_same_period(self):
    actual = add_time("3:00 PM", "3:10")
    expected = "6:10 PM"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "3:00 PM", "3:10" to return "6:10 PM"'
    )

  def test_different_period(self):
    actual = add_time("11:30 AM", "2:32")
    expected = "2:02 PM"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "11:30 AM", "2:32" to return "2:02 PM"'
    )

  def test_next_day(self):
    actual = add_time("10:10 PM", "3:30")
    expected = "1:40 AM (next day)"
    self.assertEqual(
      actual, expected,
      'Expected time to end with "(next day)" when it is the next day.')

  def test_period_change_at_twelve(self):
    actual = add_time("11:43 AM", "0:20")
    expected = "12:03 PM"
    self.assertEqual(actual, expected,
                     'Expected period to change from AM to PM at 12:00')

  def test_twenty_four(self):
    actual = add_time("11:43 PM", "24:00")
    expected = "11:43 PM (next day)"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "11:43 PM", "24:00" to return "11:43 PM"'
    )

  def test_two_days_later(self):
    actual = add_time("11:43 PM", "24:20")
    expected = "12:03 AM (2 days later)"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "11:43 PM", "24:20" to return "12:03 AM (2 days later)"'
    )

  def test_high_duration(self):
    actual = add_time("6:30 PM", "205:12")
    expected = "7:42 AM (9 days later)"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "6:30 PM", "205:12" to return "7:42 AM (9 days later)"'
    )

  def test_no_change(self):
    actual = add_time("3:00 AM", "0:00")
    expected = "3:00 AM"
    self.assertEqual(actual, expected,
                     'Expected adding 0:00 to return initial time.')

  def test_same_period_with_day(self):
    actual = add_time("11:30 AM", "2:32", "Monday")
    expected = "2:02 PM, Monday"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "11:30 AM", "2:32", "Monday" to return "2:02 PM, Monday"'
    )

  def test_twenty_four_with_day(self):
    actual = add_time("11:30 AM", "24:00", "Monday")
    expected = "11:30 AM, Tuesday (next day)"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "11:30 AM", "24:00", "Monday" to return "11:30 AM, Tuesday (next day)"'
    )

  def test_two_days_later_with_day(self):
    actual = add_time("11:43 PM", "24:20", "tueSday")
    expected = "12:03 AM, Thursday (2 days later)"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "11:43 PM", "24:20", "tueSday" to return "12:03 AM, Thursday (2 days later)"'
    )

  def test_high_duration_with_day(self):
    actual = add_time("6:30 PM", "205:12", "friDay")
    expected = "7:42 AM, Sunday (9 days later)"
    self.assertEqual(
      actual, expected,
      'Expected calling "add_time()" with "6:30 PM", "205:12", "friDay" to return "7:42 AM, Sunday (9 days later)"'
    )


if __name__ == "__main__":
  unittest.main()
