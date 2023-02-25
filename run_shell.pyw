from urllib.request import hashlib
import pyfiglet


T = "Hash Cracker"
ASCII_art_1 = pyfiglet.figlet_format(T,font='alphabet')
print(ASCII_art_1)

while True:
    print("")
    print("Enter Type of Hash to be Cracked (Select 3 to quit the script)!\n 1. SHA1 Hash \n 2. MD5 Hash \n 3. Quit ")
    print("") 
    k = int(input("> "))
    
    if (k== 1):
        passFound = False
        sha1hash  = input("Input the SH1 hash to crack. \n> ")
        
        with open("file.txt","r") as file:
            for guess in file:
                hashedGuess = hashlib.sha1(bytes(guess.strip(), 'utf-8')).hexdigest()
                if hashedGuess.upper()==sha1hash.upper():
                
                    print("The password is ",str(guess))
                    passFound = True
                    break
                elif hashedGuess != sha1hash:
                    print("Password guess ", str(guess), "does not match, trying next .... ")
                    
                    
        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k==2):
        passFound = False
        md5hash = input("Please input the MD5 hash to crack.\n>")

        with open ("file.txt","r") as file:
             for guess in file:
                hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()
                if hashedGuess.upper() == md5hash.upper():
                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != md5hash:
                    print("Password guess ",str(guess)," does not match, trying next...")
        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k==3):
        quit()
            
                
    