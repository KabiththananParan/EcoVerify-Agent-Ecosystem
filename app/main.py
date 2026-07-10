from fastapi import FastAPI
from pydantic import BaseModel


class VerificationInput(BaseModel):
    claim: str
    sources:list[str] | None = None


# Add MetaData
app = FastAPI(
    title="EcoVerify Agent Ecosystem",
    version="0.1.0",
    description="Multi-Agent AI Verification System"
)

@app.get("/")
def read_root():
    return{
        "name": "EcoVerify Agent Ecosystem",
        "version": "0.1.0",
        "status": "running"
    }
    
@app.get("/health")
def get_health():
    return{
        "status": "healthy",
        "service": "EcoVerify Agent Ecosystem"
    }
    
    
@app.post("/verify")
def verify(request : VerificationInput):
    return request

