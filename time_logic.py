print("Enter total seconds")
total_seconds = input()
total_seconds = int(total_seconds)

hours = total_seconds // 3600

remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:")
print(hours)

print("Minutes:")
print(minutes)

print("Seconds:")
print(seconds)