#1. Basic
for i in range(151):
    print(i)

#2. Multiples of 5
for i in range(1001):
    if i % 5 == 0:
        print(i)

#3. Counting the Dojo Way
for i in range(101):
    if i == 0:
        print("Coding", "Coding Dojo")
    elif i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4. Sum all odds between 1 and 500,000
sum = 0
for i in range(500000):
    if i % 2 != 0:
        sum += i
print(sum)

#5. Countdown by Fours
for i in range(2022, 1, -4):
    print(i)

#6. Multiples of 4
for i in range(4,41):
    if i % 4 == 0:
        print(i)

# OR
# for i in range(4, 41, 4):
#     print(i)