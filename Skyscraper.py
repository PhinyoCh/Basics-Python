count = 0
highest = 0
while True :
  x = input()
  x = int(x)
  if x == -1:
    break
  if x > highest :
    count = count + 1
    highest = x
print(count)
