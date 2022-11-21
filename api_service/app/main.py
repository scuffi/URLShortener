import uvicorn
from fastapi import FastAPI, Request, HTTPException, status

from routers import api_router

# Instantiate our API object
app = FastAPI()

# Add the router which adds our functionality to an endpoint
app.include_router(api_router)

# Define a list of all our statically-defined endpoints
all_endpoints = [route.path for route in app.routes]

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=3000, reload=True)