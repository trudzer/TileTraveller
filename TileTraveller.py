#https://github.com/trudzer
#https://github.com/JakobOli
#https://github.com/trudzer/TileTraveller
#https://github.com/trudzer/TileTraveller/blob/master/TileTraveller.py

def walk(direction, position):

  if direction == "e":
    position += 10
  
  elif direction == "n":
    position += 1

  elif direction == "w":
    position -= 10

  elif direction == "s":
    position -= 1
  
  return position
pos = 11
inp = input
while pos != 31:
  direct_inp = walk(inp, pos)
  pos = direct_inp
  if direct_inp > 0 and direct_inp < 34:
    if pos == 11:
      print("You can travel: (N)orth.")
      inp = input("choose direction: ").lower()
    if pos == 12:
      print ("You can travel: (N)orth or (E)ast or (S)outh")
      inp = input("choose direction: ").lower()
    if pos == 13:
      print ("You can travel: (E)ast or (S)outh.")
      inp = input("choose direction: ").lower()
    if pos == 21:
      print("you can travel: (N)orth")
      inp = input("choose direction: ").lower()
        
    if pos == 22:
      print("You can travel: (W)est or (S)outh")
      inp = input("choose direction: ").lower()
        
    if pos == 23: 
      print ("You can travel: (E)ast or (W)est.")
      inp = input("choose direction: ").lower()
        
    if pos == 32:
      print("You can travel: (N)orth or (S)outh.")
      inp = input("choose direction: ").lower()
    if pos == 33:
      print("You can travel: (S)outh or (W)est.")
      inp = input("choose direction: ").lower()
  elif pos < 0 and pos > 33:
    print("invalid direction")

  direct_inp = 0
print("congratulations you win")