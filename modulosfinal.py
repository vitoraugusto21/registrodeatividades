import os

def menu():
    print("""
    ----------DIGITE A OPÇÃO DESEJADA---------
    [A] Registrar atividade
    [B] Exibir Atividades
    [C] Mostrar Relatório
    [D] Gravar programação
    [E] Sair""")

def registrarAtividade(dicio):    
    atividade = input('Titulo da atividade: ').upper()    
    if dicio.get(atividade):
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
        dicio[atividade] = {}
        dicio[atividade]['TITULO'] = atividade     
        dicio[atividade]['DIA'] = dia
        dicio[atividade]['HORARIO'] = horario
        dicio[atividade]['TIPO'] = tipo
 
def exibirAtividade(registro):
    for atividade in registro:
        print(f"""
        {'-'*5} ATIVIDADE: {registro[atividade]['TITULO']}{'-'*5}
        DIA: {registro[atividade]['DIA']}
        HORARIO: {registro[atividade]['HORARIO']}
        TIPO DE ATIVIDADE: {registro[atividade]['TIPO']}""") 
    
def relatorio(registro):
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
    
def gravar(registro):
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

dicio = {}


