print("Exam Grade Calculator")
print()
nt= input("Name of test: ")
print()
pscore= float(input("Maximum possible score : "))
print()
score= float(input("Score recieved in test: "))
print()


per= score / pscore * 100
if per >= 90 and per <= 100:
  print(f"You got {per} % which is a A+")
elif per >= 80 and per <= 89:
  print(f"You got {per} % which is a A")
elif per >= 70 and per <= 79:
  print(f"You got {per} % which is a B")
elif per >= 60 and per <= 69:
  print(f"You got {per} % which is a C")
elif per >= 50 and per <= 59:
  print(f"You got {per} % which is a D")
elif per < 50:
  print(f"You got {per} % which is a U")
else:
  print("invalid")