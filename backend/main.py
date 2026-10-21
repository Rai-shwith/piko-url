from fastapi import FastAPI

app = FastAPI(title="piko-url")

@app.get("/")
def health_check():
    return {
        "status":"ok",
        "service":"piko-url-backend"
    }
    