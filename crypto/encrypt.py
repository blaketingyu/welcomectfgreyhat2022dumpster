import base64

flag = "REDACTED"

def encryption(text, key):
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))


# Layer 1
flag = encryption(flag, 3) # Refer to line 5

# Layer 2
flag_bytes = flag.encode('ascii')
base64_bytes = base64.b64encode(flag_bytes)
flag = base64_bytes.decode('ascii')

print("Encrypted Flag: ", flag)



