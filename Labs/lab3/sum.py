# import operator
# ops = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.div}
x = int(input("x = "))
op = input("operation(+,-,*,/)")
y = int(input("y = "))
if op == "+":
    z = x + y
    print(x, "+", y, "=", z)
elif op == "-":
    z = x - y
    print(x, "-", y, "=", z)
elif op == "*":
    z = x * y
    print(x, "*", y, "=", z)
else:
    z = x / y
    print(x, "/", y, "=", z)
# z = x op y

# print(op_func(x,y))
