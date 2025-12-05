

def main():
  with open("input.txt", "r") as input_file:
    max_joltage = sum(
      max_bank_joltage(bank.strip(), 12)
      for bank
      in input_file
    )
    print(f"Max Joltage for all banks: {max_joltage}")

def max_bank_joltage(bank: str, length: int) -> int:
  print(f"Processing bank ({length}): " + bank)
  num, ix = new_find_max(bank, length)

  if length == 1:
    return num
  
  leftover = bank[ix+1:].strip()
  return int(f"{num}{max_bank_joltage(leftover, length - 1)}")

def new_find_max(string: str, chars_needed: int):
  search_str = string[:(len(string) + 1)-(chars_needed)]
  for char in range(9, 0, -1):
    ix = search_str.find(str(char))
    if ix != -1:
      return char, ix
  assert False # we cannot get here

def more_chars_left(string: str, ix: int, requires_more_chars: bool):
  if not requires_more_chars:
    return True
  return ix != (len(string) - 1)

if __name__ == "__main__":
  main()