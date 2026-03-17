import fastapi

app=fastapi.FastAPI()

@app.get("/")
def home():
    return {"message":"Estatehub Test API is working fine!"}