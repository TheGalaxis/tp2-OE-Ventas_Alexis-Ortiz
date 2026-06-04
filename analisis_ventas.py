import csv
import datetime
import importlib.util
import os
import collections

# ------------------------------------------------------------
# Verificar si matplotlib está disponible
# ------------------------------------------------------------
if importlib.util.find_spec("matplotlib") is not None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
else:
    plt = None

# ------------------------------------------------------------
# Cargar el dataset desde /datos
# ------------------------------------------------------------
ruta_datos = os.path.join("datos", "ventas.csv")
ventas = []

with open(ruta_datos, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila["cantidad"] = int(fila["cantidad"])
        fila["precio"] = float(fila["precio"])
        fila["fecha"] = datetime.datetime.strptime(fila["fecha"], "%Y-%m-%d").date()
        fila["venta_total"] = fila["cantidad"] * fila["precio"]
        ventas.append(fila)

# ------------------------------------------------------------
# Cálculo 1: Ventas totales
# ------------------------------------------------------------
ventas_totales = sum(f["venta_total"] for f in ventas)

# ------------------------------------------------------------
# Cálculo 2: Producto más vendido
# ------------------------------------------------------------
contador_productos = collections.Counter(f["producto"] for f in ventas)
producto_mas_vendido = contador_productos.most_common(1)[0][0]

# ------------------------------------------------------------
# Cálculo 3: Ventas por mes
# ------------------------------------------------------------
ventas_por_mes = {}
for f in ventas:
    mes = f["fecha"].strftime("%Y-%m")
    ventas_por_mes[mes] = ventas_por_mes.get(mes, 0) + f["venta_total"]

ventas_por_mes = dict(sorted(ventas_por_mes.items()))

# ------------------------------------------------------------
# Ventas por día
ventas_por_fecha = {}
for f in ventas:
    dia = f["fecha"].strftime("%Y-%m-%d")
    ventas_por_fecha[dia] = ventas_por_fecha.get(dia, 0) + f["venta_total"]

ventas_por_fecha = dict(sorted(ventas_por_fecha.items()))

# ------------------------------------------------------------
# Guardar resultados en /resultados
# ------------------------------------------------------------
os.makedirs("resultados", exist_ok=True)

with open(os.path.join("resultados", "resumen_ventas.csv"), "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["ventas_totales", "producto_mas_vendido"])
    escritor.writerow([f"{ventas_totales:.2f}", producto_mas_vendido])

with open(os.path.join("resultados", "ventas_por_mes.csv"), "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["mes", "venta_total"])
    for mes, total in ventas_por_mes.items():
        escritor.writerow([mes, f"{total:.2f}"])

with open(os.path.join("resultados", "ventas_por_dia.csv"), "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["dia", "venta_total"])
    for dia, total in ventas_por_fecha.items():
        escritor.writerow([dia, f"{total:.2f}"])

# ------------------------------------------------------------
# Gráfico: Evolución de ventas por día
# ------------------------------------------------------------
if plt is not None:
    plt.figure(figsize=(10, 5))
    plt.plot(list(ventas_por_fecha.keys()), list(ventas_por_fecha.values()), marker="o")
    plt.title("Evolución de Ventas por Día")
    plt.xlabel("Fecha")
    plt.ylabel("Ventas Totales ($)")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join("resultados", "grafico_ventas_diarias.png"))
    plt.close()
else:
    print("Advertencia: matplotlib no está disponible. Se omitió la generación del gráfico.")

print("Análisis completado correctamente.")
print(f"Ventas totales: ${ventas_totales:.2f}")
print(f"Producto más vendido: {producto_mas_vendido}")