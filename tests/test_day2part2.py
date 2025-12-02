
import unittest
from dataclasses import dataclass
from day2.part2 import isInvalidId

class Day2Part2Tests(unittest.TestCase):
  def test_isInvalidId(self):
    tests = [
      TestCase("1212", True),
      TestCase("123456", False),
      TestCase("11", True),
      TestCase("22", True),
      TestCase("1188511885", True)
    ]

    for test in tests:
      self.assertEqual(isInvalidId(int(test.input)), test.expected)

if __name__ == "__main__":
  unittest.main()


@dataclass
class TestCase:
  input: str
  expected: bool