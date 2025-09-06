# function that takes int age and goal
# Subtracts 220-age for max_HR
# Print max_HR and target heart rate based on goal
def heart_rate(age,goal):
    max_HR = 220-age
    print(f"Your maximum heart rate is: {max_HR}")

    #range between 80% and 100%
    if(goal == 'S'):
        print(f"Your target heart rate is between {(80/100)*max_HR} and {max_HR}")
    #range between 60% and 80%
    elif(goal == 'E'):
        print(f"Your target heart rate is between {(60/100)*max_HR} and {(80/100)*max_HR}")

#Ask users for age and goal and call function
user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")
heart_rate(user_age, user_goal)
