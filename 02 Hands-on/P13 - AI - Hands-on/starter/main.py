import os
from typing import Literal
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ValidationError

load_dotenv()
MODE = os.environ.get("LLM_MODE", "tiruan")
app = FastAPI(title="API Ringkas")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])

# TODO 1: model TeksIn (teks 50 sampai 4000 + 100A karakter) dan Ringkasan (poin 1..3, kategori Literal)
#         POST /ringkas: bila MODE == "tiruan", kembalikan Ringkasan contoh

# TODO 2: fungsi async tanya_llm(sistem, isi) dengan httpx ke LLM_BASE_URL/chat/completions,
#         prompt sistem yang meminta JSON, validasi dengan Ringkasan.model_validate_json, 502 bila gagal
