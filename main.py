from fastapi import FastAPI, Response, HTTPException
from models import Event
from database import db

app = FastAPI()

@app.post("/reset")
def reset(response: Response):
    db.reset()
    response.status_code = 200
    return Response(status_code=200, content="OK")

@app.get("/balance")
def get_balance(account_id: str):
    account = db.get_account(account_id)
    if account:
        return account.balance
    return Response(content="0", status_code=404)

@app.post("/event")
def handle_event(event: Event, response: Response):
    if event.type == "deposit":
        account = db.get_account(event.destination)
        if not account:
            account = db.create_account(event.destination, event.amount)
        else:
            account.balance += event.amount
        response.status_code = 201
        return {"destination": {"id": account.account_id, "balance": account.balance}}

    elif event.type == "withdraw":
        account = db.get_account(event.origin)
        if account and account.balance >= event.amount:
            account.balance -= event.amount
            response.status_code = 201
            return {"origin": {"id": account.account_id, "balance": account.balance}}
        return Response(content="0", status_code=404)

    elif event.type == "transfer":
        origin_account = db.get_account(event.origin)
        destination_account = db.get_account(event.destination)

        if origin_account and origin_account.balance >= event.amount:
            if not destination_account:
                destination_account = db.create_account(event.destination, 0)
            origin_account.balance -= event.amount
            destination_account.balance += event.amount
            response.status_code = 201
            return {
                "origin": {"id": origin_account.account_id, "balance": origin_account.balance},
                "destination": {"id": destination_account.account_id, "balance": destination_account.balance}
            }
        return Response(content="0", status_code=404)

    raise HTTPException(status_code=400, detail="Invalid event type")
