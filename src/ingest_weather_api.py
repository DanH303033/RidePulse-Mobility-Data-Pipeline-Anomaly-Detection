from pathlib import Path
from utils import BRONZE_DIR

import pandas as pd
import requests


OUTPUT_FILE = BRONZE_DIR / "weather_nyc_2026_01-04.csv"


def fetch_weather_data() -> pd.DataFrame:
    """
    Fetch hourly historical weather data for New York City from Open-Meteo API.
    """

    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "start_date": "2026-01-01",
        "end_date": "2026-04-30",
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "rain",
            "weather_code",
            "wind_speed_10m",
        ],
        "timezone": "America/New_York",
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    hourly_data = data["hourly"]
    weather = pd.DataFrame(hourly_data)

    weather = weather.rename(columns={"time": "weather_datetime"})
    weather["weather_datetime"] = pd.to_datetime(weather["weather_datetime"])

    weather["weather_date"] = weather["weather_datetime"].dt.date
    weather["weather_hour"] = weather["weather_datetime"].dt.hour

    return weather


def save_weather_data(weather: pd.DataFrame) -> None:
    """
    Save weather data into the bronze data layer.
    """

    BRONZE_DIR.mkdir(parents=True, exist_ok=True)
    weather.to_csv(OUTPUT_FILE, index=False)


def main() -> None:
    weather = fetch_weather_data()
    save_weather_data(weather)

    print(f"Weather data saved to: {OUTPUT_FILE}")
    print(f"Rows: {len(weather):,}")
    print(f"Columns: {list(weather.columns)}")


if __name__ == "__main__":
    main()