


from fastapi import APIRouter
from typing import Dict
from app.models.clientuser import Client

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)


client_data = {
    1: Client(name="Healthgraph", location="New York", description="A valuable client", usermail="john.doe@example.com", phone="123-456-7890"),
    2: Client(name="santa", location="Los Angeles", description="A new client", usermail="alice.smith@example.com", phone="987-654-3210"),
    3: Client(name="walmart", location="Chicago", usermail="bob.johnson@example.com", phone="555-123-4567")
}

@router.get("/")
async def get_clients():
    return client_data

@router.get("/{client_id}")
async def get_client_details(client_id: int):
    if client_id in client_data:
        return client_data[client_id]
    else:
        return {"message": "Client not found"}