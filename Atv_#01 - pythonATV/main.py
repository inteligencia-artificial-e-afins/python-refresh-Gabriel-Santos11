def rearrange_string(s: str) -> str:
    return ''.join(c.lower() for c in s if not c.isdigit())[::-1]

teclado = input("Digite uma Palavra/Frase: ")

print("Resultado:", rearrange_string(teclado))