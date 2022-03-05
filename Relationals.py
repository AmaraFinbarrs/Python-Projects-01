# A conditional exercise from Python Crash Course
# Page
# My Solution Page 50.

people = {'Amanda': 100, 'Ify': 50, 'Rainbow': 500}
money = [0, 0, 0]
person = [0, 0, 0]
n = 0
for value in people.values():
    money[n] = value
    n += 1
n = 0
for p in people.keys():
    person[n] = p
    n += 1

print(person)
x, y, z = money

print(money)

if x > y and x > z:
    if y == z and y != x:
        print(f"{person[0]} is the richest but {person[1]} and "
              f"{person[2]} have the same value")
    elif y > z:
        print(f"{person[0]} is the richest followed by {person[1]} followed by {person[2]} ")
    elif z > y:
        print(f"{person[0]} is the richest followed by {person[2]} followed by {person[1]} ")
elif y > x and y > z:
    if x == z:
        print(f"{person[1]} is the richest but {person[0]} and "
              f"{person[2]} have the same value")
    elif x > z:
        print(f"{person[1]} is the richest followed by {person[0]} followed by {person[2]} ")
    elif z > x:
        print(f"{person[1]} is the richest followed by {person[2]} followed by {person[0]} ")
elif z > x and z > y:
    if x == y:
        print(f"{person[2]} is the richest but {person[0]} and "
              f"{person[1]} have the same value")
    elif x > y:
        print(f"{person[2]} is the richest followed by {person[0]} followed by {person[1]} ")
    elif z > y:
        print(f"{person[2]} is the richest followed by {person[1]} followed by {person[2]} ")
elif x == y and x != z:
    if x > z:
        print(f"{person[0]} and {person[1]} are the richest and have the same value and then {person[2]}")
elif x == z and x != y:
    if x > y:
        print(f"{person[0]} and {person[2]} are the richest and have the same value and then {person[1]}")
elif y == z and y != x:
    if y > x:
        print(f"{person[1]} and {person[2]} are the richest and have the same value and then {person[0]}")
else:
    print(f"None is richer because they all have the same value")





