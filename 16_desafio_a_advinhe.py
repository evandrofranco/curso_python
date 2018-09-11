import random

guesses_made = 0

name = input('Olá! Qual é o seu nome?\n')

number = random.randint(1, 20)
print('OK, {0}, Eu estou pensando em um número entre 1 e 20. \
        Vamos ver se você advinha?'.format(name))

while guesses_made < 6:

    guess = int(input('Diga um palpite: '))

    guesses_made += 1

    if guess < number:
        print('Seu palpite é muito baixo!')

    if guess > number:
        print('Seu palpite é muito alto!')

    if guess == number:
        break

if guess == number:
    print('Bom trabalho, {0}! Você adivinhou meu número em {1} tentativas!'
          .format(name, guesses_made))
else:
    print('Nãoooo! O número que eu estava pensando era {0}'.format(number))
