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

from modulosfinal import exibirAtividade, registrarAtividade,gravar,relatorio,menu,gravardados
import os

cwd = os.getcwd()
if os.path.isfile('dadosprogramacao.txt'): # VERIFICAR ARMAZENAMENTO OU NÃO ARMAZENAMENTO DE DADOS
    arquivo = open('dadosprogramacao.txt','r',encoding='utf-8')
    leitura = arquivo.read()
    registro = eval(leitura)
    arquivo.close        
else:
    registro = {}
    
opcao = ''
while opcao != 'SAIR': # LOOP PARA ESCOLHA DA OPÇÃO DESEJADA PELO USUARIO
    menu()
    opcao = input('Opção desejada: ').upper()
    if opcao == 'A':
        registrarAtividade(registro)        
    elif opcao == 'B':
        exibirAtividade(registro)
    elif opcao == 'C':
        relatorio(registro)
    elif opcao == 'D':
        gravar(registro)
        print('Registro gravado!')
    elif opcao == 'E':
        gravardados(registro)
        opcao = 'SAIR'
    else:
        print('OPÇÃO INCORRETA, TENTE NOVAMENTE.')