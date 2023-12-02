f = open("input.txt").read().strip()
result = 0
lookup = {
    "red":  12,
    "green": 13, 
    "blue": 14
}
for line in f.split('\n'):
    game, draws = line.split(':')
    possible = True
    for sets in draws.split(';'):
        for balls in sets.split(','):
            num, color = balls.split()
            if lookup.get(color) < int(num): 
                possible = False
    if possible:
        _, id = game.split()
        result += int(id)

print (result)