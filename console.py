'''
Projeto 4: Conversor de Moedas
Versão para console

By: Ravana Pereira de França
'''

#Instalando bibliotecas

#pip install Pillow
#pip install termcolor
#pip install colored

#Importando bibliotecas

from termcolor import colored
import requests
import json

#Função para Converter Moeda


def converter():
  print(
      colored(
          "\nCertifique-se de digitar a moeda corretamente. As opções para conversão são: 'ARS', 'BRL', 'CAD', 'EUR', 'INR', 'JPY', 'TRY','USD'",
          'green'))

  moeda_de = input("\nDigite a moeda de origem: ").upper()
  while moeda_de not in [
      'ARS', 'BRL', 'CAD', 'EUR', 'INR', 'JPY', 'TRY', 'USD'
  ]:
    print(colored("\nMoeda inválida! Tente novamente.", 'red'))
    moeda_de = input("\nDigite a moeda de origem: ").upper()

  else:
    moeda_para = input("\nDigite a moeda de destino: ").upper()

    while moeda_para not in [
        'ARS', 'BRL', 'CAD', 'EUR', 'INR', 'JPY', 'TRY', 'USD'
    ]:
      print(colored("\nMoeda inválida! Tente novamente.", 'red'))
      moeda_para = input("\nDigite a moeda de destino: ").upper()

    else:
      valor = input("\nDigite o valor a ser convertido: ")
      valor = valor.replace(',', '.')
      valor = float(valor)

      while valor <= 0:
        print(colored("\nValor inválido! Tente novamente.", 'red'))
        valor = input("\nDigite o valor a ser convertido:")
        valor = valor.replace(',', '.')
        valor = float(valor)

      else:
        response = requests.get(
            'https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
        dados = json.loads(response.text)
        cambio = dados['rates'][moeda_para]

        resultado = float(valor) * float(cambio)

        if moeda_para == 'USD':
          simbolo = '$'
        elif moeda_para == 'EUR':
          simbolo = '€'
        elif moeda_para == 'INR':
          simbolo = '₹'
        elif moeda_para == 'JPY':
          simbolo = '¥'
        elif moeda_para == 'ARS':
          simbolo = 'A$'
        elif moeda_para == 'TRY':
          simbolo = '₺'
        elif moeda_para == 'CAD':
          simbolo = 'C$'
        else:
          simbolo = 'R$'

        moeda_equivalente = simbolo + "{:,.2f}".format(resultado)

        moeda_equivalente = moeda_equivalente.replace(',', 'temp').replace(
            '.', ',').replace('temp', '.')

        print(colored("\nO valor convertido é:", 'green'), moeda_equivalente)

      print(colored("\nDeseja fazer outra conversão?", 'green'))
      resposta = input("Digite 'S' para sim ou 'N' para não: ").upper()
      if resposta == 'S':
        converter()
      else:
        print(colored("\nObrigado por usar o conversor de moedas!", 'green'))


#Chamando a função
print(colored("Bem-vindo ao conversor de moedas!", 'green'))
converter()
