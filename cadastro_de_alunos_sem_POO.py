'''
Sem programação orientada à objetos (POO)
'''
import csv
import pandas as pd

def salvar(alunos, arquivo = 'registro de aluno fap 2024.csv'):
    with open('registro de aluno fap 2024.csv', 'a', encoding='utf8', newline='') as arquivo:
        writer = csv.writer(arquivo)

        #Caso o arquivo já tenha sido criado este código comentado irá ser reescrito .
        #writer.writerow(('nome', 'matricula', 'curso','telefone','email'))

        for aluno in alunos:
            writer.writerow((aluno['nome'],str(aluno['matricula']),aluno['curso'],aluno['telefone'],aluno['email']))

    print('Cadastrado(a).')

def acessar(nome = '', matricula = '0', mudanca = '',tipo = '', arquivo = 'registro de aluno fap 2024.csv', email = ''):
    with open(arquivo, mode='r', encoding='utf8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    nome = nome.lower()
    matricula = str(matricula)

    print('Entradas: {nome},{matricula}')
    print('Comparar com: {row[0]}, {row[1]}')
    for row in rows:

        row[0] = row[0].lower()
        row[1] = str(row[1])


        #Para ver as comparações
        print(f'Entradas: {nome},{matricula}, mudanca tipo:{tipo}')
        print(f'Comparar com: {row[0]}, {row[1]}')




        if row[0] == nome and row[1] == matricula and tipo == '1':
            row[0] = mudanca   #---------------------Mudar o nome
            print('\nMudança tipo 1 realizada')

        elif row[0] == nome and tipo == '2':
            row[1] = mudanca #---------------------Mudar o numero de matrícula, precisa do email
            print('Mudança realizada')

        elif row[0] == nome and row[1] == matricula and tipo == '3':
            row[2] = mudanca #---------------------Mudar o curso
            print('Mudança realizada')

        elif row[0] == nome and row[1] == matricula and tipo == '4':
            row[3] = mudanca #---------------------Mudar telefone
            print('Mudança realizada')

        elif row[0] == nome and row[1] == matricula and tipo == '5':
            row[4] = mudanca #---------------------Mudar o email
            print('\nMudança de email realizada!')

        elif row[0] == nome and row[1] == matricula and tipo == '6':
            #---------------------'DELETAR DADOS'-------------------------

            row[0] = '' #----------trocando o argumanto por 'nada'
            row[1] = ''
            row[2] = ''
            row[3] = ''
            row[4] = ''

            print('Deleção realizada...')

    # Escrever os dados de volta no arquivo CSV, reecreve todas as informações
    with open(arquivo, mode='w', encoding='utf8',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def aluno_info(nome = 'teste da silva', matricula = '20230044'):
    with open(arquivo, mode='r', encoding='utf8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Alterar o valor
    i = 0

    for row in rows:
        nome_pesquisa = row[0].strip().lower()

        '''print('\nLinha:',i)
        print('valores de row[0]:',row[0])
        print('valores de row[1]:',row[1])
        print('Entradas nome e matricula:',nome,'-',matricula)
        print('Entrdads tratadas:',nome.lower(), 'comparador:',nome_pesquisa.lower())'''

        if nome_pesquisa == nome.lower() and row[1] == str(matricula):
            print('\nRow', row,'Indicie:',i)
            print(f'\n\nDados gerais de {nome.title()}:')
            print('------------------------------------------')
            print('Nome:',row[0])
            print('Matrícula:',row[1])
            print('Curso:',row[2])
            print('Telefone:',row[3])
            print('Email:',row[4],)
            print('------------------------------------------', sep = '')
        i+=1
    i=0
def informacao():
    print('\n---------------------------------------------')
    print('OPÇÕES-MENU')
    print('---------------------------------------------')
    print('[1] Para ver dados do(a) aluno(a) ')
    print('[2] Para cadastrar um novo(a) aluno(a)')
    print('[3] Para deletar/alterar perfil do(a) aluno(a)')
    print('[0] Para sair ')
    print('---------------------------------------------')

def informacao2():
    print('\n---------------------------------------------')
    print('ALTERAR/DELETAR:')
    print('---------------------------------------------')
    print('[1] para alterar o nome do aluno: ')
    print('[2] para alterar matricula')
    print('[3] para alterar curso')
    print('[4] para alterar telefone')
    print('[5] para alterar email')
    print('[6] Para deletar todos os dados de um aluno(a): ')
    print('[0] para voltar ao menu principal')
    print('---------------------------------------------')

def informacao3():
    print('\n------------------------------------------')
    print('BUSCAR DADOS:')
    print('---------------------------------------------')
    print('[0] para ir ao menu principal: ')
    print('[1] para ver informações gerais')



cadastrar = True
alunos = []
i = 0

while cadastrar:

    #usuário digite o nome, curso, matrícula e outras informações relevantes do aluno.
    informacao()
    escolha = input('digite:')

#----------------------Para econtrar um aluno----------------

    if escolha == '1' :

        while True:
            informacao3()
            escolher = input('[2] para ver dados do(a) aluno(a) em específico: ')
            print('---------------------------------------------')
            arquivo = 'registro de aluno fap 2024.csv'
            df = pd.read_csv(arquivo)
            df = list(df)

            if escolher == '1':
                print('\nTabela: Alunos - Matrícula - Email:')

                # Ler os dados do arquivo CSV
                with open('registro de aluno fap 2024.csv', mode='r', encoding='utf8') as file:
                    reader = csv.reader(file)
                    rows = list(reader)

                for row in rows:
                    print('',row[0],'   -   ',row[1], '  -  ',row[4])

            elif escolher == '2':
                nome_pesquisa = input('Insira o nome do aluno(a): ')
                matricula_pesquisa = int(input('Insira a matricula: '))
                aluno_info(nome = nome_pesquisa, matricula = str(matricula_pesquisa))

            else:
                print(f'Opção inválida! Você digitou: {escolher}')


            if escolher == '0':
                break    #Saindo do while seculdário

        else:
            print(f'Opção inválida! você digitou {escolher}')
#-------------------------------------------------------------

#-----------------------Cadstrar-------------------------------

    elif escolha == '2':
        #cadastrar aluno(a)
        print('\n------------------------------------------------------')
        print('CADASTRAR NOVO ALUNO')
        print('------------------------------------------------------')
        aluno_nome = input('Insira o nome: ').title()
        aluno_matricula = int(input('Insira o número de matricula: '))
        aluno_curso = input('Curso do aluno(a): ').title().rstrip()  #Tratar: adicionar opções
        aluno_telefone = input('Insira o número de telefone: ')   #tratar: verificar se nenhuma caractere str foi digitada
        aluno_email = input('Email do aluno(a): ')

        aluno = {
                    'nome': aluno_nome,
                    'matricula': aluno_matricula,
                    'curso': aluno_curso,
                    'telefone': aluno_telefone,
                    'email':aluno_email,
            }

        print('\n\nTudo ok, aluno(a) cadastrado(a) com sucesso!')

        alunos.append(aluno) # adicionando o aluno na lista
        salvar(alunos) #salvando alunos na planilhas
        alunos.remove(aluno) #retirando aluno da lista, para poder adicionar outro

#---------------------------------------------------------------------
#-----------------------#Continuar Cadastrando alunos-----------------
        while True:
            mais_cadastro = input('\nDeseja cadastrar outro aluno ou realizar outra aperação (s/n)?').lower().rstrip()
            if mais_cadastro == 's':
                break
            elif mais_cadastro == 'n':
                cadastrar = False  #Saindo dos dois laços/finalizando programa
                break
            else:
                print('\nPor favor, digite "n" se não quiser cadastrar outro aluno(a)\nou "s" se quiser cadastar.')

#--------------------------Alterar/ deletar---------------------------

    elif escolha == '3':
        while True:
            informacao2()
            opcao = input('digite: ')

            #writer.writerow(('nome', 'matricula', 'curso','presenca(s)','email','informacoes','notas'))
            #def acessar(nome, matricula, mudanca,tipo, arquivo = 'registro de aluno fap 2024.csv'):

            #alterar o nome
            if opcao == '1':
                nome = input('\n Insira o nome a ser alterado ')
                matricula = int(input('Insira o número de matrícula '))
                novo_nome = input('Insira o novo nome ')

                acessar(nome = nome, mudanca = novo_nome, tipo = opcao, matricula = matricula)

            #alterar o numero de matricula
            elif opcao == '2':
                mudanca = int(input('\n Insira a matricula ser alterado'))
                email_confirmar = input('Insira o email do aluno(a), por favor ')
                matricula_mudanca = int(input('Insira o novo número de matrícula '))
                novo_nome = input('Insira o nome do aluno(a) ')

                acessar(mudanca = matricula_mudanca, tipo = opcao, email = email_confirmar)

            #alterar o curso
            elif opcao == '3':
                nome = input('\nInsira o nome do aluno(a): ')
                matricula = input('\n Insira o numero de matricula: ')
                curso = input('Insira o novo curso: ')

                acessar(mudanca = curso, tipo = opcao, nome = nome, matricula = str(matricula))#Corrigir cada interação

            #alterar o telefone
            elif opcao == '4':
                nome = input('\n Insira o nome do(a) aluno(a): ')
                matricula = input('Insira o numero de matricula: ')
                numero = input('Insira o novo número: ')

                acessar(nome = nome, matricula = str(matricula), mudanca = numero )

            #alterar email
            elif opcao == '5':
                nome = input('\n Insira o nome do(a) aluno (a): ')
                matricula = input('Insira o numero de matricula: ')
                email = input('Insira o novo email: ')
                acessar(nome = nome, matricula = str(matricula), mudanca = email, tipo = opcao)

            elif opcao == '6':
                nome = input('Insira o nome do(a) aluno(a) para apagar od dados: ')
                matricula = input('Insira o numero de matricuila do(a) aluno(a): ')

                acessar(mudanca = '', nome = nome, matricula = str(matricula), tipo = opcao)

            elif opcao == '0':  # sair do laço
                break

            else:
              print(f'Opção inválida! Você digitou {opcao}')

    elif escolha == '0':
        cadastrar = False  # finaliza o programa.
    else:
        print(f'Opção inválida! você digitou "{escolha}"')
try:
    '''
    print('\nTudo ok!')
    print('------------------------------------------')
    print('Dados do aluno:')
    print('------------------------------------------')
    print('Nome do aluno:',alunos[0]['nome'])
    print('Matrícula do aluno:',alunos[0]['matricula'])
    print('Curso do aluno:',alunos[0]['curso'])
    print('Presenças do aluno:',alunos[0]['presencas'])
    print('Email do aluno:',alunos[0]['email'])
    print('Informações do aluno:',alunos[0]['informacoes'])
    print('Notas do aluno:',alunos[0]['notas'])
'''
except:
    print('Nada cadastrado!')
  
finally:
        print('\nTudo ok!')


