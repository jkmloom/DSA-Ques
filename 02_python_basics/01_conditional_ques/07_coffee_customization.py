# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_list = ['Small', 'Medium', 'Large']

order_size = input("🍵 Enter order size:\t")
order_size = order_size[0].upper() + order_size[1:].lower()

extra_shot = 0 # set default value
extra_shot = int(input("☕ Add an Extra shot of espresso? (0/1): "))

if order_size in order_list:
    if extra_shot: order = order_size + " Coffee with extra shot"
    else: order = order_size + " Coffee"
else: print("😟 Invalid order size..!")

print(f"📃 Order: {order}")