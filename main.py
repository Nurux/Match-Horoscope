from datetime import date

#Define as caracteristicas da pessoa
class Person():
    def __init__(self, name, age, date, signo, elemento):
        self.name = name
        self.age = age
        self.nasc_date = date
        self.signo = signo
        self.element = elemento

#Cria lista de pessoas  
class Dados():
    lista_dados = []

    def lista(self, objeto): 
        self.lista_dados.append(objeto)
        print('Dados cadastrados')

#Relaiza o cadastro da pessoa
def cadastro():
    while True:
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
        data = str(input('Digite sua data de nascimento (dia/mês/ano): '))
        sig = designar_signo(data)
        elemento = designar_elemental(sig)

        if verificar_idade(data, idade) == True:
            pessoa = Person(nome, idade, data, sig, elemento)

            adicionar = Dados()
            adicionar.lista(pessoa)

            option = str(input('Deseja fazer um novo cadastro? (Y/N)'))

            if option.lower() == 'y':
                continue

            if option.lower() == 'n':
                break    
        else:
            print('Verifique a idade informada e tente novamente')

#Verifica idade da pessoa
def verificar_idade(data, idade):
    time = date.today().strftime('%d/%m/%Y')
    data_nascimento = int(data[6:10])
    data_atual = int(time[6:10])

    idade_real = data_atual - data_nascimento 
        
    if idade+1 < idade_real:
        return False
    
    return True

#Define o signo da pessoa
def designar_signo(data):
    dia = int(data[0:2])
    mes = int(data[3:5])

    if mes == 1:
        if dia >= 21:
            sig = "Aquário"
        if dia <= 20:
            sig = "Capricórnio" 

    if mes == 2:
        if dia >= 19:
            sig = "Peixes"
        if dia <= 18:
            sig = "Aquário"

    if mes == 3:
        if dia >= 21:
            sig = "Áries"
        if dia <= 20:
            sig = "Peixes"

    if mes == 4:
        if dia <= 20:
            sig = "Áries"
        if dia >= 21:
            sig = "Touro"
    
    if mes == 5:
        if dia <= 20:
            sig = "Touro"
        if dia >= 21: 
            sig = "Gêmeos"
    
    if mes == 6:
        if dia <= 20:
            sig = "Gêmeos"
        if dia >= 21:
            sig = "Câncer"

    if mes == 7:
        if dia <= 22:
            sig = "Câncer"
        if dia >= 23:
            sig = "Leão"
    
    if mes == 8:
        if dia <= 22:
            sig = "Leão"
        if dia >= 23:
            sig = "Virgem"
    
    if mes == 9:
        if dia <= 22:
            sig = "Virgem"
        if dia >= 23:
            sig = "Libra"
    
    if mes == 10:
        if dia <= 22:
            sig = "Libra"
        if dia >= 23:
            sig = "Escorpião"
    
    if mes == 11:
        if dia <= 21:
            sig = "Escorpião"
        if dia >= 22:
            sig = "Sargitário"

    if mes == 12:
        if dia <= 21:
            sig = "Sargitário"
        if dia >= 22:
            sig = "Capricórnio"
    
    return sig

#Define o elemnto do signo
def designar_elemental(signo):
    if signo == 'Áries' or  signo == 'Sargitário' or  signo == 'Leão':
        elemento = 'Fogo'
    elif signo == 'Touro' or signo == 'Virgem' or signo == 'Capricórnio':
        elemento = 'Terra'
    elif signo == 'Gêmeos' or signo == 'Libra' or signo == 'Aquário':
        elemento = 'Ar'
    elif signo == 'Câncer' or signo == 'Escorpião' or signo == 'Peixes':
        elemento = 'Água'
    
    return elemento

#Mostra a lista de pessoas cadastradas
def consultar(pessoa):
    pessoa = Dados()
    cont = 0

    while cont < len(pessoa.lista_dados):
        ilust_person = pessoa.lista_dados[cont]
        print('-'*20)
        print(f'Nome: {ilust_person.name}')
        print(f'Idade: {ilust_person.age}')
        print(f'Dat.Nasc: {ilust_person.nasc_date}')
        print(f'Signo: {ilust_person.signo}')
        print(f'Elemento: {ilust_person.element}')
        print('-'*20)

        cont += 1

#Busca e verifica as pessoas a serem selecionadas
def relacionar(pessoa):
    cont = 0
    pessoa = Dados()
    content = False
    i = 0
    content2 = False
    
    name_input = str(input('Digite o nome da primeira pessoa a ser relacionada: '))

    while cont < len(pessoa.lista_dados):
        person = pessoa.lista_dados[cont]
        
        if person.name == name_input:
            print(f'{person.name} foi encontrada com sucesso!')

            content = True
            cont = len(pessoa.lista_dados)
        
        cont += 1
    
    if content == False:
        print(f'O nome {name_input} não foi encontrado!')
    
    if content == True:
        name_input2 = str(input(f'Digite o nome da pessoa a ser relacionada com {name_input}: '))

        while i < len(pessoa.lista_dados):
            person2 = pessoa.lista_dados[i]

            if person2.name == name_input2:
                print(f'{person2.name} foi encontrada com sucesso!')
                        
                content2 = True
                i = len(pessoa.lista_dados)
                    
            i += 1

    if content2 == False:
        print(f'O nome {name_input2} não foi encontrado!')
    
    if content and content2 == True:
        calcular(person, person2)

#Calcula o nivel de match das pessoas selecionadas
def calcular(person, person2):
   if person.element == person2.element:
        print(f'{person.name} e {person2.name} Deram Match!!!')
   else:
        print(f'Infelizmente {person.name} com {person2.name} não deram match ;-;')
        print('--'*20)
        print(f'Mas não fique assim signos de elemento {person.element} não costumam se dar bem com o signo de {person2.signo}\nProcure novas experiencias  :)')

#inicio
def main():
    op = 0

    while(op != 4):
        print('-' *20)
        print('HOROSCOPO')
        print('-' *20)
        print('1) Cadastro')
        print('2) Consulta')
        print('3) Calcular')
        print('4) Sair')

        op = int(input())

        if op == 1:
            pessoa = cadastro()
    
        if op == 2:
            consultar(pessoa)
        
        if op == 3:
            relacionar(pessoa)


if __name__ == '__main__':
    main()