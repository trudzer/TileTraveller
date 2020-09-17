def walk(direction, position):

  if direction == "e":
    position += 1
  
  if direction == "n":
    position += 10

  if direction == "w":
    position -= 1

  if direction == "s":
    position -= 10
  else:
    print("invalid input")
  
  return position
pos = 11
while pos != 33:
  inp = input("choose direction: ").lower()
  direct_inp = walk(inp, pos)
  if direct_inp > 0 and direct_inp < 34:
    pos = direct_inp
  else:
    print("invalid direction")

  direct_inp = 0
print("congratulations you win")