
# def get_odds():
#     for i in range(10):
#         if i % 2 == 1:
#             yield i
# oddser = get_odds()
# oddser_list = list(oddser)
#
# print(oddser_list[2])

def outer(a , b):
    a = a * 2
    b = b * 3
    def inner(c,d):
        return c + d + a + b
    return inner

k = outer(1, 2)

print(type(k))
print(k(2,4))

def good():
    a = ["harry", "hermione", "ron"]
    return print(a)

good()

















