from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API KRS dengan PostgreSQL")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])

# TODO: GET /matkul dan POST /matkul memakai basis data (409 bila kode sudah ada)
