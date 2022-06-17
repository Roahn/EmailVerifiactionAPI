from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sendemail
app = FastAPI()


class EmailAdd(BaseModel):
    email:str


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''

@app.get("/css/home", response_class=FileResponse)
async def Home():
    return FileResponse("./Home.css")

@app.get("/css/nicepage", response_class=FileResponse)
async def Nice():
    return FileResponse("./nicepage.css")

'''


@app.get("/js/handle", response_class=FileResponse)
async def javascript():
    return FileResponse("./handle.js")
@app.get("/js/enter", response_class=FileResponse)
async def javascript():
    return FileResponse("./enteremail.js")

@app.get('/sendemailaddress/{email}')
def getemail(email):
    print(email)
    OTP_TEXT = sendemail.OTP()
    sendemail.send(email, OTP_TEXT)

    return {"email": email,"OTP":OTP_TEXT}
