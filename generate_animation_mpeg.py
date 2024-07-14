import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams

# Configurar ffmpeg como el writer de animación
rcParams["animation.ffmpeg_path"] = "/usr/bin/ffmpeg"

# Cargar el dataset
file_path = "Popularity of Programming Languages from 2004 to 2024.csv"
data = pd.read_csv(file_path)

# Convertir la columna 'Date' a datetime con el formato especificado
data["Date"] = pd.to_datetime(data["Date"], format="%B %Y")

# Establecer la columna 'Date' como el índice
data.set_index("Date", inplace=True)

# Seleccionar un subconjunto de lenguajes para la animación
selected_languages = [
    "Python",
    "Java",
    "JavaScript",
    "C#",
    "C/C++",
    "Dart",
    "Go",
    "PHP",
    "Rust",
]

# Crear la figura y el eje para la gráfica
fig, ax = plt.subplots(figsize=(12, 8))


# Función para actualizar la gráfica en cada cuadro de la animación
def update(frame):
    ax.clear()
    ax.set_title(f'Popularity of Programming Languages - {frame.strftime("%B %Y")}')
    ax.set_xlabel("Programming Languages")
    ax.set_ylabel("Popularity (%)")
    ax.set_ylim(0, data[selected_languages].max().max() + 5)

    # Graficar datos para el cuadro actual (mes)
    current_data = data.loc[frame, selected_languages]
    current_data.plot(kind="bar", ax=ax, color=plt.cm.tab10.colors)

    plt.xticks(rotation=45)
    plt.tight_layout()


# Crear la animación
ani = FuncAnimation(fig, update, frames=data.index, repeat=False, interval=200)

# Guardar la animación como un archivo MP4 usando ffmpeg
ani.save("programming_languages_popularity.mp4", writer="ffmpeg")

print("Animation has been saved as 'programming_languages_popularity.mp4'")
