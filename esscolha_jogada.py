
def jogada_escolhida(escolha): 
  if escolha == 1:
    from random import choices
    print("Você escolheu Passe")
    resul_possiveis = ['Passe completo', 'Passe Incompleto', 'Passe Interceptado', 'Sack']
    pesos = [30, 30, 15, 25]
    resultado = choices(resul_possiveis, pesos)
    if resultado == ['Passe completo']:
      print("Que recepção meu filho!!!")
    elif  resultado == ['Passe Incompleto']:
      print("Passe nao completado Proxima decida")
    elif resultado == ['Passe Interceptado']:
      print("Interceptação!!")
    else:
      print("Seu QB foi sackado!!")
    print(*resultado )
    
  else:
    from random import choices
    print("Você escolheu Corrida")
    resul_possiveis = ['Tackle', 'Touchdown', 'Fumble']
    pesos = [80, 5, 15]
    resultado = choices(resul_possiveis, pesos)
    print(*resultado)
    if resultado == ['Tackle']:
      print("Ganhou x jardas")
    elif resultado == ['Touchdown']:
      print("TOOOUCHHHDOOOOOOOWNNN")
    else:
      print("Fumble é vida! Bola recuperado pelo x time")

escolha = int(input("Escolha a proxima jogada de ataque:\n""1 => Passe\n""2 => Corrida\n"))

jogada_escolhida(escolha)