sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Valor incorreto. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
