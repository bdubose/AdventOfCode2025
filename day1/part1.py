

def main():
  dial_position = 50
  times_at_zero = 0

  with open("input.txt", "r") as input_file:
    for line in input_file:
      dial_position = process_line(line.strip(), dial_position)
      if dial_position == 0:
        times_at_zero += 1

  print(f"Times at Zero: {times_at_zero}")


def process_line(line: str, dial_position: int) -> int:
  "Reads the line and executes the dial command"
  direction = line[0]
  clicks = int(line[1:])
  if direction == "L":
    new_position = (dial_position - clicks) % 100
  else:
    new_position = (dial_position + clicks) % 100
  return new_position




if __name__ == "__main__":
  main()