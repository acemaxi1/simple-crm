from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlite3 import IntegrityError
from storage.database import Base, engine
from models.db.orders import Order
from models.db.customers import Customer


app = FastAPI()
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

#API
orders_path = '/orders'
@app.get(
    orders_path,
    status_code=status.HTTP_200_OK,
    tags=['orders'],
    summary='Get orders'
)
async def get_orders(customer: str = None):
    try:
        return Order.get({'customer_name': customer})
    except IntegrityError as ex:
        msg = "Unable to retrive orders: %s" % ex
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            msg
        )
    
customers_path = '/customers/names'
@app.get(
    customers_path,
    status_code=status.HTTP_200_OK,
    tags=['customers'],
    summary='Get customers'
)
async def get_customers_names():
    try:
        return [item.customer_name for item in Customer.get_names()]
    except IntegrityError as ex:
        msg = "Unable to retrive customers: %s" % ex
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            msg
        )

#CONTROLLER
@app.get("/", response_class=HTMLResponse)
async def generate_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


