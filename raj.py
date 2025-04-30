import random
from itertools import product

def raj_encryption(plaintext,key):
    if len(plaintext) > 256:
        raise ValueError('Plaintext message exceeds 256 length.')
    elif len(plaintext) < 256:
        plaintext += '.'*(256 - len(plaintext))
    
    key_sub = []

    for k in key:
        binary = ''
        for i in k:
            match i:
                case 'A':
                    binary = ''.join((binary,'00'))
                case 'C':
                    binary = ''.join((binary,'01'))
                case 'G':
                    binary = ''.join((binary,'10'))
                case 'T':
                    binary = ''.join((binary,'11'))
        key_sub.append(int(binary,2))
    
    m_a = ['{0:08b}'.format((ord(plaintext[i])+ key_sub[i]) % 256) for i in range(256)]

    m_b = []

    for b in m_a:
        nucleotide = ''
        for i in range(0,8,2):
            match b[i:i+2]:
                case '00':
                    nucleotide = ''.join((nucleotide,'A'))
                case '01':
                    nucleotide = ''.join((nucleotide,'C'))
                case '10':
                    nucleotide = ''.join((nucleotide,'G'))
                case '11':
                    nucleotide = ''.join((nucleotide,'T'))
        m_b.append(nucleotide)

    ciphertext = [key.index(m_b[i]) for i in range(256)]

    return ciphertext

def raj_key_generation():
    nucleotides = ['A','C','G','T']
    key = [''.join(comb) for comb in product(nucleotides, repeat=len(nucleotides))]
    random.shuffle(key)

    return key

def raj_decryption(ciphertext,key):
    ciphertext = [ciphertext[i] for i in range(256)]
    m_b = [key[ciphertext[i]] for i in range(256)]

    m_a = []

    for a in m_b:
        bin = ''
        for i in a:
            match i:
                case 'A':
                    bin = ''.join((bin,'00'))
                case 'C':
                    bin = ''.join((bin,'01'))
                case 'G':
                    bin = ''.join((bin,'10'))
                case 'T':
                    bin = ''.join((bin,'11'))
        m_a.append(bin)
    
    key_sub = []

    for k in key:
        binary = ''
        for i in k:
            match i:
                case 'A':
                    binary = ''.join((binary,'00'))
                case 'C':
                    binary = ''.join((binary,'01'))
                case 'G':
                    binary = ''.join((binary,'10'))
                case 'T':
                    binary = ''.join((binary,'11'))
        key_sub.append(int(binary,2))
    
    plaintext = ''.join([chr((int(m_a[i],2) - key_sub[i]) % 256) for i in range(256)])
    
    return plaintext

key = raj_key_generation()
ciphertext = raj_encryption('Thequickbrownfoxjumpedoverthelazydog',key)
print(raj_decryption(ciphertext,key))