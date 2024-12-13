a = eval(input("Enter your Prelim grade: "))
b = eval(input("Enter your Midterm grade: "))
c = eval(input("Enter your Semi-Final grade: "))
d = eval(input("Enter your Final grade: "))
e = eval(input("Enter your Quiz grade: "))
f = eval(input("Enter your Project grade: "))

fg = (a * 0.15) + (b * 0.15) + (c * 0.15) + (d * 0.15) + (e * 0.15) + (f * 0.25)

aa = fg

print ("")

print ("Total Grades", aa,)
if fg >= 75:
	print("")
	print ("Congrats")

else:
	print("")
	print("KYS")