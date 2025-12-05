
import unittest
from dataclasses import dataclass
from day3.part2 import max_bank_joltage

class Day3Part2Tests(unittest.TestCase):
  def test_find_max_number(self):
    tests = [
      TestCase("123", 2, 23),
      TestCase("987654321111111", 12, 987654321111),
      TestCase("811111111111119", 12, 811111111119),
      TestCase("234234234234278", 12, 434234234278),
      TestCase("818181911112111", 12, 888911112111),
    ]

    for test in tests:
      self.assertEqual(max_bank_joltage(test.input, test.length), test.expected)

@dataclass
class TestCase:
  input: str
  length: int
  expected: int