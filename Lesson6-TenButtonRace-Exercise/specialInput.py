# No shabang in modules

"""
	Defines several input functions for inputting numbers and non-string data.
"""
def int_input(prompt):
	"""
		Allows the user to input an integer and asks for another try if a non-integer
	"""
	
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			return answer
		except ValueError:
			print(" That's not an integer dude. Try again!")
def name_input(prompt):	
	"""
		Allow the user to input their name and call their nickname
	"""
	name = raw_input(prompt)
	if len(name) >= 10:
		name = name[:10]
		
	print("I will give you a nick name,your name is:" + name + ".")
	return name






def float_input(prompt):
	while True:
		answer = raw_input(prompt)
		try:
			answer = float(answer)
			return answer
		except ValueError:
			print("That's not a real number. Try again")