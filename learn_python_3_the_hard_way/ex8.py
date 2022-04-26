formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, True, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "난 이게 있쬬.",
    "지금 막 써 주신 그것.",
    "하지만 '노래'하진 않아요.",
    "그러니까 잘 자요."
))
