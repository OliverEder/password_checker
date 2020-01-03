# password_checker
This is a tool that uses the API from https://haveibeenpwned.com/ to search in several data bases and find out how many times the password has been hacked.

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
