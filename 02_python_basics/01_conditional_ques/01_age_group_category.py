# Problem: Age group categorization
# Child: <13, Teenager: 13-19, Adult: 20-59, Senoir: <=60

age = int(input("Enter age:\t"))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")