from .Keytable import keyTable

def decrypt(pBuffer):
    x = 4
    checksumEnc = 0
    checksumDec = 0
    keyResult = 0
    loopiterator = 0
    hashKey = pBuffer[2]
    keyIncrement = keyTable[hashKey * 2] & 0xFF
    buffer_size = len(pBuffer)

    while x < buffer_size:
        checksumEnc += pBuffer[x]
        keyResult = keyTable[((keyIncrement & 0x800000FF) * 2) + 1]
        loopiterator = x & 3
        
        if loopiterator == 0:
            calc = pBuffer[x] - (keyResult << 1)
            res = bytes([calc & 0xFF])
            pBuffer = pBuffer[:x] + res + pBuffer[x+1:]
        elif loopiterator == 1:
            calc = pBuffer[x] + (keyResult >> 3)
            res = bytes([calc & 0xFF])
            pBuffer = pBuffer[:x] + res + pBuffer[x+1:]
        elif loopiterator == 2:
            calc = pBuffer[x] - (keyResult << 2)
            res = bytes([calc & 0xFF])
            pBuffer = pBuffer[:x] + res + pBuffer[x+1:]
        elif loopiterator == 3:
            calc = pBuffer[x] + (keyResult >> 5)
            res = bytes([calc & 0xFF])
            pBuffer = pBuffer[:x] + res + pBuffer[x+1:]
        else:
            pass
        checksumEnc += pBuffer[x]
        keyIncrement += 1
        x += 1
        
    checksumEnc = checksumEnc & 0xFF
    checksumDec = checksumDec & 0xFF
    calc = checksumDec - checksumEnc
    checksum = bytes([calc & 0xFF])
    pBuffer = pBuffer[:3] + checksum + pBuffer[3+1:]
    
    if(pBuffer[3] != (calc & 0xFF)):
        return None
    else:
        return pBuffer