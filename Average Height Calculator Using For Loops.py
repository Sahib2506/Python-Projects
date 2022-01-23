student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
for height in student_heights:
  total_heights += height
  
strenght = 0
for n in student_heights:
  strenght +=1

average = round(total_heights/strenght)

print(f"The average height of the students is {average}")




