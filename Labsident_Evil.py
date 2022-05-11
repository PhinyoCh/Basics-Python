damage = int(input())
zombie = input()
zombies = zombie.split()
zombies = [int(x) for x in zombies]
lsDamade = []
count = 0
for r in zombies:
  while True :
    if r > 0 :
      r = r - damage
      count = count+1
    else:
      lsDamade.append(count)
      break

print(max(lsDamade))
print(*lsDamade)
