# Problem: Suggest activities based on weather (eg. Sunny - go for a walk, Rainy - read a book, Snowy - build a snowman).

print("Sunny, Rainy, Snowy")
weather = input("☺️ What's the weather?\t")

activity = "😟 You may have entered an invalid weather..!"
weather = weather.lower()

if weather == "sunny": activity = "🚶‍♂️ Go for a walk..!"
elif weather == "rainy": activity = "📖 Read a book..!"
elif weather == "snowy": activity = "☃️ Build a snowman..!"

print(activity)