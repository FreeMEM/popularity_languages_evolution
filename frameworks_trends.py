from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
import time

# Configurar ffmpeg como el writer de animación
rcParams["animation.ffmpeg_path"] = "/usr/bin/ffmpeg"

# Configurar pytrends
pytrends = TrendReq(
    hl="en-US",
    tz=360,
    # retries=2,
    backoff_factor=0.1,
    requests_args={"verify": False},
    geo="GLOBAL",
)

# Lista de términos de búsqueda
search_terms = [
    "flutter",
    "react native",
    "django",
    "laravel",
    "react",
    "angular",
    "vue",
]


# Función para obtener datos de Google Trends con reintentos
def get_trends_data(terms, retries=1):
    for i in range(retries):
        try:
            pytrends.build_payload(
                terms, cat=0, timeframe="today 5-y", geo="GLOBAL", gprop=""
            )
            data = pytrends.interest_over_time()
            if "isPartial" in data.columns:
                data = data.drop(columns=["isPartial"])
            return data
        except Exception as e:
            print(f"Error fetching data (attempt {i+1}): {e}")
            time.sleep(2)  # Esperar 2 segundos antes de reintentar
    raise Exception("Failed to fetch data from Google Trends after multiple attempts")


# Obtener los datos de interés a lo largo del tiempo
try:
    data = get_trends_data(search_terms)
    print(data.head())
except Exception as e:
    print(f"Error fetching data: {e}")
    data = pd.DataFrame()

# Crear la figura y el eje para la gráfica
if not data.empty:
    fig, ax = plt.subplots(figsize=(12, 8))

    # Función para actualizar la gráfica en cada cuadro de la animación
    def update(frame):
        ax.clear()
        ax.set_title(
            f'Popularidad de frameworks de desarrollo - {frame.strftime("%B %Y")}'
        )
        ax.set_xlabel("Frameworks")
        ax.set_ylabel("Interés")
        ax.set_ylim(0, data.max().max() + 5)

        # Graficar datos para el cuadro actual (mes)
        current_data = data.loc[frame]
        current_data.plot(kind="bar", ax=ax, color=plt.cm.tab10.colors)

        plt.xticks(rotation=45)
        plt.tight_layout()

    # Crear la animación
    ani = FuncAnimation(fig, update, frames=data.index, repeat=False, interval=200)

    # Guardar la animación como un archivo MP4 usando ffmpeg
    ani.save("frameworks_popularity.mp4", writer="ffmpeg")

    print("Animation has been saved as 'frameworks_popularity.mp4'")
else:
    print("No data to plot.")
