import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# Fechas y eventos en la línea de tiempo
dates = [
    "2006-01-01", "2007-01-01", "2008-01-01", "2009-01-01", 
    "2012-01-01", "2013-01-01", "2018-01-01", "2018-07-01", 
    "2019-01-01", "2023-01-01", "2023-08-01", "2024-01-01"
]
events = [
    "Ley N.º 2.264: Crea el Régimen de Promoción Cultural",
    "Decreto N.º 886: Reglamentación de la Ley N.º 2.264",
    "Resolución N.º 4054: Coordinación Administrativa",
    "Decreto N.º 1135: Asignación de presupuesto",
    "Ley N.º 4.353: Distrito de las Artes",
    "Decreto N.º 429: Plataforma TAD para trámites",
    "Resolución N.º 3794: Reglamento General del Régimen",
    "Ley N.º 6.026: Nuevo Régimen de Participación Cultural",
    "Decreto N.º 155: Reglamenta Ley N.º 6.026",
    "Resolución N.º 4962: Procedimientos de solicitudes",
    "Resolución N.º 6565: Periodo de inscripción",
    "Decreto N.º 279: Texto ordenado de Ley N.º 6.026"
]

# Convertir fechas a formato datetime
dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, [1]*len(dates), "bo-", color="skyblue", markerfacecolor="blue")

# Configuración del eje x y formato de fechas
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.xticks(rotation=45)

# Eliminar el eje y para un aspecto más limpio
ax.get_yaxis().set_visible(False)

# Añadir los eventos a la gráfica
for i, (date, event) in enumerate(zip(dates, events)):
    ax.text(date, 1.05, event, rotation=45, verticalalignment="bottom", horizontalalignment="right", fontsize=9)

# Título y ajuste de la disposición
plt.title("Línea de Tiempo de la Evolución Normativa del Régimen de Promoción Cultural en CABA")
plt.tight_layout()

# Guardar la imagen como archivo PNG
plt.savefig("evolucion_normativa_rpc_timeline.png")

# Mostrar la gráfica
plt.show()
