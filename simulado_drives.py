
def drive(pi, pqb, nd, oj):
  from random import randint
  inicio_jogada = pi - pqb #de onde a bola sai 
  jardas_ganhas = randint(0, 10) #quantia de jardas ganhas
  pf = inicio_jogada + jardas_ganhas
  objetivo = oj
  print("Será first down na linha de {} jardas".format(objetivo))

  
  if pf >= objetivo:
    print("Conseguiu o first down")
    print("\nO ataque termiou na linha de {} jardas".format(pf))
  elif pf < objetivo and nd != 4:
    nd += 1
    print("A jogada terminou na linha de {}".format(pf))
    print("vai para o {}° down".format(nd))
    print("\nIniciando na linha de {} jardas".format(pf))
    drive(pf, 0, nd, objetivo)
  else:
    print("turnover on downs")
    print("\nO ataque termiou na linha de {} jardas".format(pf))
    
    
pos_incial=int(input("Em que jarda o ataque inicia?"))
num_drive = 1
objetivo = pos_incial + 10
drive(pos_incial, 0, num_drive, objetivo)



