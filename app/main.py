from fastapi import FastAPI

from app.endpoints.router import router as router_1

app = FastAPI(
    title="Middle test"
)



app.include_router(router_1)




