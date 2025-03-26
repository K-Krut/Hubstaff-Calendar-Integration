from fastapi import FastAPI
from routes import calendar
app = FastAPI()

app.include_router(calendar.router, prefix="/api/calendar", tags=["calendar"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)