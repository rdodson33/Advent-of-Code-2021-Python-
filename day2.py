forwards = sum(list(map(lambda x: int(x.split()[1]), list(filter(lambda x: x.split()[0] == 'forward', open("day2input.txt").readlines())))))
down = sum(list(map(lambda x: int(x.split()[1]), list(filter(lambda x: x.split()[0] == 'down', open("day2input.txt").readlines())))))
up = sum(list(map(lambda x: int(x.split()[1]), list(filter(lambda x: x.split()[0] == 'up', open("day2input.txt").readlines())))))
depth = down - up
part1 = forwards * depth
print(part1)

def part2(input):
    forward = 0
    aim = 0
    depth = 0
    for i in input:
        if (i.split()[0] == 'down'):
            aim = aim + int(i.split()[1])
        elif (i.split()[0] == 'up'):
            aim = aim - int(i.split()[1])
        elif (i.split()[0] == 'forward'):
            forward = forward + int(i.split()[1])
            depth = depth + (aim * int(i.split()[1]))
    answer = forward * depth
    print(answer)
 
part2(open("day2input.txt").readlines())