from datetime import date

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import get_connect

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
def home(req:Request):
    return templates.TemplateResponse(request=req,
                                      name="home.html")


@app.get("/add-expense")
def add_expense_get(req: Request):
    return templates.TemplateResponse(request=req, name="add_expense.html")


@app.post("/add-expense", response_class=HTMLResponse)
def add_expense(
    req: Request,
    expense_id: int = Form(),
    catagory: str = Form(),
    amount: int = Form(),
    description: str = Form(),
    expense_date: date = Form()):  # noqa: B008
    conn = get_connect()
    pen = conn.cursor()
    pen.execute(
        "insert into record(id,catagory,amount,travelDate,description)"
        " values(%s,%s,%s,%s,%s)",
        (expense_id, catagory, amount, expense_date, description),
    )
    conn.commit()
    pen.close()
    conn.close()
    return templates.TemplateResponse(
        request=req, name="expenses.html", context={"expenses": []}
    )


@app.get("/show-expense", response_class=HTMLResponse)
def search(req: Request):
    conn = get_connect()
    pen = conn.cursor(dictionary=True)
    pen.execute("select * from record")
    rows = pen.fetchall()
    conn.close()
    pen.close()
    return templates.TemplateResponse(
        request=req, name="expenses.html", context={"result": rows}
    )


@app.get("/search", response_class=HTMLResponse)
def search_by_catagory_get(req: Request):
    return templates.TemplateResponse(request=req, name="search_catagory.html")


@app.post("/search", response_class=HTMLResponse)
def search_by_catagory(req: Request, search: str = Form()):
    conn = get_connect()
    pen = conn.cursor(dictionary=True)
    pen.execute("select * from record where catagory like %s", (search,))
    rows = pen.fetchall()
    pen.close() 
    conn.close()
    
    return templates.TemplateResponse(
        request=req, name="expenses.html", context={"result": rows}
    )
@app.get("/highest_expense",response_class=HTMLResponse)
def highest_expense(req:Request):
    conn=get_connect()
    pen=conn.cursor(dictionary=True)
    pen.execute("select * from record where amount=(select max(amount) from record)")
    row=pen.fetchall()
    pen.close() 
    conn.close()
    
    return templates.TemplateResponse(request=req,
                                      name="expenses.html",
                                      context={"result":row})
@app.get("/total_expense",response_class=HTMLResponse)
def total_expense(req:Request):
    conn=get_connect()
    pen=conn.cursor()
    pen.execute("select sum(amount) from record")
    total=pen.fetchone()[0]
    pen.close() 
    conn.close()
    return templates.TemplateResponse(request=req,
                                      name="total.html",
                                      context={"result":total})
@app.get("/search_filter",response_class=HTMLResponse)
def get_filter(req:Request):
    return templates.TemplateResponse(request=req,
                                      name="filter.html",
                                      )
@app.post("/search_filter",response_class=HTMLResponse)
def filter_expense(req:Request,
           start_date:date=Form(),
           end_date:date =Form()):
    conn=get_connect()
    pen=conn.cursor(dictionary=True)
    pen.execute("select * from record where travelDate between %s and %s",(start_date,end_date))
    rows=pen.fetchall()
    pen.close() 
    conn.close()
    return templates.TemplateResponse(request=req,
                                      name="expenses.html",
                                      context={"result":rows})