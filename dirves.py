info_drive =  {
    "scrimmage": 55,
    "position_qb": 5,
    "result": 0,
    "down": 1,
    "target": 65
}

def drive(infos):
    from random import randint
    initial_position =  infos.get("scrimmage") - infos.get("position_qb")
    #criar função para definir quantas jardas foram ganahas
    yards_gain = randint(0,10)
    infos["result"] = initial_position + yards_gain
    result = infos["result"]
    target = infos["target"]
    print(f"Será first down na linha de {target}")
    print(f"O ataque terminou na linha de {result}")

def main():
    drive(info_drive)

if __name__ == "__main__":
    main() 