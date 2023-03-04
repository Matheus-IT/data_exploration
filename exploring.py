t = input()
answers = input().split(" ")

right_answers = [a for a in answers if a == t]

print(len(right_answers))
