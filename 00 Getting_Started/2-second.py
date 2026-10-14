from pathlib import Path
import pickle

import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "dataset" / "GDP.csv"
MODEL_PATH = BASE_DIR / "model.pkl"


def load_model_and_encoder():
    with MODEL_PATH.open("rb") as model_file:
        payload = pickle.load(model_file)

    if isinstance(payload, dict) and "model" in payload:
        return payload["model"], payload.get("encoder")

    return payload, None


def build_reference_data():
    df = pd.read_csv(DATA_PATH, skiprows=4)
    drop_columns = [column for column in ["Unnamed: 70", "2026"] if column in df.columns]
    df = df.drop(columns=drop_columns)

    year_columns = [int(column) for column in df.columns[4:] if str(column).isdigit()]

    value_vars = df.columns[4:]
    df_long = df.melt(
        id_vars=["Country Name", "Country Code"],
        value_vars=value_vars,
        var_name="Years",
        value_name="GDP",
    )
    df_long = df_long.dropna(subset=["GDP"]).copy()

    encoder = LabelEncoder()
    encoder.fit(df_long["Country Name"])

    return encoder, min(year_columns), max(year_columns)


model, saved_encoder = load_model_and_encoder()
reference_encoder, MIN_YEAR, MAX_YEAR = build_reference_data()
country_encoder = saved_encoder or reference_encoder
COUNTRIES = country_encoder.classes_.tolist()


def render_home(error=None, selected_country="", selected_year=""):
    return render_template(
        "index.html",
        countries=COUNTRIES,
        error=error,
        max_year=MAX_YEAR,
        min_year=MIN_YEAR,
        selected_country=selected_country,
        selected_year=selected_year,
    )


@app.route("/")
def home():
    return render_home()


@app.route("/predict", methods=["POST"])
def predict():
    country = request.form.get("country", "").strip()
    selected_year = request.form.get("year", "").strip()

    try:
        if not country or country not in COUNTRIES:
            raise ValueError("Please choose a valid country from the list.")

        year = int(selected_year)
        if year < MIN_YEAR or year > MAX_YEAR:
            raise ValueError(f"Please enter a year between {MIN_YEAR} and {MAX_YEAR}.")

        country_label = int(country_encoder.transform([country])[0])
        features = pd.DataFrame({"Country_Label": [country_label], "Years": [year]})
        prediction = float(model.predict(features).squeeze())
    except ValueError as exc:
        return render_home(
            error=str(exc),
            selected_country=country,
            selected_year=selected_year,
        ), 400

    return render_template(
        "result.html",
        country=country,
        formatted_prediction=f"{prediction:,.2f}",
        prediction_text=f"Predicted GDP for {country} in {year} is {prediction:,.2f} USD.",
        year=year,
    )


if __name__ == "__main__":
    app.run(debug=True)
