from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.post("/auth/signup")
def sign_up():
    return


@app.post("/auth/signin")
def sign_in():
    return


@app.post("/auth/refresh")
def refresh_token():
    return

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)