score = float(input("enter your score"))

if 0 <= score <= 100:
    print("invalid score")
if score >= 50:
    print("you passed")
else:
    print("you failed!")
