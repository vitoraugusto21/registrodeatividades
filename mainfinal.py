from logging.config import dictConfig
from modulosfinal import exibirAtividade, registrarAtividade,gravar,relatorio,menu

registro = {}
opcao = ''
while opcao != 'SAIR    ':
    menu()
    opcao = input('Opção desejada: ').upper()
    if opcao == 'A':
        registrarAtividade(registro)
        print(registro)
    elif opcao == 'B':
        exibirAtividade(registro)
    elif opcao == 'C':
        relatorio(registro)
    elif opcao == 'D':
        gravar(registro)
    elif opcao == 'E':
        opcao == 'SAIR'