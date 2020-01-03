"""
Author:         Oliver Eder Espinosa Meneses
Title:          checkmypass.py
Description:    This is a tool that checks if a password has ever been hacked.
                The program uses the API from https://haveibeenpwned.com/ to search in several data bases and find out
                how many times the password has been hacked.
                Password Hash
                The API uses the sha1 algorithm to hash the password, then it uses the key anonymity technique that only
                takes the first five characters of the hash and look in the data bases for all the hash passwords that
                have the same first characters. Once the API give a response with all the hash passwords, the program
                search with the rest of the hash if the password has ever been pwned. This way, the API is never going
                to know our full hash.
                Pwned Passwords
                    Pwned Passwords are 555,278,657 real world passwords previously exposed in data breaches. This exposure
                    makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other
                    accounts. They're searchable online below as well as being downloadable for use in other online systems.
                    Read more about how HIBP protects the privacy of searched passwords.
                Password reuse and credential stuffing
                    Password reuse is normal. It's extremely risky, but it's so common because it's easy and people aren't
                    aware of the potential impact. Attacks such as credential stuffing take advantage of reused credentials
                    by automating login attempts against systems using known emails and password pairs.

                Way to use
                    Execute in the console the file checkmypass.py and as parameters the path and the name of some files
                    like in the example:
                        python checkmypass.py file.txt file1.txt
                    Each file must the contain passwords separated by a new line or "\n", if the password has ever been
                    hacked it will show a massage like this "password was fount 10109 times... you should probably
                    change the password", otherwise, it will show Aldebaran.01 was NOT found. Carry on!
"""

import requests
import hashlib
import sys
from pathlib import Path


def request_api_data(query_char):
    """
    This function sends the query_char to the pwnedpasswords API and gets the response
    :param query_char:
    :return: res
    """
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res= requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again")
    return res


def get_password_leaks_cont(hashes, hash_to_check):
    """
    Splits the hashes and find out how many times does each password has been hacked
    :param hashes:
    :param hash_to_check:
    :return: count
    """
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    """
    Checks the password if it exists in te API response
    :param password:
    :return:
    """
    """
    :param password: 
    :return: 
    """
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5char, tail = sha1password[:5] , sha1password[5:]
    response = request_api_data(first_5char)
    return get_password_leaks_cont(response, tail)


def read_file(file):
    """
    Reads the files from the arguments and sends every line to the API
    :param file:
    :return:
    """
    with open(file) as my_file:
        for line in my_file.readlines():
            password = line.split("\n")
            count = pwned_api_check(password[0])
            if count:
                print(f"{password[0]} was fount {count} times... you should probably change the password")
            else:
                print(f"{password[0]} was NOT found. Carry on!")



def main(args):
    for file in args:
        input_p = Path(file)
        if input_p.exists():
            read_file(file)
        else:
            print("El archivo no existe")
    return "done!"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))




