#pede para o usuário colocar um número inteiro qualquer:
tb =  int(input('Digite um numero: '))

#processa e escreve a tabuada do número:
for x in range(1,11):
 processo = tb * x
 print(tb,'*',x,'= {}'.format(processo))
