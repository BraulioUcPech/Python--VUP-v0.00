def calcular_circuitos_en_serie(voltaje, resistencias):
    # Calcula la resistencia total
    resistencia_total = sum(resistencias)

    # Calcula la corriente total
    corriente_total = voltaje / resistencia_total

    resultados = {
        'Corriente total': corriente_total,
        'Voltaje total': voltaje,
        'Potencia total': voltaje * corriente_total,
        'Resistencia total': resistencia_total
    }

    for i, resistencia in enumerate(resistencias):
        # Calcula el voltaje en cada resistencia
        voltaje_resistencia = corriente_total * resistencia

        # Calcula la potencia en cada resistencia
        potencia_resistencia = voltaje_resistencia * corriente_total

        Diferencia_voltaje = voltaje -  voltaje_resistencia

        resultados[f'Voltaje R{i+1}'] = voltaje_resistencia
        resultados[f'Potencia en R{i+1}'] = potencia_resistencia
        resultados[f'Diferencia de voltaje R{i+1}'] = Diferencia_voltaje

    return resultados


# Ejemplo de uso
voltaje = 108
resistencias = [20,60, 30, 40, 24, 12]

resultados = calcular_circuitos_en_serie(voltaje, resistencias)

# Imprime los resultados
for clave, valor in resultados.items():
    print(f'{clave}: {valor}')




def calcular_voltaje(corriente, resistencia):
    voltaje = corriente * resistencia
    return voltaje


corriente = 2  # Ampere
resistencia = 17.8  # Ohm

voltaje = calcular_voltaje(corriente, resistencia)
print(f'El voltaje en el circuito es: {voltaje} Voltios')


def calcular_resistencia(voltaje, corriente):
    resistencia = voltaje / corriente
    return resistencia


voltaje = 36 # Voltios
corriente = 2 # Ampere

resistencia = calcular_resistencia(voltaje, corriente)
print(f'El valor de la resistencia es: {resistencia} Ohmios')
