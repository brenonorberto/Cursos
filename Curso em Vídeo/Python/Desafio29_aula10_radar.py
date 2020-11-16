print('\033[33m=\033[m'*12, '\033[1;30mDesafio 28\033[m', '\033[33m=\033[m'*12)
print()
from time import sleep
velocidade = int(input('Digite a velocidade do carro! '))
print('\033[1;33mPROCESSANDO...\033[m')
sleep(1)
if velocidade > 80:
    print()
    print('\033[1;31mVOCÊ FOI MULTADO!\033[m \033[30mpois passou do limite de \033[1;31m80 Km/h\033[m')
    multa = (velocidade - 80) * 7
    print('\033[1;33mCALCULANDO MULTA...\033[m')
    sleep(2)
    print()
    print('\033[30mVocê vai pagar uma multa de \033[1;31mR$ {:.2f}!\033[m'.format(multa))

print()
print('\033[1;32mTenha um bom dia! e dirija com cuidado!!!\033[m')