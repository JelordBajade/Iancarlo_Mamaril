gold = 0

a = input ("Enter your name: ")
b = input ('Did you mine today("yes" or "no")? ')

if b.lower() == "yes":
	gold += 10
	print ("Hello" , a , " your gold amount is " , gold,)

else:
	print (gold)
	print ("Hello" , a , " your gold amount is " , gold,)

