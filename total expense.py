"""
You are given two lists of numbers and need to find total of each of these list
"""
tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

def calculate_total(exp):
    total = 0
    for items in exp:
        total = total + items
    return total

t_total = calculate_total(tom_exp_list)
j_total = calculate_total(joe_exp_list)

print(j_total)
print(t_total)