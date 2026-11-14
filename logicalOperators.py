temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is on!")

age = 22
is_online = True

if age == 20 and is_online:
    print("Hello my brother!")
elif age < 20 and is_online:
    print("Okay, go to sleep!")
elif age > 28 and age < 40 and is_online:
    print("Come outside!")
else: 
    print("OOOPs")