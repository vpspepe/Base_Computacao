usuarios = []
senhas = []

while True:
    usuario = input('Digite o nome do usuário que quer cadastrar: ')
    senha = input('Digite a senha do usuário que quer cadastrar: ')
    
    usuarios.append(usuario)
    senhas.append(senha)
    
    parar = input('Deseja parar de cadastrar? (s/n) ') == 's'
    if parar:
        break
    
for i in range(len(usuarios)):
    print(f'Usuário: {usuarios[i]} - Senha: {senhas[i]}')
    
while True:
    usuario = input('Digite o nome do usuário que quer deletar: ')
    
    for i in range(len(usuarios)):
        if usuario == usuarios[i]:
            usuarios.pop(i)
            senhas.pop(i)
            break
    
    parar = input('Deseja parar de deletar? (s/n) ') == 's'
    if parar:
        break
    
for i in range(len(usuarios)):
    print(f'Usuário: {usuarios[i]} - Senha: {senhas[i]}')
    
usuario_login = input('Digite o nome do usuário que deseja logar: ')
senha_login = input('Digite a senha do usuário que deseja logar: ')

for i in range(len(usuarios)):
    if usuario_login == usuarios[i] and senha_login == senhas[i]:
        print('Usuário logado com sucesso!')
        break
