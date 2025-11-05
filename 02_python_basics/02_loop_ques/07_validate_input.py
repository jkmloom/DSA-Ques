# Problem: Validation Input
# Keep asking the user for input until they enter a number between 1 and 10

while True:
    num = int(input("Enter a number between 1-10:\t"))
    if 1 <= num <= 10:
        print("✅ Valid value..!")
        break
    else: print("❌ Invalid Number..! * TRY AGAIN *")