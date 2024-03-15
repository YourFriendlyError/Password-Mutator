# Password variations generator

This is a simple, and basic, Python script that will generate the many possibilities of a given password or passwords from a given list. This script can be useful instead of having to rely on the 'crunch' tool which only generates basic lists and or appending at the end of a password.


# Use cases
<u>For educational purposes only.</u> Use this in CTF tournaments, create wordlists, red teaming if you have permissions, or hashcat.

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
\$> python3 password_variations.py -p password -o variations_example.txt

pAssword

passWoRD

pAsSWoRd

PaSswOrd

paSSwOrd

pASsWOrD

paSSwOrD

pasSwORD

PasSWOrd

pAsSWORd

passWORd

paSswOrd

pAssWord

pASsWord

PAsswOrd

PasSwoRd

PASSWord

pasSWorD

pasSWORD

pASSworD

...