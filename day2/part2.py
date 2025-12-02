
def main():
  with open("input.txt", "r") as input_file:
    for line in input_file:
      running_sum = 0
      for rng in line.split(","):
        [lowerStr, upperStr] = rng.split("-")
        lower = int(lowerStr)
        upper = int(upperStr)
        print(f"Working Range: {rng}")
        running_sum += sum([x for x in range(lower, upper) if isInvalidId(x)])
      
      print(f"Total invalid ids: {running_sum}")


def isInvalidId(id: int):
  strId = str(id)
  if len(strId) < 2:
    return False # can't repeat
  
  split_point = len(strId) // 2
  for i in range(split_point, 0, -1):
    parts = list(chunkstring(strId, i))
    # if all split parts are the same, then this id is invalid
    if all(x == parts[0] for x in parts):
      return True
  
  return False


def chunkstring(string: str, length: int):
    return (string[0+i:length+i] for i in range(0, len(string), length))

if __name__ == "__main__":
  main()