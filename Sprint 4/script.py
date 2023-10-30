import hashlib

while True:
    input_str = input("Digite uma string para calcular o hash (ou digite 'exit' para retornar ao início): ")
    if input_str == 'exit':
        break
    hash_object = hashlib.sha1(input_str.encode())
    hex_dig = hash_object.hexdigest()
    print(f"Hash SHA-1 da string '{input_str}': {hex_dig}")
