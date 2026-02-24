import sys
import requests

def get_weather():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Posadas,AR&appid=a072769bcc49d8eee751b0d46372542e&units=metric")
    return response.json()



def suggest_clothing(t):
    if t >= 40 :
        print("No se vio en años esto, trata de quedarte en casa con el aire!")
    elif t >= 30 and t <= 39:
        print("Esta re caliente, bermuda y remera, Si o si!")
    elif t >= 20 and t <= 29:
        print("Dia normalito, sali como quieras :)")
    elif t >= 10 and t <=19:
        print("Bastante frio che, Sali con campera y Pantalon, si o si") 
    elif t >= 0 and t <= 9:
        print("Esta reee frio, sali con un camperon!")
    elif t >= -10 and t <- -1:
        print("Ola Polar 100%, Trata de ni salir!")

def main():

    data = get_weather()
    temp = data["main"]["temp"]
    print(f"La temperatura en posadas es de:{temp}°C")
    suggest_clothing(temp)

if __name__ == "__main__":
    main()