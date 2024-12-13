a = input('Did you buy an item from the store?("yes or no"): ')

price = 250
aprice = price + (12.3 / 100) * price
ap = aprice - (0.052 / 100) * aprice

if a.lower() == "yes":
	print ('Name of the item: Coke') 
	print ('Price of the item: '  ,price,)
	amount = eval(input('Total of amount given: '))

	age = int(input('What is your age: '))

	if age >= 60:
		print("")
		print (f"Total Price: {price}, Plus 12.3% Tax")
		print ('Total: ' , aprice,)
		print (' You will get a discount of 5.2%, your total purchase is ', ap,)

	elif age <=59:
		print ("The total amount of you purchase is", aprice,)
else:
	print ('Please buy our productssssssss')

		

