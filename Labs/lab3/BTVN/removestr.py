
def remove_dollar_sign(x):
    string_with_no_dollars = x.replace("$","")
    return string_with_no_dollars

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# string_with_no_dollars.replace(" $", "")
# print(string_with_no_dollars)
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
