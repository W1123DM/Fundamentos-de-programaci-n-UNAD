# ============================================
# Problema 5 - Control de Horas Semanales
# ============================================

# MATRIZ:
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 10, 9, 10, 9, 10],
    ["Marta", 8, 8, 8, 8, 8]
]

# --------------------------------------------
# MÓDULO / FUNCIÓN
# Calcula el total de horas y clasifica
# la jornada laboral
# --------------------------------------------

def calcular_horas(datos_recurso):

    nombre = datos_recurso[0]

    # Suma de horas trabajadas
    total_horas = sum(datos_recurso[1:])

    # Clasificación de jornada
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# --------------------------------------------
# PROCESO PRINCIPAL
# --------------------------------------------

print("REPORTE DE HORAS SEMANALES\n")

for recurso in recursos:

    nombre, total, estado = calcular_horas(recurso)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", estado)
    print("-----------------------------")