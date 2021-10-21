## 8-  Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# A formula de conversão é C = K  - 273.15,
# Sendo C a temperatura em Celsius e K a temperatura em Kelvin

temperatura = input('Digite a temperatura em Kelvin: ')

tempKelvin = float(temperatura)

tempCelsius = tempKelvin - 273.15
print(f'A temperatura {tempKelvin}º Kelvin, convertida em Celsius e: ', tempCelsius)