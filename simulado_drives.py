
def drive(pi, pqb, nd, oj):
  from random import randint
  inicio_jogada = pi - pqb #de onde a bola sai 
  jardas_ganhas = randint(0, 10) #quantia de jardas ganhas
  pf = inicio_jogada + jardas_ganhas
  objetivo = oj
  print("Será first down na linha de {} jardas".format(objetivo))

  
  if pf >= objetivo:
    print("\n\nConseguiu o first down")
    print("O ataque termiou na linha de {} jardas".format(pf))
  elif pf < objetivo and nd != 4:
    nd += 1
    print("A jogada terminou na linha de {}".format(pf))
    print("\n\nvai para o {}° down".format(nd))
    print("Iniciando na linha de {} jardas".format(pf))
    drive(pf, 0, nd, objetivo)
  else:
    print("turnover on downs")
    print("O ataque termiou na linha de {} jardas".format(pf))
    
    
pos_incial=int(input("Em que jarda o ataque inicia?"))
num_drive = 1
objetivo = pos_incial + 10
drive(pos_incial, 0, num_drive, objetivo)



