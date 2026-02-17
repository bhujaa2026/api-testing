from fastapi import FastAPI

app = FastAPI()

# This is our API
@app.get("/weather")
def get_weather(city: str):
    data = {
        "Chennai": "32°C",
        "Delhi": "28°C",
        "Mumbai": "30°C"
    }

    return {
        "city": city,
        "temperature": data.get(city, "City not found")
    }
