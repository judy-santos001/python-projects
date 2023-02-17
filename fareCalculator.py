def calculator(num_1, num_2, operação):
  result = 0

  if opera == "+":
    result = num_1 + num_2

  elif opera == "-":
    result = num_1 - num_2

  elif opera == "*":
    result = num_1 * num_2

  elif opera =="/":
    result = num_1 / num_2

  print(f"{num_1} {opera} {num_2} = {result}")
  
calculator(5, 5, "+")
calculator(12, 4, "/")
calculator(5, 10, "*")
calculator(8, 3, "-")