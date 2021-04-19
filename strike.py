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

# Given a string representation of a bowling score card, calculate the numeric score of the score card.
# 
# The scoring information for a bowling score card is provided below:
# 
#     Bowler is allowed a maximum of 10 frames.
#     Each frame has 10 pins.
#     Frames 1 - 9 consist of two balls (two attempts).
#     Frame 10 can consist of three balls.
#     If all pins are down using one ball, this is a strike (denoted by an X) and counts as 10 points.
#     If all pins are down using two balls, this is a spare (denoted by a /) and counts as 10 points.
#     In the event of a strike the next two balls' points are added to the strike score of 10.
#     EG: bowling a strike, five and one results in scoring of (10+5+1), 5, 1).
#     In the event of a spare the next one ball's points are added to the spare score of 10.
#     EG: bowling a spare, five and one results in scoring of (10+5), 5, 1).
#     In the event of a strike, additional attempts in that frame are not used.
#     The maximum attainable score from any frame is 30 (three strikes in a row).
# 
# 
# The score card will be passed as an array of strings constituting 10 frames. The method should return an integer score.
# 
# For example, consider the following score card:
# 
# ["9", "/", "7", "1", "X", "5", "1", "0", "7", "9", "0", "3", "6", "X", "3", "1", "9", "0"]
# 
# The total score in the above example is 99.
