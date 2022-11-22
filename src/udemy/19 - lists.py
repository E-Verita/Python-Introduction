computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse"]

for part in computer_parts:
    print(part)
print()
print(computer_parts[0])
print(computer_parts[0:3])
print()
print(computer_parts[-1])

print("*"*20)
computer_parts[3] = "trackball"
print(computer_parts)

other_parts = ["chair", "desk"]
computer_parts[1:3] = other_parts
print(computer_parts)