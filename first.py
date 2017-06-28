
altura = float(input('Qual sua altura?: '))

peso = float(input('Qual seu peso?: '))

IMC = (peso/(altura*altura))


if IMC>=29.9:
    msg = 'YOU IS NOT HELTHY'

elif 25<IMC<29.9:
    msg = 'CAUTION FOR YOUR HEALTH'

else:
    msg = ' YOU IS HELTHY'

print('Your IMC IS:', IMC, msg)
