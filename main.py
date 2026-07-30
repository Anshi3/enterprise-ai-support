from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Enterprise AI Support Assistant is running"
    }
    
    
    
@app.get("/chat")
def  chat():
    return {
        "message":"Chat point is working"
    }