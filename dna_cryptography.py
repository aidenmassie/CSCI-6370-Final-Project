import rahti_improved, raj, Karimi, os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to the DNA Cryptography Demonstration!')
    print()

    while True:
        print('Select an algorithm using the respective number.')
        print('(1) Symmetric Stream Cipher')
        print('(2) Symmetric Block Cipher')
        print('(3) Symmetric Key Generation')
        print('(4) Exit program.')
        number = str(input())

        match number:
            case '1':
                raj_demonstration()
            case '2':
                rahti_demonstration()
            case '3':
                karimi_demonstration()
            case '4':
                print('We appreciate your time here!')
                break
            case _:
                print('Input not recognized!')

def rahti_demonstration():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You have selected the Symmetric Stream Cipher Algorithm.')
    key = None
    plaintext = None
    ciphertext = None

    while True:
        print('Select an option using the respective number.')
        print('(1) Generate key.')
        print('(2) Generate ciphertext.')
        print('(3) Generate plaintext.')
        print('(4) Exit demonstration.')
        number = str(input())

        match number:
            case '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                key = rahti_improved.rahti_key_generation_improved()
                print('Your newly generated key is: {}.'.format((key)))

                if not ciphertext == None:
                    print('Alert! Reseting current ciphertext! Please generate a new ciphertext.')
                    ciphertext = None
            case '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                if key == None:
                    print('You need to generate a key first!')
                else:
                    while True:
                        plaintext = input('Input a message text: ')
                        try:
                            ciphertext = rahti_improved.rahti_encryption_improved(plaintext,key)
                            print('Your newly encrypted ciphertext is: {}.'.format((ciphertext)))
                            break
                        except:
                            print('Error! Plaintext exceeds 64 characters!')
            case '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                if key == None:
                    print('You need to generate a key first!')
                elif ciphertext == None:
                    print('You need to generate a ciphertext first!')
                else:
                    plaintext_1 = rahti_improved.rahti_decryption_improved(ciphertext,key)
                    print('Your newly decrypted plaintext is: {}.'.format((plaintext_1)))
            case '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Returning to main menu!')
                break
            case _:
                print('Input not recognized!')

def raj_demonstration():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You have selected the Symmetric Block Cipher Algorithm.')
    key = None
    plaintext = None
    ciphertext = None

    while True:
        print('Select an option using the respective number.')
        print('(1) Generate key.')
        print('(2) Generate ciphertext.')
        print('(3) Generate plaintext.')
        print('(4) Exit demonstration.')
        number = str(input())

        match number:
            case '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                key = raj.raj_key_generation()
                print('Your newly generated key is: {}.'.format((key)))

                if not ciphertext == None:
                    print('Alert! Reseting current ciphertext! Please generate a new ciphertext.')
                    ciphertext = None
            case '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                if key == None:
                    print('You need to generate a key first!')
                else:
                    while True:
                        plaintext = input('Input a message text: ')
                        try:
                            ciphertext = raj.raj_encryption(plaintext,key)
                            print('Your newly encrypted ciphertext is: {}.'.format((ciphertext)))
                            break
                        except:
                            print('Error! Plaintext exceeds 64 characters!')
            case '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                if key == None:
                    print('You need to generate a key first!')
                elif ciphertext == None:
                    print('You need to generate a ciphertext first!')
                else:
                    plaintext_1 = raj.raj_decryption(ciphertext,key)
                    print('Your newly decrypted plaintext is: {}.'.format((plaintext_1)))
            case '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Returning to main menu!')
                break
            case _:
                print('Input not recognized!')

def karimi_demonstration():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You have selected the Symmetric Key Generation Algorithm.')
    key = None
    plaintext = None
    ciphertext = None

    while True:
        print('Select an option using the respective number.')
        print('(1) Generate keys.')
        print('(2) Generate ciphertext.')
        print('(3) Generate plaintext.')
        print('(4) Exit demonstration.')
        number = str(input())

        match number:
            case '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                password = input('Input a password (in binary, 0s and 1s): ')
                key = Karimi.generate_keys(password)
                print('Your newly generated keys are: {}.'.format((key)))

                if not ciphertext == None:
                    print('Alert! Reseting current ciphertext! Please generate a new ciphertext.')
                    ciphertext = None
            case '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                if key == None:
                    print('You need to generate a key first!')
                else:
                    while True:
                        plaintext = input('Input a message text: ')
                        try:
                            ciphertext = Karimi.encrypt_message(plaintext,key)
                            print('Your newly encrypted ciphertext is: {}.'.format((ciphertext[1])))
                            break
                        except:
                            print('Error! Plaintext exceeds 64 characters!')
            case '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                if key == None:
                    print('You need to generate a key first!')
                elif ciphertext == None:
                    print('You need to generate a ciphertext first!')
                else:
                    plaintext_1 = Karimi.decrypt_message(ciphertext[0],key)
                    print('Your newly decrypted plaintext is: {}.'.format((plaintext_1)))
            case '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Returning to main menu!')
                break
            case _:
                print('Input not recognized!')

if __name__ == "__main__":
    main()