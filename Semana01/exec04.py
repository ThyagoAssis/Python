## 9 - Leia uma temperatura em Celsius e apresente-a convertida em graus Kelvin.
# A formula de conversão é K = C+273.15,
# Sendo C a temperatura em Celsius e K a temperatura em Kelvin

temperatura = input('Digite a temperatura em Celsius: ')

tempCelsius = float(temperatura)

tempKelvin = tempCelsius + 273.15
print(f'A temperatura {tempCelsius}º Celsius, convertida em Kelvin e: ',tempKelvin)