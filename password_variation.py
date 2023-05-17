import random
import sys, getopt, os

from datetime import datetime
from termcolor import colored

def generate_pass_variations(password: str):
	replacements = {'a': [4, '@'], 'b': [8], 'c': ['('], 'e': [3], 'i': [1, '|', '!'], 'l': [1, '|', '!'], 'o': [0], '0': ['o'], 'g': [9, 6, '&'], 's': [5, '$', 'S'], 't': [7], '_': [' ', '-', '.'], ' ': ['_', '-', '.'], '-': [' ', '_', '.'], '.': [' ', '_', '-'], '5': ['s', 'S', '$'], '8': ['b', 'B']}
	new_pass = password
	generated = []
	for char in password:
		# We have to convert all characters to lowercase.
		if char.lower() in replacements:
			# len() is used to get the length of the list, so it does not go out of bounds when choosing a random item
			new_pass = new_pass.replace(char.lower(), str(replacements[char.lower()][random.randrange(0, len(replacements[char.lower()]))]))
		else:
			new_pass = new_pass.replace(char, random.choice([char.lower(), char.upper()]))
		generated.append(new_pass)
	return set(generated)

def print_help():
	print("Usage: password_variations.py -p <password> [-i <iterations>] [-o <output-file>] [-f <password-file>] [-d <output-directory>]\n")
	print(colored('******************************************************************* For higher uniqueness *******************************************************************', 'green'))
	print(colored('Linux users, use the "awk \'!seen[$0]++\' output.txt > new_output.txt" command to weed out any duplicates after generating variations.', 'yellow'))
	print(colored('Windows users, it is recommended that you install Gawk for Windows from GNUWin32 and add it to the PATH. The same Linux commands almost apply.', 'blue'))
	print(colored('Example: awk "!seen[$0]++" output.txt > new_output.txt', 'blue'))
	print(colored('Or in Powershell, use these commands to \'type output.txt | sort -unique > new_output.txt\' for high precision but lower quantity results', 'blue'))
	print(colored('*************************************************************************************************************************************************************\n', 'green'))
	print("This script generates many possibilities of a given password by replacing characters with numbers and special characters.")
	print("Arguments:")
	print("-p, --password\t\tThe password to generate variations for.")
	print("-i, --iterations\tThe number of variations to generate (default: min=10x, max=40x). x = times repeating the loop which results in repeating the same variations")
	print("-o, --output\t\tThe file to write the generated variations to (optional).")
	print("-f, --password-file\tThe file containing passwords to generate variations for (optional).")
	print("-d, --output-directory\tThe directory to place the generated password variations in (optional). Defaults to the script directory.")
	print("\nExamples:")
	print("password_variations.py -p password")
	print("password_variations.py -p password -i 20")
	print("password_variations.py -p password -o output.txt")
	print("password_variations.py -p password -i 20 -o output.txt -d output_directory/")
	print("password_variations.py -f passwords.txt")
	print("password_variations.py -f passwords.txt -i 20")
	print("password_variations.py -f passwords.txt -o output.txt")
	print("password_variations.py -f passwords.txt -i 20 -o output.txt -d output_directory/")
	print(colored('Side note: If your passwords contain spaces, you must input them in double quotes. This is only if you are not using txt files.\n(Example usage: password_variations.py -p "tH15 c0T1an$ 5PAc3S")', 'magenta'))


def main(argv):
	password = ''
	times_to_iterate = 10
	output_file = ''
	password_file = ''
	output_directory = os.path.dirname(os.path.abspath(__file__))

	try:
		opts, args = getopt.getopt(argv, "hp:i:o:f:d:", ["password=", "iterations=", "output=", "password-file=", "output-directory="])
	except getopt.GetoptError:
		print(
			'generate_password_variations.py -p <password> [-i <iterations>] [-o <output-file>] [-f <password-file>] [-d <output-directory>] -h for help')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print_help()
			sys.exit()

		elif opt in ("-p", "--password"):
			password = arg

		elif opt in ("-i", "--iterations"):
			times_to_iterate = int(arg)
			if times_to_iterate > 40:
				print('defaulting max iteration to 40')
				times_to_iterate = 40

		elif opt in ("-o", "--output"):
			output_file = arg

		elif opt in ("-f", "--password-file"):
			password_file = arg

		elif opt in ("-d", "--output-directory"):
			output_directory = arg


	if password_file:
		with open(password_file, 'r') as file:
			passwords = file.readlines()

		for password in passwords:
			password = password.strip()
			for i in range(times_to_iterate):
				variations = generate_pass_variations(password)
				output = f"" + "\n".join(variations)

				print(output)

				if output_directory and not os.path.exists(output_directory):
					os.makedirs(output_directory)

				if output_file:
					with open(output_file, 'a') as file:
						file.write(output + '\n')
				else:
					output_file = os.path.join(output_directory, f"variations.txt")
					with open(output_file, 'w') as file:
						file.write(output + '\n')

	else:
		for i in range(times_to_iterate):
			variations = generate_pass_variations(password)
			output = f"" + "\n".join(variations)

			print(output)

			if output_directory and not os.path.exists(output_directory):
				os.makedirs(output_directory)

			if output_file:
				with open(output_file, 'a') as file:
					file.write(output + '\n')
			else:
				output_file = os.path.join(output_directory, f"{password}_{i}.txt")
				with open(output_file, 'w') as file:
					file.write(output + '\n')


if __name__ == '__main__':
	random.seed(datetime.now().timestamp())
	main(sys.argv[1:])
