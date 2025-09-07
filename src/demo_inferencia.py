import joblib
import numpy as np
import pandas as pd
from pathlib import Path

ARTIFACTS = Path(__file__).resolve().parents[1] / "artifacts" / "best_model.joblib"
DATA = Path(__file__).resolve().parents[1] / "data" / "raw" / "ETTh1.csv"

def main():
    bundle = joblib.load(ARTIFACTS)
    model = bundle["model"]
    scaler = bundle["scaler"]
    df = pd.read_csv(DATA, parse_dates=["date"])
    df = df.sort_values("date").reset_index(drop=True)
    y = df["OT"].values.astype(float)
    warm_window = 302
    y_hist = y[-warm_window:]
    y_hist_scaled = scaler.transform(y_hist.reshape(-1,1)).ravel()

    # recursive 100-step forecast using last known values
    n_lags = getattr(model, "n_lags", 48)
    hist = list(y_hist_scaled[-n_lags:])
    preds_scaled = []
    for _ in range(100):
        x = np.array(hist[-n_lags:]).reshape(1, -1)
        yhat = float(model.predict(x).ravel()[0])
        preds_scaled.append(yhat)
        hist.append(yhat)

    preds = scaler.inverse_transform(np.array(preds_scaled).reshape(-1,1)).ravel()
    print("Pronóstico (primeros 10 de 100 pasos):", np.round(preds[:10], 3))

if __name__ == "__main__":
    main()