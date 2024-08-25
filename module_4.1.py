from true_math import divide as true_divide
from fake_math import divide as fake_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

# true_math
# from math import inf
# def divide(first, second):
#     if second == 0:
#         return 'inf'
#     else:
#         return (first / second)

# fake_math
# def divide(first, second):
#     if second == 0:
#         return ('Error!')
#     else:
#         return (first / second)