import base64

flag = "Z2h7TnJpNHQ1aW5yeWFzN2FzME1UMF9OX3JOcFM3T31ldFJGNE5kNDBJ"

#decrypt layer 2
flag_bytes = flag.encode('ascii')
base64_bytes = base64.b64decode(flag_bytes)
flag = base64_bytes.decode('ascii')

print("Decrypted Flag: ", flag)