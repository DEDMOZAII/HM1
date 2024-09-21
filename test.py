name = "asdqa"
value = []
print(id(value))
def vovik_true(a, b=1):
    a.append(b)
    print(a)
    print(id(a))
vovik_true(value)
print(value)
print(id(value))
