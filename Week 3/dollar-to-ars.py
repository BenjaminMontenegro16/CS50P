dollar = [{"name": "dolar oficial", "cost": 1370},
           {"name": "dolar blue", "cost": 1415},
           {"name": "dolar tarjeta", "cost": 1846},
           {"name":"dolar mep", "cost": 1408 }]


user_request = input("Que dolar desea consultar? ").strip(" ").lower()


found = False
for d in dollar :
    if user_request == d["name"]: 
        print (f"{d['name']} cuesta {d['cost']}")
        found = True
        break


if not found: print("Dolar no encontrado")