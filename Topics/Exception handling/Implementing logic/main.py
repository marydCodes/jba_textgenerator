try:
    name, surname = input().split()
    print("Welcome to our party,", name, surname)
except ValueError:
    print("You need to enter exactly 2 words. Try again!")

# ValueError: not enough values to unpack (expected 2, got 1)
# ValueError: too many values to unpack (expected 2)