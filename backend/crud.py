from sqlalchemy.orm import Session
import models, schemas

def create_agent(db: Session, agent: schemas.AgentCreate):
    db_agent = models.Agent(name=agent.name, description=agent.description)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def get_agent(db: Session, agent_name: str):
    return db.query(models.Agent).filter(models.Agent.name == agent_name).first()

def update_agent(db: Session, agent_name: str, agent_data: schemas.AgentCreate):
    db_agent = db.query(models.Agent).filter(models.Agent.name == agent_name).first()
    if db_agent:
        db_agent.description = agent_data.description
        db.commit()
        db.refresh(db_agent)
    return db_agent

def delete_agent(db: Session, agent_name: str):
    db_agent = db.query(models.Agent).filter(models.Agent.name == agent_name).first()
    if db_agent:
        db.delete(db_agent)
        db.commit()
    return db_agent
