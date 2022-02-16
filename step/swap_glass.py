white_mug = "coffee"
transparent_mug = "tea"
transparent_glass = ""

print("White mug:", white_mug)
print("Transparent mug:", transparent_mug)
print("Transparent glass:", transparent_glass)

# Step one
transparent_glass = transparent_mug

# Step two
transparent_mug = white_mug

# Step three
white_mug = transparent_glass

print("\nAfter swap")
print("White mug:", white_mug)
print("Transparent mug:", transparent_mug)
print("Transparent glass:", transparent_glass)