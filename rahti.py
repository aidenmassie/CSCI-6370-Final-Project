import random

def rahti_encryption(plaintext, key):
    if len(plaintext) > 64:
        raise ValueError('Plaintext message exceeds 64 length.')
    elif len(plaintext) < 64:
        plaintext += '.'*(64 - len(plaintext))

    m = [[ord(plaintext[i+8*j]) for i in range(8)] for j in range(8)]

    m_t = [[m[j][i] for j in range(8)] for i in range(8)]

    key_sub = [key[i:i+4] for i in range(0,len(key),4)]
    k_t = [[None for _ in range(8)] for _ in range(8)]

    for i, x in enumerate(key_sub):
        for j, y in enumerate(x):
            match y:
                case 'A':
                    k_t[i][2*j] = 0
                    k_t[i][2*j+1] = 0
                case 'C':
                    k_t[i][2*j] = 0
                    k_t[i][2*j+1] = 1
                case 'G':
                    k_t[i][2*j] = 1
                    k_t[i][2*j+1] = 0
                case 'T':
                    k_t[i][2*j] = 1
                    k_t[i][2*j+1] = 1
    
    m_k = [[m_t[i][j]+k_t[i][j] for j in range(8)] for i in range(8)]

    m_r = m_k

    for i in range(8):
        for j in range(8-i):
            m_r[i].insert(0,m_r[i].pop())
    
    temp = zip(*m_r[::-1])
    m_c = [list(x) for x in temp]

    for i in range(8):
        for j in range(8-i):
            m_c[i].append(m_c[i].pop(0))

    for i in range(3):
        temp = zip(*m_c[::-1])
        m_c = [list(x) for x in temp]

    c = [[chr(m_c[i][j]) for j in range(8)] for i in range(8)]

    ciphertext = ''
    for row in c:
        for col in row:
            ciphertext = ''.join((ciphertext,col))

    return ciphertext

def rahti_key_generation():
    k_t = [[random.randrange(0, 128) % 2 for _ in range(8)] for _ in range(8)]

    key = ''

    for row in k_t:
        for i in range(0, len(row),2):
            match str(row[i]) + str(row[i+1]):
                case '00':
                    key = ''.join((key,'A'))
                case '01':
                    key = ''.join((key,'C'))
                case '10':
                    key = ''.join((key,'G'))
                case '11':
                    key = ''.join((key,'T'))
    return key

def rahti_decryption(ciphertext, key):
    m_c = [[ord(ciphertext[i+8*j]) for i in range(8)] for j in range(8)]
    
    temp = zip(*m_c[::-1])
    m_r = [list(x) for x in temp]

    for i in range(8):
        for j in range(8-i):
            m_r[i].insert(0,m_r[i].pop())

    for i in range(3):
        temp = zip(*m_r[::-1])
        m_r = [list(x) for x in temp]
    
    m_k = m_r

    for i in range(8):
        for j in range(8-i):
            m_k[i].append(m_k[i].pop(0))

    key_sub = [key[i:i+4] for i in range(0,len(key),4)]
    k_t = [[None for _ in range(8)] for _ in range(8)]

    for i, x in enumerate(key_sub):
        for j, y in enumerate(x):
            match y:
                case 'A':
                    k_t[i][2*j] = 0
                    k_t[i][2*j+1] = 0
                case 'C':
                    k_t[i][2*j] = 0
                    k_t[i][2*j+1] = 1
                case 'G':
                    k_t[i][2*j] = 1
                    k_t[i][2*j+1] = 0
                case 'T':
                    k_t[i][2*j] = 1
                    k_t[i][2*j+1] = 1

    m_t = [[m_k[i][j]-k_t[i][j] for j in range(8)] for i in range(8)]

    m = [[chr(m_t[j][i]) for j in range(8)] for i in range(8)]

    plaintext = ''
    for row in m:
        for col in row:
            plaintext = ''.join((plaintext,col))

    return plaintext