"""
To look for key and say where it's found
"""
key_location = "kitchen"
locations =  ["bedroom", "sitting room", "kitchen", "bathroom"]

for i in locations:
    if i == key_location:
        print("Key is found in", i)
    else:
        print("Key is not found in", i)
