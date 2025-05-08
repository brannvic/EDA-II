from scipy.optimize import minimize

# Definir la función objetivo A(r)
def area_superficial(r):
    return 2/r + 2 * 3.1416 * r**2

# Restricción del volumen
def restriccion(r):
    return 3.1416 * r**2 * (1/(3.1416 * r**2))

# Definir el problema de optimización
problema_optimizacion = {
    'type': 'eq',
    'fun': lambda r: restriccion(r) - 1
}

# Valor inicial para r
valor_inicial = 0.5

# Minimizar la función objetivo sujeta a la restricción
resultado_optimizacion = minimize(area_superficial, valor_inicial, constraints=problema_optimizacion)

# Obtener el radio óptimo
radio_optimo = resultado_optimizacion.x[0]

# Calcular la altura correspondiente
altura_optima = restriccion(radio_optimo)

# Mostrar resultados
print(f"Radio óptimo: {radio_optimo}")
print(f"Altura correspondiente: {altura_optima}")
print(f"Área superficial mínima: {resultado_optimizacion.fun}")
