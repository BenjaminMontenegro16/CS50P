import requests

def get_dolares():
    response = requests.get("https://dolarapi.com/v1/dolares")
    return response.json()

def main():
    while True:
        try:
            dolares = get_dolares()
            
            print("\nTipos de dólar disponibles:")
            for i, d in enumerate(dolares):
                print(f"{i + 1}. {d['nombre']} - Compra: ${d['compra']} | Venta: ${d['venta']}")

            opcion_input = input("\nElegí un tipo de dólar (O un número fuera de rango para salir): ")
    
            opcion = int(opcion_input) - 1
            if opcion < 0 or opcion >= len(dolares):
                print("Saliendo del convertidor...")
                break
                
            dolar_elegido = dolares[opcion]

            monto = float(input(f"¿Cuántos dólares querés convertir a {dolar_elegido['nombre']}? "))
            resultado = monto * dolar_elegido["venta"]

            print(f"\n{monto} USD ({dolar_elegido['nombre']}) = ${resultado:,.2f} ARS")
            print("-" * 30) 
            break 
        except ValueError:
            print("\nError: Por favor ingresá solo números.")

main()