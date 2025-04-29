import rahti_improved, os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to the DNA Cryptography Demonstration!')
    print()

    while True:
        print('Select an algorithm using the respective number.')
        print('(1) Rahti Algorithm')
        print('(2) Exit program.')
        number = str(input())

        match number:
            case '1':
                rahti_demonstration()
            case '2':
                print('We appreciate your time here!')
                break
            case _:
                print('Input not recognized!')

def rahti_demonstration():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You have selected the Rahti Algorithm.')
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


if __name__ == "__main__":
    main()