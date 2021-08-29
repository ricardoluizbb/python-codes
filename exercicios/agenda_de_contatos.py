AGENDA = {}

def exibir_contatos():
    if len(AGENDA) > 0:
        for contato in AGENDA:
            buscar_contato(contato)
            print('-' * 30)
    else:
        print('\nA sua agenda está vazia. Adicione alguns contatos!\n')

def buscar_contato(contato):
    try:
        print(f'Nome: {contato}')
        print('Celular:', AGENDA[contato]['celular'])
        print('E-mail:', AGENDA[contato]['email'])
    except KeyError:
        print(f'\nO contato {contato} não existe na agenda.\n')
    except:
        print('\nDesculpe, aconteceu um erro inesperado.\n')

# Verifica se o nome do contato digitado já existe na agenda. Linha 87 e 97 #
def verificando_se_existe(contato):
    if contato in AGENDA:
        return True
    return False

def incluir_contato(contato, celular, email, verificacao_incluir_editar = True):
    AGENDA[contato] = {
        'celular': celular,
        'email': email
    }
# Verificação para retornar a mensagem correta. #
    if verificacao_incluir_editar:
        print(f'\nO contato {contato} foi incluido.\n')
    else:
        print(f'\nO contato {contato} foi editado.\n')

def editar_contato(contato, celular, email):
    incluir_contato(contato, celular, email, verificacao_incluir_editar = False)
    
def deletar_contato(contato):
    try:
        AGENDA.pop(contato)
        print(f'\nO contato {contato} foi deletado.\n')
    except KeyError:
        print(f'\nO contato {contato} não existe na agenda.\n')

# Função que exporta contatos para um arquivo txt #
def exportar_contatos():
    try:
        with open('agenda.txt', 'w') as arquivo:
            arquivo.write('Nome, Celular, E-mail\n')
            for contato in AGENDA:
                celular = AGENDA[contato]['celular']
                email = AGENDA[contato]['email']
                arquivo.write(f'{contato}, {celular}, {email}\n')
        print('\nSua agenda foi exportada com sucesso!\n')
    except Exception as error:
        print('\nDesculpe, aconteceu um erro inesperado.\n')

def imprimir_menu(): 
    print('\n1 - Exibir contatos')
    print('2 - Buscar um contato')
    print('3 - Incluir um contato')
    print('4 - Editar um contato')
    print('5 - Deletar um contato')
    print('6 - Exportar agenda para um arquivo txt')
    print('0 - Fechar agenda\n')

while True:
    imprimir_menu()
    action = (input('Digite o que deseja fazer: '))
    print()

    if action == '1':
        exibir_contatos()

    elif action == '2':
        contato = input('Digite o nome do contato: ')
        print('-' * 30)
        buscar_contato(contato)
        print('-' * 30)

    elif action == '3':
        contato = input('Digite o nome do contato: ')

        if verificando_se_existe(contato):
            print(f'\nO contato {contato} já existe na agenda. Tente adicioná-lo com outro nome ou sobrenome.\n')
        else:
            celular = input('Digite o número do celular do contato: ')
            email = input('Digite o e-mail do contato: ')
            incluir_contato(contato, celular, email)

    elif action == '4':
        contato = input('Digite o nome do contato que deseja editar: ')

        if  verificando_se_existe(contato):
            celular = input('Digite o número do celular do contato: ')
            email = input('Digite o e-mail do contato: ')
            editar_contato(contato, celular, email)
        else:
            print(f'\nO contato {contato} não existe na agenda.\n')
    elif action == '5':
        contato = input('Digite o nome do contato que deseja deletar: ')
        deletar_contato(contato)
    elif action == '6':
        exportar_contatos()
    elif action == '0':
        print('A agenda foi fechada.')
        break
    else:
        print('Por favor, dhigite um comando válido.')