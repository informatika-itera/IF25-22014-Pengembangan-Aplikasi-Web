from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API KRS")

DATA: list[dict] = [
    {"kode": "IF25-22014", "nama": "Pengembangan Aplikasi Web", "sks": 3},
    {"kode": "IF25-22017", "nama": "Pengembangan Aplikasi Mobile", "sks": 3},
    {"kode": "IF25-21012", "nama": "Basis Data", "sks": 3},
    {"kode": "IF25-21099", "nama": "Kerja Praktik", "sks": 2},
]

@app.get("/")
def beranda():
    return {"pesan": "API KRS berjalan"}

# TODO 1: GET /matkul dengan query sks (opsional) dan batas (bawaan 5 + A)
# TODO 2: GET /matkul/{kode}, 404 bila tidak ada
# TODO 3: model MatkulIn dan POST /matkul (201, 409 bila kode sudah ada)
# TODO 4: PUT /matkul/{kode} dan DELETE /matkul/{kode} (204)
# TODO tingkat 3: CORSMiddleware untuk http://localhost:3000
