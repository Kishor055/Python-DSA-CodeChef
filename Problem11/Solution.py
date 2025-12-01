# Number of test cases
T = int(input())

for _ in range(T):
    X = int(input())       # Total prize pool factor
    S = input().strip()    # Result string of length 14

    carlsen_points = 0
    chef_points = 0

    # Calculate points
    for result in S:
        if result == 'C':
            carlsen_points += 2
        elif result == 'N':
            chef_points += 2
        elif result == 'D':
            carlsen_points += 1
            chef_points += 1

    # Determine Carlsen's prize
    if carlsen_points > chef_points:
        prize = 60 * X
    elif carlsen_points < chef_points:
        prize = 40 * X
    else:  # Tie: Carlsen wins as defending champion
        prize = 55 * X

    print(prize)
