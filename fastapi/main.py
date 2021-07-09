from fastapi import FastAPI, HTTPException, Response
from typing import Optional
from contact_base import Contact, ContactOut

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/contact1/{contact_id}")
def contact_details(contact_id: int, page:Optional[int]=1):
    if page:
        return {'contact_id':contact_id, 'page':page}
    return {"Test": contact_id}


@app.post('/contact', response_model=Contact, response_model_exclude={"password"})
async def create_contact(contact: Contact):
    return contact


@app.get('/contact/{id}', response_model=Contact, response_model_exclude={"password"}, description="Fetch a contact")
async def contact_details(id: int):
    if id < 1:
        raise HTTPException(status_code=404, detail="The required contact details not found")
    contact = Contact(contact_id = id, first_name="Rajesh",surname="P", username="rajeshpyne",password="***")
    return contact
