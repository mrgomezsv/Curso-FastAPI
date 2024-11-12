import zoneinfo
from datetime import datetime
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message":  "Hola Mario!"}


country_timezone = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    country_timezone.get(iso)
    timezone_str = country_timezone.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}
