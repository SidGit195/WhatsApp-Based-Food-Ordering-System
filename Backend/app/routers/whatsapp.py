from fastapi import APIRouter, Form, Request, Depends, Response
from twilio.twiml.messaging_response import MessagingResponse
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/whatsapp", tags=["whatsapp"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/webhook")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db),
):
    resp = MessagingResponse()
    parts = Body.strip().split(";")
    if parts[0].lower() == "order" and len(parts) == 3:
        _, customer_name, items_raw = parts
        try:
            items = [
                schemas.OrderItemCreate(
                    menu_item_id=int(menu_id),
                    quantity=int(qty),
                )
                for menu_id, qty in (p.split(":") for p in items_raw.split(","))
            ]
            order_in = schemas.OrderCreate(
                customer_name=customer_name,
                whatsapp_number=From.replace("whatsapp:", ""),
                items=items,
            )
            order = crud.create_order(db, order_in)
            resp.message(f"✅ Thanks {customer_name}! Your order #{order.id} is confirmed.")
        except Exception as e:
            resp.message(f"❌ Could not place order: {e}")
    else:
        resp.message("Format: order;YourName;item1:qty,item2:qty")

    return Response(content=str(resp), media_type="application/xml")

@router.post("/status")
async def message_status(
    MessageSid: str = Form(...),
    MessageStatus: str = Form(...),
    To: str = Form(...),
    From: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Twilio will POST here when the message is queued, sent, delivered, read, etc.
    You can look up your Order by MessageSid or phone, then update its status in your DB.
    """
    # Example: log or update DB
    print(f"Msg {MessageSid} is now {MessageStatus}")
    return Response(status_code=204)