"""
A program that asks user to enter dish name and should print which cuisine is that dish
"""
kenyan = ["omena", "ugali", "matumbo"]
indian = ["samosa", "naan", "daal"]
american = ["pizza" ,"burger", "waffles"]

dish = input("Enter dish of choice: ")


if dish in kenyan:
    print("Kenyan")
elif dish in indian:
    print("Indian")
elif dish in american:
    print("American")
else:
    print("Not applicable")
