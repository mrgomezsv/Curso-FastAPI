import zoneinfo
from datetime import datetime

from fastapi import FastAPI
from models import CustomerCreate, Transaction, Invoice, Customer


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


current_id: int = 0

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    country_timezone.get(iso)
    timezone_str = country_timezone.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}


db_customers: list[Customer] = []


@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    # Asumiendo que se hace en la base de datos
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer


@app.get("/customers", response_model=list[Customer])
async def list_customer():
    return db_customers


@app.post("/transactions")
async def create_transactions(transactions_data: Transaction):
    return transactions_data


@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data
