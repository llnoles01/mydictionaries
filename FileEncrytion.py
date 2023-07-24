codes = {'a':'%','T':'@','b':'*','c':'&','B':'!'}

input_file = 'info_security-1.txt'
output_file = 'encrypted.txt'

with open (input_file, 'r') as file:
    content = file.read()

encrypted_content = ''

for char in content:
    if char in codes:
        encrypted_content += codes[char]

    else:
        encrypted_content += char

with open(output_file,'w') as file:
    file.write(encrypted_content)