metric = input("F of C?\n")
value = input("Input value\n")

if metric == "F":
    to_C = (float(value) - 32) * 5 / 9
    print(to_C)
elif metric == "C":
    to_F = float(value) * 9 / 5 + 32
    print(to_F)
else:
    print("Unknown metric")
