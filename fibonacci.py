Max_Value = 1000

def fibonacci_calc(count):
    posint = int(count)
    assert isinstance(posint, (int))
    assert posint >= 0

    sequence = [0, 1]
    if posint > 2:
        for f in range(2, posint):
            parent = sequence[-1]
            grandparent = sequence[-2]
            sequence.append(grandparent + parent)
    return sequence[:posint]
