# Write a program to read seconds and convert them into hours, minutes and seconds.

seconds = int(input("Enter the Time in Seconds : "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{seconds }sec = {hours} hr  {minutes} min  {remaining_seconds} sec")