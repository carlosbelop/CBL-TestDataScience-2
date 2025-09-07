
# CBL-TestDataScience-2

Proyecto de ciencia de datos desarrollado en formato Jupyter Notebook y exportado como HTML.
Serie temporal y regression.

## 📊 Dataset  

Dataset de la información temporal de dos transofrmadores de electricidad en dos diferentes estaciones. Incluyen carga y temperatura del aceite.

- **Fuente**: 
  ETT (Electricity Transformer Temperature) — *Zhou et al., AAAI 2021*  
  Repositorio: https://github.com/zhouhaoyi/ETDataset  
  Archivo utilizado: `ETT-small/ETTh1.csv` (frecuencia horaria). 
- **Instancias**:  
  - 17420  
- **Atributos**: 6 atributos de carga, uno de fecha y otro de temperatura del aceite.
- **Problema**: predicción de **OT** (Oil Temperature) con los demás valores mediante regresión y sin disponibilidad de las demás variables para predecir.

---



**Atributos:**

      1. date
      2. HUFL: High UseFul Load. float
      3. HULL: High UseLess Load. float
      4. MUFL: Middle UseFul Load. float
      5. Mull: Middel UseLess Load. float
      6. LUFL: Low UseFul Load. float
      7. LULL: Low UseLess Load. float
      8. OT: Oil Temperature. float


**Objetivo:**  
Predecir los últimos 100 días sin uso de las demás variables regresoras. Elegir el mejor modelo mediante evaluación de MSE, RMSE y MAPE. Uso práctico del modelo.

El pipeline incluye:
- Carga y preprocesamiento de datos.
- EDA y análisis.
- Entrenamiento y evaluación de modelos.
- Guardado de resultados.



## ⚙️ Installation

Crear un entorno de conda o un entorno virtual con python==3.12 e instalar las dependencias:

```bash
pip install -r requirements.txt

```
Clonar el repositorio e ir ejecutando el notebook.

⚠️ **WARNING** ⚠️ 
Si en el momento de ejecución, la generación de figuras muestra un error como el siguiente:
```bash
UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown.
```

Desinstalar y volver a instalar la librería ydata-profiling. Resetear el kernel y ya debería funcionar.

--Opcional--  
En vez de clonar el repositorio, es suficiente descargando el notebook:

Una vez instalado los paquetes, descargar el notebook **CBL-TestDataScience-2.ipynb** e ir ejecutándolo en orden.  
Conforme avance la ejecución, se irá creando el repositorio con los directorios y los resultados.




## Deployment

Después de la instalación y ejecución del notebook, ejecutar **scripts/predict.py**

Seguir las instrucciones para hacer predicciones con el modelo obtenido, tanto manualmente introduciendo valores por terminal como mediante un archivo df (usar prueba_test.csv por ejemplo).


## 📂 Estructura del repositorio  
```
CBL-TestDataScience-2
├── artifacts                # Modelos y objetos serializados
│   ├── best_model_RF.joblib    # Mejor modelo entrenado y estandarizador
│
├── data                     # Datos del proyecto
│   └── raw                  # Datos en bruto (sin procesar)
│       └── ETTh1.csv          # csv crudo con datos

├── notebooks                # Notebooks de experimentación
│   ├── CBL-TestDataScience-2.html   # Exportación en HTML del notebook
│   └── CBL-TestDataScience-2.ipynb  # Notebook principal con análisis y modelos
│
├── reports                  # Resultados y reportes del proyecto
│   ├── figures                        # Carpeta para figuras y gráficas
│   └── scores_df.csv  # Métricas de cada modelo entrenado
│
├── src                      # Código fuente del proyecto
│   └── demo_inferencia.py           # Script para hacer predicciones con el modelo entrenado
│
├── .gitignore               # Archivos/carpetas ignorados por git
├── README.md                # Documentación principal del proyecto
└── requirements.txt         # Dependencias necesarias para reproducir el entorno

```
## References

- H. Zhou, S. Zhang, J. Peng, S. Zhang, J. Li, H. Xiong, W. Zhang (2021). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI 2021), 35(12):11106-11115.

