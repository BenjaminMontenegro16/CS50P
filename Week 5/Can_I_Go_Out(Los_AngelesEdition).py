import sys
import requests

def get_weather():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Los+Angeles,US&appid=a072769bcc49d8eee751b0d46372542e&units=imperial")
    return response.json()



def suggest_clothing(t):
    if t >= 104 :
        print("Don't even try to go outside, it's boiling!")
    elif t >= 86 and t <= 102:
        print("It's really hot, but you can still go outside :)")
    elif t >= 68 and t <= 84:
        print("Really normal day go out if you want!")
    elif t >= 50 and t <= 66:
        print("It's a little cold, but you can still go outside!") 
    elif t >= 32 and t <= 48:
        print("It's incredibly cold, if you want to go outside, go really sheltered!")
    elif t >= 14 and t <- 30:
        print("It's freezing, maybe it's snowing outside, go skiing")

def main():

    data = get_weather()
    temp = data["main"]["temp"]
    print(f"The temperature on Los Angeles is:{temp}°F")
    suggest_clothing(temp)

if __name__ == "__main__":
    main()

#Now im starting to like APIs, its not that logical, its more research than syntax.