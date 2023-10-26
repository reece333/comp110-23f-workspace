"""PLAYING WITH MY DICT."""

#creating a new dict
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my dict")
print(ice_cream)

#adding key,value pair to my dict
ice_cream["mint"] = 3
print("Added mint to my dict!!")
print(ice_cream)

#removing mint from my dict
ice_cream.pop("mint")
print("No more mint dict :(")
print(ice_cream)

#accessing and modifying my dict
print(f"We've gotten {ice_cream['chocolate']} orders of chocolate!!!")
ice_cream["vanilla"] = 10
print(ice_cream)

#measuring the length of my dict
print(f"We offer {len(ice_cream)} different ice cream flavors!")

#check for keys in my dict
if "mint" in ice_cream:
    print(f"There have been {ice_cream['mint']} orders of mint")
else: 
    print("no orders of mint...")
print("Chocolate in dict??")
print("chocolate" in ice_cream)

#for loop my dict
for key in ice_cream:
    print(f"{(key)} has {ice_cream[key]} orders!!!")