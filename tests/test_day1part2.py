
import unittest
from day1.part2 import *
from dataclasses import dataclass

class Day1Part2Tests(unittest.TestCase):
  def test_passes_right(self):
    np, zero_passes = process_line("R500", 50)

    self.assertEqual(np, 50)
    self.assertEqual(zero_passes, 5)

  def test_passes_left(self):
    np, zero_passes = process_line("L250", 50)

    self.assertEqual(np, 0)
    self.assertEqual(zero_passes, 3)

  def test_passes_zero(self):
    np, zero_passes = process_line("L0", 50)
    np1, zero_passes1 = process_line("R0", 50)

    self.assertEqual(np, 50)
    self.assertEqual(np1, 50)
    self.assertEqual(zero_passes, 0)
    self.assertEqual(zero_passes1, 0)

  def test_one_whole_pass(self):
    np, p = process_line("L100", 0)

    self.assertEqual(np, 0)
    self.assertEqual(p, 1)
  
  def test_be_careful(self):
    np, p = process_line("R1000", 50)

    self.assertEqual(np, 50)
    self.assertEqual(p, 10)

  def test_various(self):
    tests = [
      TestCase("L2", 1, 99, 1),
      TestCase("R2", 98, 0, 1),
      TestCase("R3", 98, 1, 1),
      TestCase("R45", 7, 52, 0),
      TestCase("L45", 7, 62, 1),
      TestCase("L20", 45, 25, 0),
      TestCase("L457", 10, 53, 5),

      # from site
      TestCase("L68", 50, 82, 1),
      TestCase("L30", 82, 52, 0),
      TestCase("R48", 52, 0, 1),
      TestCase("L5", 0, 95, 0),
      TestCase("R60", 95, 55, 1),
      TestCase("L55", 55, 0, 1),
      TestCase("L1", 0, 99, 0),
      TestCase("L99", 99, 0, 1),
      TestCase("R14", 0, 14, 0),
      TestCase("L82", 14, 32, 1),
    ]
    for test in tests:
      new_pos, zeros = process_line(test.input, test.start_pos)
      self.assertEqual(new_pos, test.end_pos, f"For test case: {test.input} - {test.start_pos} (end position)")
      self.assertEqual(zeros, test.expected_zero_passes, f"For test case: {test.input} - {test.start_pos} (zero passes)")

if __name__ == "__main__":
  unittest.main()


@dataclass
class TestCase:
  input: str
  start_pos: int
  end_pos: int
  expected_zero_passes: int
