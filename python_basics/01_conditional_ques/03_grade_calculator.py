# Problem: Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score = int(input("Enter Score:\t"))

while score > 100:
    print("⚠️ Invalid Score..!\nMax score allowed: 100")
    score = int(input("Enter score again:\t"))

if score >= 90: print("Grade: A")
elif score >= 80: print("Grade: B")
elif score >= 70: print("Grade: C")
elif score >= 60: print("Grade: D")
elif score < 60: print("Grade: F")
