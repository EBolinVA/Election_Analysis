temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

score = int(input("What is your Grade? "))

# if grade is 90 or above then it's an A
if score >= 90:
    print("Your grade is an A")

# if grade is 80-89 then it's a B
elif score >= 80:
    print("Your grade is a B")

# if grade is 70-79 then it's a C
elif score >= 70:
    print("Your grade is a C")

#if grade is 60-69 then it's a D
elif score >= 60:
    print("Your grade is a D")

#everything else is F
else:
    print("Your grade is an F")