def find_extra_integer(x, y):
  # Create dictionaries to store the counts of each number in each list
  x_counts = {}
  y_counts = {}

  # Count the occurrences of each number in each list
  for num in x:
    if num in x_counts:
      x_counts[num] += 1
    else:
      x_counts[num] = 1
  for num in y:
    if num in y_counts:
      y_counts[num] += 1
    else:
      y_counts[num] = 1

  # Find the number that appears in one list but not the other
  for num in x_counts:
    if num not in y_counts:
      return num
  for num in y_counts:
    if num not in x_counts:
      return num

  # If no such number is found, return None
  return None
