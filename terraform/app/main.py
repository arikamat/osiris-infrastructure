from fastapi import FastAPI
from app.api.endpoints import terraform_actions, state_actions, creation_destruction

app = FastAPI(
    title = "Team 9 - Terraform Scripts and Infrastructure Management"
)

app.include_router(terraform_actions.router)
app.include_router(state_actions.router)
app.include_router(creation_destruction.router)
