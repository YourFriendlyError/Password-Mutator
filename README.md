# Password variations generator

This is a simple, and basic, Python script that will generate the many possibilities of a given password or passwords from a given list. This script can be useful instead of having to rely on the 'crunch' tool which only generates basic lists and or appending at the end of a password.


# Use cases
<u>For educational purposes only.</u> Use this in CTF tournaments, create wordlists, red teaming if you have permissions, or hashcat.

## Extra installation

**This is optional and the script will work fine without it.**

Windows users, please install GAWK from <a href="https://www.gnu.org/software/gawk/" target="_blank">GNU.org</a> and add it to the path. This tool will come in handy to weed out any duplicates after generating password variations.

## Usage

Arguments:

-p, --password         The password to generate variations for.

-i, --iterations       The number of variations to generate (default: min=10x, max=40x) x = times repeating the loop which results in repeating the same variations.

-o, --output           The file to write the generated variations to (optional).

-f, --password-file    The file containing passwords to generate variations for (optional).

-d, --output-directory The directory to place the generated password variations in (optional). Defaults to the script directory.

Examples:

password_variations.py -p password

password_variations.py -p password -i 20

password_variations.py -p password -o output.txt

password_variations.py -p password -i 20 -d output_directory/

password_variations.py -f passwords.txt

password_variations.py -f passwords.txt -i 20

password_variations.py -f passwords.txt -o output.txt

password_variations.py -f passwords.txt -i 20 -d output_directory/

# Variations output example
## Non-unique
\$> python3 password_variations.py -p password -i 20 -o variations_example.txt


P@\$\$W0RD

P@\$\$W0rd

P@\$\$W0Rd

P@\$\$W0rd

P@\$\$W0RD

P@\$\$W0Rd

P@\$\$W0RD

P@\$\$W0Rd

P@\$\$W0rd

P@\$\$W0RD

P@\$\$W0rd

P@\$\$W0Rd

P@\$\$W0RD

P@\$\$W0rd

P@\$\$W0Rd

P@\$\$W0RD

P@\$\$W0rd

P@\$\$W0Rd

P@\$\$W0rd

P@\$\$W0Rd

P@\$\$W0rd

P@\$\$W0RD

P@\$\$W0rd

...

## Unique
*Only after you have generated and saved your password variations*

\$> awk '!seen[$0]++' variations_example.txt > unique_variations.txt

\$> cat new_output.txt

password

p4SSw0Rd

p4SSw0rd

p4SSword

p4ssword

p4SSw0RD

p@ssword

p@55w0rd

p@55word

p@55w0rD

P@SSw0rD

P@ssword

P@SSword

P@SSw0rd

Password

p4SSW0Rd

p4SSWord

p4SSW0rd

P@\$\$Word

P@\$\$word

P@\$\$W0Rd

P@\$\$W0RD

P@\$\$W0rd

P455w0rD

P455word

P455w0rd

P4ssword

P455w0Rd

p4\$\$Word

p4\$\$W0rd

p4\$\$word

p4\$\$W0rD

P4\$\$word

P4\$\$w0rd

P4\$\$w0rD

P4\$\$w0Rd

P@55word

P@55Word

P@55W0rd

P@SSW0rd

P@SSWord

P4\$\$Word

P4\$\$W0rd

P455W0rd

P455W0Rd

P455Word

P@55W0Rd

P@55W0RD

p@\$\$word

p@\$\$W0rd

p@\$\$Word

P455W0RD

P@SSW0rD

p4\$\$w0rD

p4\$\$w0rd

p@SSW0rD

p@SSW0rd

p@SSWord

p@SSword

p455W0Rd

p455word

p455Word

p455W0rd

p455W0RD

p455W0rD

P4SSW0Rd

P4SSW0RD

P4SSWord

P4SSW0rd

p@SSw0rd

p@\$\$W0RD

p@\$\$W0Rd

P4$$W0Rd

p@55Word

p@55W0Rd

p@55W0rd

p455w0rd

p455w0RD

p455w0Rd

p@SSW0Rd
