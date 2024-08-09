from fastapi import APIRouter, HTTPException, Body, Response
from app.services.account_service import AccountService
from app.database import Database
from fastapi.responses import JSONResponse

router = APIRouter()
db = Database()
service = AccountService(db)

@router.post("/reset")
async def reset():
    db.reset()
    return Response(status_code=200, content="OK")

@router.get("/balance")
async def get_balance(account_id: str):
    balance = service.get_balance(account_id)
    if balance is None:
        return JSONResponse(content=0, status_code=404)
    return JSONResponse(content=balance, status_code=200)


@router.post("/event")
async def handle_event(event: dict = Body(...)):
    event_type = event.get("type")
    
    try:
        if event_type == "deposit":
            account = service.deposit(event["destination"], event["amount"])
            if account:
                return JSONResponse(content={"destination": account}, status_code=201)
            else:
                return Response(content="0", status_code=404)

        elif event_type == "withdraw":
            account = service.withdraw(event["origin"], event["amount"])
            if account:
                return JSONResponse(content={"origin": account}, status_code=201)
            else:
                return Response(content="0", status_code=404)

        elif event_type == "transfer":
            result = service.transfer(event["origin"], event["destination"], event["amount"])
            if result:
                origin, destination = result
                return JSONResponse(content={"origin": origin, "destination": destination}, status_code=201)
            else:
                return Response(content="0", status_code=404)
        
        else:
            raise HTTPException(status_code=400, detail="Invalid event type")
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
