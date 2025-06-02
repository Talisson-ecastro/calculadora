# CABEÇALHO
data_atual=$(date +"%Y-%m-%d %H:%M")
echo -e 'CALCULADORA' $data_atual
echo -e 'CALCULADORA' $data_atual >> mmc.txt

read -p "Olá, seja bem-vindo. Qual o seu nome, por favor? " nome
nome=${nome^}
local_mmc="/home/talisson/modulo1/linux/mmc.txt"
echo -e "\nOlá" ${nome}", aproveite todos os recursos da calculadora. \nTodos os cálculos serão armazenados em $local_mmc. Obrigado\n"
echo -e "\nOlá" ${nome}", aproveite todos os recursos da calculadora. \nTodos os cálculos serão armazenados em $local_mmc. Obrigado\n" >> mmc.txt

# executa a calculadora
echo -e "\nCÁLCULO 01 - " >> mmc.txt
echo -e "\nCÁLCULO 01 - "
python3 calculadora.py
echo -e

MMC_01()
{
	read -p "Quer realizar novo cálculo? Para SIM, digite 1; Para sair digite qualquer outra tecla.  " repetir
	echo -e
	if [ $repetir == "1" ]; then
		echo -e "\nNOVO CÁLCULO"
		echo -e "\nNOVO CÁLCULO" >> mmc.txt
		python3 calculadora.py
	else
		echo -e "Obrigado, volte sempre"
	fi
}

MMC_01

nano $local_mmc
