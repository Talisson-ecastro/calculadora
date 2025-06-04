# CALCULADORA
Script de calculadora com programação em python

Como executar o arquivo .sh?
Baixe o arquivo, logo em seguida abra um terminal wsl e localize a pasta onde o arquivo foi salvo. Estando nela, digite "./calculadora.sh" e pressione enter.

# SOBRE O CÓDIGO EM PYTHON
Este código em python realiza cálculos utilizando as 4 operações matemáticas básicas, adição, subtração, multiplicação e divisão.
O código apresenta duas funções, a primeira é para a escolha do operador, e a segunda para que sejam definos os números que serão calculados. Antes, porém, é aberto um arquivo .txt, o qual será uma memória do cálculo realizado. A segunda função, calculadora (), chama a primeira, operador(). Num primeiro momento nas variáveis calc_1 e calc_2 são armazenadas as entradas dos dois números que serão calculados. Em seguida, a função operador () é chamada, sendo armazenado na variável "operação" a entrada do sinal de operador escolhido (+, -, / ou *). Para tanto, usou-se uma condicionais if, elif e else. Após receber o retorno da função operador(), a função calculadora() prossegue com o cálculo utilizando os dois números armazenados e o resultado da função operador(). Este cálculo é armezanado no arquivo .txt gerado.  
