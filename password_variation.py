import random
import sys, getopt, os, itertools

from datetime import datetime
from termcolor import colored


def generate_pass_variations(password: str):
	old_pass = password # Save the old password
	generated = []

	# First we need to set every alphabetical character into an uppercase. Then, do the opposite
	generated.append(password.upper())
	generated.append(password.lower())

	# Next, individually uppercase each character at a time. Do the same for the next loop
	for i in range(len(password)):
		char = password[i]
		if char.isalpha():
			new_pass = password[:i] + char.upper() + password[i + 1:]
			generated.append(new_pass)

	password = password.upper()
	for i in range(len(password)):
		char = password[i]
		if char.isalpha():
			new_pass = password[:i] + char.lower() + password[i + 1:]
			generated.append(new_pass)

	# Mix of capitalizations
	for subset_len in range(1, len(old_pass)):  # Generate subsets of different lengths
		for subset_indices in itertools.combinations(range(len(old_pass)), subset_len):
			new_pass = old_pass.lower()
			for idx in subset_indices:
				new_pass = new_pass[:idx] + new_pass[idx].upper() + new_pass[idx + 1:]
			generated.append(new_pass)

	return generated

def print_help():
	print("Usage: password_variations.py -p <password> [-i <iterations>] [-o <output-file>] [-f <password-file>] [-d <output-directory>]\n")
	print("This script generates the many possibilities of a given password by replacing characters with numbers and special characters.")
	print("Arguments:")
	print("-p, --password\t\tThe password to generate variations for.")
	print("-o, --output\t\tThe file to write the generated variations to (optional).")
	print("-f, --password-file\tThe file containing passwords to generate variations for (optional).")
	print("-d, --output-directory\tThe directory to place the generated password variations in (optional). Defaults to the script directory.")
	print("\nExamples:")
	print("password_variations.py -p password")
	print("password_variations.py -p password -o output.txt")
	print("password_variations.py -p password -o output.txt -d output_directory/")
	print("password_variations.py -f passwords.txt")
	print("password_variations.py -f passwords.txt -o output.txt")
	print("password_variations.py -f passwords.txt -o output.txt -d output_directory/")
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
			variations = set(generate_pass_variations(password)) # Proper use of set(). Removes duplicate passwords
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
		variations = set(generate_pass_variations(password))
		output = f"" + "\n".join(variations)

		print(output)

		if output_directory and not os.path.exists(output_directory):
			os.makedirs(output_directory)

		if output_file:
			with open(output_file, 'a') as file:
				file.write(output + '\n')
		else:
			output_file = os.path.join(output_directory, f"{password}.txt")
			with open(output_file, 'w') as file:
				file.write(output + '\n')


if __name__ == '__main__':
	random.seed(datetime.now().timestamp())
	main(sys.argv[1:])
