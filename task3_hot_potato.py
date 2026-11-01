from collections import deque

def circle_game(players, passes):
    li = players.split(', ')
    circle = deque(li)
    out_li = []
    while len(circle) > 1:
        for _ in range(passes):
            circle.append(circle.popleft())
        out_li.append(circle.popleft())

    for i in out_li:
        print(i,end = ' ')
    print("out, Winner:", circle[0])

team = input()
passed = int(input())
circle_game(team, passed)
