from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def acceuil():
    return {"message": "Bienvenue sur notre API de recommandation de parfums"}