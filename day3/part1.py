
# 17545 too high
# 17311 correct answer

def main():
  with open("input.txt", "r") as input_file:
    max_joltage = sum(
      max_bank_joltage(bank.strip())
      for bank
      in input_file
    )
    print(f"Max Joltage for all banks: {max_joltage}")

def max_bank_joltage(bank: str) -> int:
  print("Processing bank: " + bank)
  tens, ix = find_max_number(bank, True)
  
  to_the_right = bank[ix+1:].strip()
  print(f"\tFound: {tens}. Now processing: {to_the_right}")
  ones, _ = find_max_number(to_the_right)
  return int(f"{tens}{ones}")

def find_max_number(string: str, dont_allow_final_char: bool = False):
  ix = -1
  for char in range(9, 0, -1):
    ix = string.find(str(char))
    if ix != -1 and more_chars_left(string, ix, dont_allow_final_char):
      return char, ix
  
  assert False # we cannot get here

def more_chars_left(string: str, ix: int, requires_more_chars: bool):
  if not requires_more_chars:
    return True
  return ix != (len(string) - 1)

if __name__ == "__main__":
  main()