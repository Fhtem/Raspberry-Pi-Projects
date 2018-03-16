import json

madness_list = []

def list_compiler(lst):
	print ('Type \'n\' to exit')
	while True:
		inpt = input('Type in Team name: ')
		if inpt == 'n':
			print ('Stopping Program..............')
			break
		else:
			lst.append(inpt)
def clear_list(lst):
	lst = []

def roster_rand(list):
	
with open('madness_list.json', 'r+') as madness_file: 
	
	json.dump(madness_list, madness_file, indent=2)
	
	
