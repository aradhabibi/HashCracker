import hashlib
from os import system as sys


def chap():
    print(
        '''
               ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
            ▄▄█▀▀░░░░░░░░░░░░▀▀█▄▄
          ▄█▀░░░░░░░░░░░░░░░░░░░░▀█▄
         ▄█░░░░░░░░░░░░░░░░░░░░░░░░█▄
        ▄█░░░░░░░░░░░░░░░░░░░░░░░░░░█▄
        █▌░░▐░░░░░░░░░░░░░░░░░░░░▌░░▐█
        █▌░░▐▌░░░░░░░░░░░░░░░░░░▐▌░░▐█
        ▐▌░░█▀░░░░░░░░░░░░░░░░░░▀█░░▐▌
         █▄░░▄▄██▄▄▄░░░░░░▄▄▄██▄▄░░▄█
         ▐▌░█████████░░░░█████████░▐▌
        ▄█░░█████████░░░░█████████░░█▄
        █░░░░▀▀▀▀▀▀▀░▄▄▄▄░▀▀▀▀▀▀▀░░░░█
        ▀█▄▄▄░░░░░░░▄████▄░░░░░░░▄▄▄█▀
             ▀█░░░░░██████░░░░░█▀
              █▄░░░░░░░░░░░░░░▄█
              ▀█▄▄█░▄░▄▄░▄░█▄▄█▀
                 ▀▀▀▀▀▀▀▀▀▀▀▀
        
        By @Arad_HBI
'''
    )


system = input("choose system t/c ?")
if system == 't':
    sys("clear")
    chap()
elif system == 'c':
    sys("cls")
    chap()


while True:
    
    try:
        file_path = 'passlist.txt'
        with open(file_path,'r') as file:
            lines = [line.strip() for line in file]
    except:
        pass

    print('''
    1)Encrypt
    2)Decrypt
    3)Exit
    ''')

    chosemenu = int(input("Menu#>"))

    if chosemenu == 1:#Encrypt
        print("chose encryption method:\nmd5\tsha1\tsha256\nsha512")
        choseencrypt = str(input("Encrypt#>"))
#-----------------------------------md5 encrypt------------------------------------
        if choseencrypt == "md5":

            Md5HashInput = input("md5#>").encode()
            Md5hashCreator = hashlib.md5(Md5HashInput).hexdigest()
            print(Md5hashCreator)
#-----------------------------------sha1 encrypt------------------------------------
        elif choseencrypt == "sha1":

            Sha1HashInput = input("sha1#>").encode()
            Sha1hashCreator = hashlib.sha1(Sha1HashInput).hexdigest()
            print(Sha1hashCreator)
#-----------------------------------sha256 encrypt------------------------------------
        elif choseencrypt == "sha256":

            Sha256HashInput = input("sha256#>").encode()
            Sha256hashCreator = hashlib.sha256(Sha256HashInput).hexdigest()
            print(Sha256hashCreator)
#-----------------------------------sha512 encrypt------------------------------------
        elif choseencrypt == "sha512":

            Sha512HashInput = input("sha512#>").encode()
            Sha512hashCreator = hashlib.sha512(Sha512HashInput).hexdigest()
            print(Sha512hashCreator)


    elif chosemenu == 2:#Decrypt
        print('''
              
ghable harshis esm password list khod ra <passlist.txt> bezarid va daron poshe folder gharardahid''')
        

        print("chose decryption method:\nmd5\tsha1\tsha256\nsha512")
        chosedecrypt = str(input("DEcrypt#>"))

#-----------------------md5 Decrypt------------------
        if chosedecrypt == "md5":

            Md5DecryptInput = input("Decrypt md5#>")

            for passlist in range(len(lines)):

                Md5DecryptCreator = hashlib.md5(lines[passlist].encode()).hexdigest()

                if Md5DecryptCreator == Md5DecryptInput:

                    print(f"word is {lines[passlist]}")
                    break

                else:

                    print(f"word is not {lines[passlist]}")

#-----------------------sha1 Decrypt------------------
        elif chosedecrypt == "sha1":

            Sha1DecryptInput = input("Decrypt sha1#>")

            for passlist in range(len(lines)):

                Sha1DecryptCreator = hashlib.sha1(lines[passlist].encode()).hexdigest()

                if Sha1DecryptCreator == Sha1DecryptInput:

                    print(f"word is {lines[passlist]}")
                    break
                
                else:

                    print(f"word is not {lines[passlist]}")

#-----------------------sha256 Decrypt------------------                    
        elif chosedecrypt == "sha256":

            Sha256DecryptInput = input("Decrypt sha256#>")

            for passlist in range(len(lines)):

                Sha256DecryptCreator = hashlib.sha256(lines[passlist].encode()).hexdigest()

                if Sha256DecryptCreator == Sha256DecryptInput:

                    print(f"word is {lines[passlist]}")
                    break
                
                else:

                    print(f"word is not {lines[passlist]}")

#-----------------------sha512 Decrypt------------------
        elif chosedecrypt == "sha512":

            Sha512DecryptInput = input("Decrypt sha512#>")

            for passlist in range(len(lines)):

                Sha512DecryptCreator = hashlib.sha512(lines[passlist].encode()).hexdigest()

                if Sha512DecryptCreator == Sha512DecryptInput:
                    print(f"word is {lines[passlist]}")
                    break
                
                else:
                    print(f"word is not {lines[passlist]}")

    elif chosemenu == 3:#Exit

        print("good bye!")
        break
    
    else:
        print("wrong page!")
        