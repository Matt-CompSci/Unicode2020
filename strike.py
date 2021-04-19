def get_score(input):
    score = 0
    prevBall = 0

    for ballIdx, ball in enumerate(input):
        if ball == "X":
            score += 10
            if ballIdx + 3 < len(input):
                for i in range(min(len(input) - ballIdx - 1, 2)):
                    if input[ballIdx + i + 1] == "X":
                        score += 10
                    elif input[ballIdx + i + 1] == "/":
                        score += 10 - int(input[ballIdx + i])
                    else:
                        score += int(input[ballIdx + i + 1])

        elif ball == "/":
            score += 10 - prevBall
            if ballIdx + 3 < len(input):
                if ballIdx != len(input) - 1:
                    score += input[ballIdx + 1] == "X" and 10 or int(input[ballIdx + 1])
        else:
            score += int(ball)
            prevBall = ball == "X" and 10 or int(ball)

    return score

# Tests
print(get_score(["9", "/", "7", "1", "X", "5", "1", "0", "7", "9", "0", "3", "6", "X", "3", "1", "9", "0"]) == 99)
print(get_score(["X", "9", "/", "5", "/", "7", "2", "X", "X", "X", "9", "0", "8", "/", "9", "/", "X"]) == 187)
print(get_score(["X", "9", "/", "5", "/", "7", "2", "X", "X", "X", "9", "0", "8", "/", "X", "X", "X"]) == 198)
print(get_score(["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]) == 300)
print(get_score(["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "9", "/"]) == 289)
print(get_score(["9", "/", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]) == 290)
