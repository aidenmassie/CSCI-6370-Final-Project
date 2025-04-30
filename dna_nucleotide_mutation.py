#DNA Encryption


##KEY GENERATION
#convert bits into DNA
def dna_encode(binary):
    
    #convert to DNA
    dna = ''

    for i in range(0, len(binary), 2):
        if binary[i] == '0' and binary[i+1] == '0':
            dna += 'A'
        elif binary[i] == '0' and binary[i+1] == '1':
            dna += 'G'
        elif binary[i] == '1' and binary[i+1] == '0':
            dna += 'T'
        elif binary[i] == '1' and binary[i+1] == '1':
            dna += 'C'
    
    #if the length of dna is less than 60, replicate from the start
    print (f"Length of DNA: {len(dna)}")

    if len(dna) < 60:
        for i in range(0,len(dna)):
            dna += dna[i]
            if len(dna) >= 60:
                break
    
    #last element of dna
    last = dna[-1]

    #if the length of dna is not a multiple of 3, replicate the last element until it is
    while len(dna)%3 != 0:
        dna += last

        
    return dna
    
#combines two DNA strands
def Anneal(key):

    new_key = key
    for char in key:
        if char == 'A':
            new_key += 'T'
        elif char == 'T':
            new_key += 'A'
        elif char == 'C':
            new_key += 'G'
        elif char == 'G':
            new_key += 'C'
    
    return new_key

##transcription of DNA to mRNA
def transcription(dna):

    mRNA = ''
    for char in dna:
        if char == 'A':
            mRNA += 'A'
        elif char == 'T':
            mRNA += 'U'
        elif char == 'C':
            mRNA += 'C'
        elif char == 'G':
            mRNA += 'G'
    
    return mRNA

##mutation of DNA to mRNA
def mutation(dna):

    stop_codon = ['UAA', 'UAG', 'UGA']

    mutation_map = [
    ('CAG', 'UAG'),
    ('CGA', 'UGA'),
    ('UGG', 'UGA'),
    ('GAU', 'GUU'),
    ('GAG', 'GUG'),
    ('GCC', 'ACC')
    ]

    codons = [dna[i:i+3] for i in range(0, len(dna), 3)]

    for i in range(len(codons)):
        for rule in mutation_map:
            if codons[i] == rule[0]:
                codons[i] = rule[1]
                break
    
    dna = '' 
    for codon in codons:
        dna += codon


    keys = [[]]
    stops = 0

    #check for stop codon
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        keys[0] += codon
        if stops > 0:
            for i in range(1, stops+1):
                keys[i] += codon
        if codon in stop_codon:
            stops += 1
            keys.append([])
            continue
    
    #turn the keys into a string
    for i in range(len(keys)):
        keys[i] = ''.join(keys[i])

    return keys
    
##ENCRYPTION
def dna_decode(dna):
    binary = ''
    for char in dna:
        if char == 'A':
            binary += '00'
        elif char == 'G':
            binary += '01'
        elif char == 'T' or char == 'U':
            binary += '10'
        elif char == 'C':
            binary += '11'
    
    return binary

def binary_blocks(binary):
    
    #split the binary string into blocks of 8 bits
    blocks = []
    for i in range(0, len(binary), 8):
        block = binary[i:i+8]
        blocks.append(block)
    
    #if the last block is not 8 bits, pad it with 0s
    if len(blocks[-1]) < 8:
        blocks[-1] = blocks[-1].ljust(8, '0')
    
    return blocks

def encryption(blocks, message):

    ciphertext = []

    for plain in message:
        m = plain
        for i, key_block in enumerate(blocks, start=1):
            m = (m << i) 
            for k in key_block:
                m ^= k
        ciphertext.append(m)
     
    return ciphertext

def decryption(blocks, ciphertext):
    decrypted_message = []
    for cm in ciphertext:
        m = cm
        for i, key_block in reversed(list(enumerate(blocks, start=1))):
            for k in reversed(key_block):
                m ^= k
            m = (m >> i) 
        decrypted_message.append(m)
    return decrypted_message

def main():
    #get the key
    key = input("Enter the key: ")
    
    #encode to DNA
    dna = dna_encode(key)
    
    #combine the DNA strands
    new_key = Anneal(dna)

    new_key = transcription(new_key)

    keys = mutation(new_key)

    for i in range(len(keys)):
        keys[i] = dna_decode(keys[i])

    #convert to binary
    for i in range(len(keys)):
        keys[i] = binary_blocks(keys[i])


    message = input("Enter the message: ")

    #turn message into binary using ascii
    message = ''.join(format(ord(i), '08b') for i in message)

    #break message into blocks of 8 bits
    message_blocks = []
    #pad the message with 0s if it is not a multiple of 8
    if len(message)%8 != 0:
        message = message.ljust(len(message)+8-len(message)%8, '0')
    for i in range(0, len(message), 8):
        block = message[i:i+8]
        message_blocks.append(block)

    #turn everything into binary
    for i in range(0,len(message_blocks)):
        message_blocks[i] = int(message_blocks[i],2)

    for i in range(0,len(keys)):
        for j in range(0,len(keys[i])):
            keys[i][j] = int(keys[i][j],2)


    ciphertext = encryption(keys, message_blocks)
    #convert the ciphertext to binary
    ciphertext_binary = ''
    for i in range(0,len(ciphertext)):
        ciphertext_binary += format(ciphertext[i], '08b')
    print(f"Ciphertext: {ciphertext}")

    input("Press enter to decrypt the message")

    decrypted_message = decryption(keys, ciphertext)
    print(f"Decrypted message: {decrypted_message}")

    decrypted_message = ''.join(format(i, '08b') for i in decrypted_message)
    decrypted_message = ''.join(chr(int(decrypted_message[i:i+8], 2)) for i in range(0, len(decrypted_message), 8))
    print(f"Decrypted message: {decrypted_message}")

main()