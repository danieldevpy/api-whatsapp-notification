from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from controller.wpp import WhatsappNotification, ChromeDriverController
from controller.list_contacts import ListContacts
from controller.number import NumberController
from pydantic import BaseModel


class RequestWpp(BaseModel):
    number: str
    message: str


app = FastAPI()
templates = Jinja2Templates(directory="templates")
driver = ChromeDriverController(False, True)
contacts = ListContacts()
wpp = WhatsappNotification(driver, contacts)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "contatos": contacts.get_contacts_list()})

@app.get('/contatos')
def get_contatos():
    return {"contatos": contacts.get_contacts_list()}

@app.post('/send')
def send_message(data: RequestWpp):
    contact = contacts.get_contact(data.number)
    try:
        if contact:
            wpp.send_message(contact, data.message)
        else:
            number = NumberController.check(data.number)
            wpp.send_message_new_contact(number, data.message)
        return JSONResponse({"msg": "A mensagem foi enviada"})
    except Exception as e:
        return JSONResponse({"msg": str(e)}, 400)

@app.post('/sendForm')
def send_message(request: Request, contato: str = Form(None), message: str = Form(None)):
    contact = contacts.get_contact(contato)
    msg = None
    if not contact:
        msg = 'contato não encontrado'
    wpp.send_message(contact, message)
    if msg == None:
        msg = 'a mensagem foi enviada'
    return templates.TemplateResponse("index.html", {
        "request": request,
        "contatos": contacts.get_contacts_list(),
        "alert": msg
    })
