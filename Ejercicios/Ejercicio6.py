# Programa que pase una velocidad en Km/h a m/s. 
#La velocidad se lee por teclado.

velocidad = float(input("Ingrese la velovcidad en KM/H -> "))
print(f"{velocidad} kM/H -> ",velocidad * 1000 / 3600," m/s22")

# Solucion de chatgpt

velocidad_km_h = float(input("Introduce la velocidad en km/h: "))
velocidad_m_s = velocidad_km_h * 1000 / 3600
print("La velocidad en m/s es:", velocidad_m_s)

