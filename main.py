from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
app = FastAPI()

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


@app.get("/js/enter", response_class=FileResponse)
async def javascript():
    return FileResponse("./enteremail.js")

