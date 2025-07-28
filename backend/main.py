from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router  # Custom API routes

app = FastAPI(
    title="Job Portal API",
    description="Backend for the Job Portal",
    version="1.0.0",
)

# Allow all origins for now — secure this in production!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root test route
@app.get("/")
def read_root():
    return {"message": "Job Portal Backend is running 🚀"}

# Include all API routes
app.include_router(router)

