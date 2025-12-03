
# 17545 too high

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
  ix = -1
  tens = 0
  for char in range(9, 0, -1):
    ix = bank.find(str(char))
    if ix != -1 and ix != (len(bank) - 1): # can't be the last character either
      tens = char
      break
  
  to_the_right = bank[ix+1:].strip()
  print(f"\tFound: {tens}. Now processing: {to_the_right}")
  for char in range(9, 0, -1):
    ones_ix = to_the_right.find(str(char))
    if ones_ix != -1:
      print(f"\tReturning: {tens}{char}")
      return int(str(tens) + str(char))
    
  assert False # should not get here

if __name__ == "__main__":
  main()