# Problem: Choose a mode of transportation based on the distance (eg. <3km: walk, 3-15km: bike, >15km: car).

cover_distance = int(input("Enter the distance to be covered (in km):\t"))

transport_mode = ['Walk', 'Bike', 'Car']

if cover_distance < 3: print(f"Transportation Mode: {transport_mode[0]}")
elif cover_distance <= 15: print(f"Transportation Mode: {transport_mode[1]}")
else: print(f"Transportation Mode: {transport_mode[-1]}")