import sys

people = dict()

while True:

	command = input()

	command = command.split()

	if command[0].lower() == "print":
		try:
			print(people[command[1].lower()][command[2].lower()])
			
		except:

			try:
				print(people[command[1].lower()])
			except:
				print("INVALID PERSON")

	elif command[0].lower() == "add":

		tempDict = {command[1].lower() : {}}

		people.update(tempDict)

		try:
			people[command[1].lower()].update({command[2].lower() : command[3].lower()})

		except:
			pass

	elif command[0].lower() == "detail":

		people[command[1].lower()].update({command[2].lower() : command[3].lower()})

	elif command[0].lower() == "del":

		try:

			del(people[command[1].lower()][command[2].lower()])

		except:

			try:

				del(people[command[1].lower()])

			except:

				print("INVALID PERSON")

	elif command[0].lower() == "edit":

		people[command[1]][command[2]] = command[3].lower()

	elif command[0].lower() == "people":

		for x in list(people.keys()): print(x)

	elif command[0].lower() == "keys":

		for x in list(people[command[1]].keys()): print(x)

	elif command[0].lower() == "save":

		with open("people.txt", "w") as f:

			f.write(str(people))

	elif command[0].lower() == "load":

		with open("people.txt", "r") as f:

			people = eval(f.read())

	elif command[0].lower() == "save&exit":

		with open("people.txt", "w") as f:

			f.write(str(people))

		sys.exit()

	elif command[0].lower() == "exit":

		sys.exit()

	elif command[0].lower() == "help":

		print("""
			COMMANDS:

			print *person* optional*detailName*

			add *person name* optional*detailName* optional*attribute*

			detail *person* *detailName* *attribute*

			edit *person* *detailName* *newAttribute*

			keys *person*

			people

			del *person* optional*detailName*

			exit

			save&exit

			save

			load
			""")


	else:
		print("INVALID SYNTAX")