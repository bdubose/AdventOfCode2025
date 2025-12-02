

def main():
  dial_position = 50
  times_at_zero = 0

  with open("input.txt", "r") as input_file:
    for line in input_file:
      dial_position, passes_at_zero = process_line(line.strip(), dial_position)
      times_at_zero += passes_at_zero
      assert 0 <= dial_position <= 99

  print(f"Times at Zero: {times_at_zero}, Final position: {dial_position}")


def process_line(line: str, dial_position: int):
  "Reads the line and executes the dial command"
  direction = line[0]
  clicks = int(line[1:])
  if direction == "L":
    passes_by_zero = int((dial_position - clicks) / -100)
    new_position = (dial_position - clicks) % 100
    if (clicks > dial_position and new_position > dial_position and dial_position != 0):
      passes_by_zero += 1
    elif new_position == 0 and clicks != 100:
      passes_by_zero += 1
    
    # weird edge case idk
    if dial_position == clicks:
      passes_by_zero = 1
  else:
    passes_by_zero = int((dial_position + clicks) / 100)
    new_position = (dial_position + clicks) % 100

  assert passes_by_zero >= 0
  return new_position, passes_by_zero


# not sure what is going on. I think my tests are accurate, but I keep coming
# up with a number that is too high

if __name__ == "__main__":
  main()