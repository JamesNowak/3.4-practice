age = int(input("What is your age?: "))

if age <= 1:
    print("You are an infant.")
elif 2 < age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
