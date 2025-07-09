point1 = float(input("Enter your exam1 point:"))
point2 = float(input("Enter your exam2 point:"))
point3 = float(input("Enter your exam3 point:"))
avg = (point1 + point2 +point3) / 3
print("Your's average score is:", avg)
if(avg > 95):
    print("Congratulation!")
else:
    print("You did well!" , avg)


