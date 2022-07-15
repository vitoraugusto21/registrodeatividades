Tema: Feira de Graduação da UEFS 
Utilizando os conhecimentos adquiridos quanto a estruturas de controle, estruturas de dados, arquivos e  modularização, faça um programa utilizando a linguagem Python, que realize as seguintes funcionalidades: 
1. Disponibilizar um menu com 5 opções: Registrar Atividade, Exibir Atividades, Mostrar Relatório, Gravar  Programação e Sair, e permitir ao usuário a escolha de uma opção;
2. A opção Registar Atividade deve solicitar os seguintes dados de uma atividade a ser realizada na Feira de  Graduação: título da atividade, dia da semana (as atividades ocorrem de segunda-feira até sexta-feira durante  uma única semana), horário (as atividades só podem ocorrer entre 8h e 20h e duram 1 hora), tipo de atividade  (oral, oficina, pôster, laboratório); e guardar os dados de toda atividade cadastrada em uma estrutura de dados  em memória; 
3. A opção Exibir Atividades deve exibir em tela uma lista de todas as atividades ordenadas pelo título da  atividade;
4. A opção Mostrar Relatório deve exibir um relatório indicando 
quantas atividades acontecerão em cada um dos dias; 
quantas atividades de cada tipo estão programadas; 
quais atividades estão no mesmo dia e horário, exibindo dia e horário seguidos pelos demais dados destas  atividades.
5. A opção Gravar Programação deve criar um arquivo texto ‘programação.txt’ (se já existir, deve sobrescrever)  contendo a programação da Feira de Graduação, com as atividades divididas por dia da semana e horário, no  seguinte formato: (1,0) 
Dia X, Horário Y: 
Título atividade A, Tipo Atividade A 
Título atividade B, Tipo Atividade B 
... 
Dia Z, Horário W: 
Título atividade C, Tipo Atividade C 
Título atividade D, Tipo Atividade D 
6. A opção Sair, antes de interromper a execução do programa, deve realizar o armazenamento dos dados de  todas as atividades em um arquivo; 
7. Ao iniciar o programa, antes da exibição do menu, se existir o arquivo com dados armazenados, os dados de  todas as atividades armazenadas no arquivo devem ser lidos para a mesma estrutura de dados indicada no  item 2;