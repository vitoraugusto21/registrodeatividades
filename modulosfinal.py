#/*******************************************************************
#Autor: Vitór Augusto Novaes de Jesus
#Componente Curricular: MI - ALGORITMOS
#Concluído em: 15/07/2022
#Declaro que este código foi elaborado por mim de forma individual e não contém 
#nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e 
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código 
#de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
#código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#**********************************************************************/
import os

def menu(): # MODULARIZAÇÃO DO MENU
    print("""
    ----------DIGITE A OPÇÃO DESEJADA---------
    [A] Registrar atividade
    [B] Exibir Atividades
    [C] Mostrar Relatório
    [D] Gravar programação
    [E] Sair""")

def registrarAtividade(dicio): #FUNÇÃO PARA O REGISTRO DE ATIVIDADES    
    atividade = input('Titulo da atividade: ').upper()    
    if dicio.get(atividade): #VERIFICAR SE JÁ EXISTE ATIVIDADE CADASTRADA
        print('Atividade já adicionada')
    else:        
        dia = input('Dia que a atividade ocorrerá(Segunda a sexta): ').upper().replace('Ç','C')
        while dia != 'SEGUNDA' and dia != 'TERCA' and dia != 'QUARTA' and dia != 'QUINTA' and dia != 'SEXTA':
            print('Dia invalido, por favor insira um dia da semana de segunda a sexta.')
            dia = input('Dia que a atividade ocorrerá(Segunda a sexta): ').upper().replace('Ç','C')
        try:
            horario = float(input('Horario da atividade(8 as 20:00): '))
            while horario > 20 or horario < 8:
                print('Horario invalido, por favor selecione um horario entre 8:00 e 20:00 horas. ')
                horario = float(input('Horario da atividade(8 as 20:00): '))
        except ValueError:
            horario = float(input('Horario da atividade(8 as 20:00): '))
            while horario > 20 or horario < 8:
                print('Horario invalido, por favor selecione um horario entre 8:00 e 20:00 horas. ')
                horario = float(input('Horario da atividade(8 as 20:00): '))
        tipo = input('Tipo de atividade(oral,oficina,pôster ou laboratório): ').upper().replace('Ô','O')
        while tipo != 'ORAL' and tipo != 'OFICINA' and tipo != 'POSTER' and tipo != 'LABORATORIO':
            print('Tipo de atividade invalida, por afvor insira uma atividade valida.')
            tipo = input('Tipo de atividade(oral,oficina,pôster ou laboratório): ').upper().replace('Ô','O').replace('Ó','O')
        dicio[atividade] = {} # ARMAZENAMENTO DE ATIVIDADES E SUAS CARACTERISTICAS
        dicio[atividade]['TITULO'] = atividade     
        dicio[atividade]['DIA'] = dia
        dicio[atividade]['HORARIO'] = horario
        dicio[atividade]['TIPO'] = tipo
 
def exibirAtividade(registro): #FUNÇÃO PARA EXIBIR ATIVIDADES
    for atividade in registro: #PERCORRER DICIONARIOS E EXIBIR ATIVIDADES E CARACTERISTICAS
        print(f"""
        {'-'*5} ATIVIDADE: {registro[atividade]['TITULO']}{'-'*5}
        DIA: {registro[atividade]['DIA']}
        HORARIO: {registro[atividade]['HORARIO']}
        TIPO DE ATIVIDADE: {registro[atividade]['TIPO']}""") 

def contador(lista, valor): #CONTADOR PARA REGISTRAR ATIVIDADES COM HORARIOS REPETIDOS
    cont = 0
    for c in lista:
        if c == valor:
            cont += 1
    return cont
def diasehorarios(dia,registro): #FUNCAO PARA MODULARIZAR EXIBIÇÃO DE ATIVIDADES QUE OCORREM NO MESMO HORARIO
    horas = []
    for i in range(8,21):
        for key in registro:                                
            if registro[key]['DIA'] == dia and registro[key]['HORARIO'] == i:
                horas.append(registro[key]['HORARIO'])
                if contador(horas,i) > 1 :
                    print(f"""
                    AS {i} HORAS OCORRERÁ:""")
                    for key in registro:  
                        if registro[key]['HORARIO'] == i:                
                            print(f"{registro[key]['TITULO']} DO TIPO {registro[key]['TIPO']}")                     

