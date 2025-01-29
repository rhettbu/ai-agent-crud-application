from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/agents/", response_model=schemas.AgentResponse)
async def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    return crud.create_agent(db=db, agent=agent)

@app.get("/agents/{name}", response_model=schemas.AgentResponse)
async def get_agent(name: str, db: Session = Depends(get_db)):
    agent = crud.get_agent(db, name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@app.put("/agents/{name}", response_model=schemas.AgentResponse)
async def update_agent(name: str, agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    updated_agent = crud.update_agent(db, name, agent)
    if not updated_agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return updated_agent

@app.delete("/agents/{name}")
async def delete_agent(name: str, db: Session = Depends(get_db)):
    deleted_agent = crud.delete_agent(db, name)
    if not deleted_agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"message": "Agent deleted successfully"}
