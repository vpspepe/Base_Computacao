senha_real_1: str = "123456"
senha_real_2: str = "56789"
nivel_de_seguranca: int = 1

if nivel_de_seguranca == 0:
    print("Acesso público! Pode acessar!")

elif nivel_de_seguranca == 1:
    print("Acesso restrito 1! Digite a senha!")
    senha_digitada_1: str = input("Digite a senha 1: ")
    esta_correto: bool = senha_real_1 == senha_digitada_1
    print("Senha está correto? :", esta_correto)
    print("Acesso permitido? :", esta_correto)
    
elif nivel_de_seguranca == 2:
    print("Acesso restrito 2! Digite as senhas!")
    senha_digitada_1: str = input("Digite a senha 1: ")
    senha_digitada_2: str = input("Digite a senha 2: ")
    esta_correto: bool = (senha_real_1 == senha_digitada_1) and (senha_real_2 == senha_digitada_2)
    print("Senha 1 e 2 estão corretas? :", esta_correto)
    print("Acesso permitido? :", esta_correto)
    
print("Fim do programa!")