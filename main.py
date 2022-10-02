from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Link(BaseModel):
    url: str

@app.post("/")
async def root(link: Link):
    if link.url.startswith("https://www.missionjuno.swri.edu/junocam/processing?id="):
        if link.url.startswith("https://www.missionjuno.swri.edu/junocam/processing?id=JNCE_2019149_"):
            #exec(open('model.py').read(), {'argv': link.url})
            return {"message": "success"}
        else:
            return {"message": "error1"}
    else:
        return {"message": "error2"}
    
    return {"message": "Success"}

@app.get("/")
async def get():
    return {"message": "test"}

@app.head("/")
async def head():
    print("head request received correctly")
    return {"message:" "Success"}

@app.options("/")
async def options():
    print("options request received correctly")
    return {"message": "Success"}