# x = [1, 2, 5, -10, 9, 6]
def get_even_list(x):
    evens = []
    for number in x:
        if number % 2 == 0:
            evens.append(number)
    return evens
# print(evens)
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
