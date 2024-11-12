import zoneinfo
from datetime import datetime

from fastapi import FastAPI
from models import Customer, Transaction, Invoice


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


@app.post("/customers")
async def create_customer(customer_data: Customer):
    
    return customer_data

@app.post("/transactions")
async def create_transactions(transactions_data: Transaction):
    
    return transactions_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data
