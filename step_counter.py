import math
print("🏃‍♂️Step Counter🏃‍♂️")

daily_step_goal = int(input("What is yur daily goal? "))

today_steps = int(input("How many steps have you taken today? "))

final_goal = daily_step_goal - today_steps
print(final_goal)

if final_goal > 0:
    print(f"You need {final_goal} more steps to reach your goal!")
else:
    print("🎉Congratualations! You've exceeded goal by {abs(final_goal) steps}")