def relatorio(registro): #FUNÇÃO PARA MOSTRAR RELATORIO DE ATIVIDADES
    quantAtividadesseg = 0
    quantAtividadester = 0
    quantAtividadesqua = 0
    quantAtividadesqui = 0
    quantAtividadessex = 0
    quantOral = 0
    quantOficina = 0
    quantPoster = 0
    quantLab = 0      
    for atividade in registro:
        if registro[atividade]['DIA'] == 'SEGUNDA':
            quantAtividadesseg += 1
        elif registro[atividade]['DIA'] == 'TERCA':
            quantAtividadester += 1
        elif registro[atividade]['DIA'] == 'QUARTA':
            quantAtividadesqua += 1
        elif registro[atividade]['DIA'] == 'QUINTA':
            quantAtividadesqui += 1
        elif registro[atividade]['DIA'] == 'SEXTA':
            quantAtividadessex += 1

        if registro[atividade]['TIPO'] == 'ORAL':
            quantOral += 1
        elif registro[atividade]['TIPO'] == 'OFICINA':
            quantOficina += 1
        elif registro[atividade]['TIPO'] == 'POSTER':
            quantPoster += 1
        elif registro[atividade]['TIPO'] == 'LABORATORIO':
            quantLab += 1

        
    print(f"""
    ACONTECERÁ NA SEGUNDA: {quantAtividadesseg} ATIVIDADES 
    ACONTECERÁ NA TERÇA: {quantAtividadester} ATIVIDADES 
    ACONTECERÁ NA QUARTA: {quantAtividadesqua} ATIVIDADES  
    ACONTECERÁ NA QUINTA: {quantAtividadesqui} ATIVIDADES 
    ACONTECERÁ NA SEXTA: {quantAtividadessex} ATIVIDADES 
    ------------------------------------------------------
    SERÁ REALIZADO:
    {quantOral} ATIVIDADES ORAIS
    {quantOficina} ATIVIDADES DE OFICINA
    {quantPoster} ATIVIDADES DE POSTER
    {quantLab} ATIVIDADES DE LABORATÓRIO
    ------------------------------------------------------
    """)
    
    
    print('-----ATIVIDADES DA SEGUNDA COM HORARIOS IGUAIS-----')

    
    diasehorarios('SEGUNDA',registro)
    print('-----ATIVIDADES DA TERÇA COM HORARIOS IGUAIS-----')
    
    diasehorarios('TERCA',registro)
    print('-----ATIVIDADES DA QUARTA COM HORARIOS IGUAIS-----')
   
    diasehorarios('QUARTA',registro)
    print('-----ATIVIDADES DA QUINTA COM HORARIOS IGUAIS-----')
    
    diasehorarios('QUINTA',registro)
    print('-----ATIVIDADES DA SEXTA COM HORARIOS IGUAIS-----')

    diasehorarios('SEXTA',registro)  

def gravar(registro): # FUNÇÃO PARA GRAVAR ATIVIDADES
    arquivo = open('programação.txt','w',encoding= 'utf-8')    
    for atividade in registro:
        if registro[atividade]['DIA'] == 'SEGUNDA':
            arquivo = open('programação.txt','a',encoding= 'utf-8')
            arquivo.write(f"""
            SEGUNDA FEIRA as {registro[atividade]['HORARIO']}:
            """)
            arquivo.close()
            for atividades in registro:
                arquivo = open('programação.txt','a',encoding= 'utf-8')
                arquivo.write(f"""{registro[atividades]['TITULO']}, {registro[atividades]['TIPO']}
                """)
            arquivo.close()
        elif registro[atividade]['DIA'] == 'TERCA':
            arquivo = open('programação.txt','a',encoding= 'utf-8')
            arquivo.write(f"""
            TERÇA FEIRA as {registro[atividade]['HORARIO']}:
            """)
            arquivo.close()
            for atividades in registro:
                arquivo = open('programação.txt','a',encoding= 'utf-8')
                arquivo.write(f"""{registro[atividades]['TITULO']}, {registro[atividades]['TIPO']}
                """)
            arquivo.close()

        elif registro[atividade]['DIA'] == 'QUARTA':
            arquivo = open('programação.txt','a',encoding= 'utf-8')
            arquivo.write(f"""
            QUARTA FEIRA as{registro[atividade]['HORARIO']}
            """)
            arquivo.close()
            for atividades in registro:
                arquivo = open('programação.txt','a',encoding= 'utf-8')
                arquivo.write(f"""{registro[atividades]['TITULO']}, {registro[atividades]['TIPO']}
                """)
            arquivo.close()

        elif registro[atividade]['DIA'] == 'QUINTA':
            arquivo = open('programação.txt','a',encoding= 'utf-8')
            arquivo.write(f"""
            QUINTA FEIRA as{registro[atividade]['HORARIO']}
            """)
            arquivo.close()
            for atividades in registro:
                arquivo = open('programação.txt','a',encoding= 'utf-8')
                arquivo.write(f"""{registro[atividades]['TITULO']}, {registro[atividades]['TIPO']}
                """)
            arquivo.close()

        elif registro[atividade]['DIA'] == 'SEXTA':
            arquivo = open('programação.txt','a',encoding= 'utf-8')
            arquivo.write(f"""
            SEXTA FEIRA as{registro[atividade]['HORARIO']}
            """)
            arquivo.close()
            for atividades in registro:
                arquivo = open('programação.txt','a',encoding= 'utf-8')
                arquivo.write(f"""{registro[atividades]['TITULO']}, {registro[atividades]['TIPO']}
                """)
            arquivo.close()
def gravardados(dicio): #FUNÇÃO ARMAZENADORA DE DADOS PARA USO FUTURO DO PROGRAMA
    with open('dadosprogramacao.txt','w',encoding='utf-8') as arquivo:
        arquivo.write(f'{dicio}')

