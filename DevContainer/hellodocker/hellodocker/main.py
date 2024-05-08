from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"Class":"Wednesday"}

@app.post("/today")
def today(day: str):
    return {f"Day: {day}"}
