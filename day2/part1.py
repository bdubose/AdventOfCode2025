
def main():
  with open("input.txt", "r") as input_file:
    for line in input_file:
      running_sum = 0
      for rng in line.split(","):
        [lowerStr, upperStr] = rng.split("-")
        lower = int(lowerStr)
        upper = int(upperStr)
        running_sum += sum([x for x in range(lower, upper) if isInvalidId(x)])
      
      print(f"Total invalid ids: {running_sum}")


def isInvalidId(id: int):
  strId = str(id)
  if len(strId) % 2 == 1:
    return False # can't repeat
  
  half = len(strId) // 2
  return strId[:half] == strId[half:]

if __name__ == "__main__":
  main()