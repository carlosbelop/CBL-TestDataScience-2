# Pronóstico de Serie Temporal Multivariante (ETT - OT sin estacionalidad)

Este repositorio contiene un proyecto completo en **Python** para pronosticar **100 pasos en el futuro** de la variable **OT (Oil Temperature)** del dataset abierto **ETT (Electricity Transformer Temperature)**, **sin acceso a regresores futuros a partir del instante de predicción**.

## Contenidos

- `notebooks/01_forecasting_ett_nonseasonal.ipynb`: Notebook principal con todo el análisis, comprobaciones, modelado, evaluación y guardado del mejor modelo.
- `src/forecast_ett/`: Código auxiliar (utilidades de features, evaluación, pipeline de guardado/carga de modelo).
- `scripts/demo_inferencia.py`: Demostración mínima de carga del mejor modelo entrenado y generación de un pronóstico de 100 pasos.
- `requirements.txt`: Dependencias fijadas para reproducibilidad.
- `reports/figures/`: Carpeta para gráficos generados.
- `models/`: Carpeta donde se guardarà el mejor modelo entrenado y los scalers asociados.
- `data/`: Descarga automática del dataset al ejecutar el notebook (si no existe).

## Dataset (fuente)
- **ETT (Electricity Transformer Temperature)** — *Zhou et al., AAAI 2021*  
  Repositorio: https://github.com/zhouhaoyi/ETDataset  
  Archivo utilizado: `ETT-small/ETTh1.csv` (frecuencia horaria).

> La variable objetivo **OT** no presenta patrones de estacionalidad diaria/semanal evidentes según la descripción del dataset. En el notebook se realiza además una comprobación mediante ACF, STL, ADF y KPSS.

## Cómo reproducir

1. Crea y activa un entorno (opcional, recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Abre Jupyter y ejecuta el notebook en orden:
   ```bash
   jupyter lab  # o jupyter notebook
   ```

4. Al finalizar, se guardará el mejor modelo en `models/`. Puedes ejecutar la demo de inferencia:
   ```bash
   python scripts/demo_inferencia.py
   ```

## Estándares de calidad

- Estilo **PEP8**.
- Análisis estático con **flake8**, **isort**, **mypy** (tipado en utilidades clave).
- Estructura tipo *cookie-cutter* ligera.

## Nota
El notebook descarga automáticamente `ETTh1.csv` desde el repo oficial de ETT si no se encuentra en `data/raw/`.