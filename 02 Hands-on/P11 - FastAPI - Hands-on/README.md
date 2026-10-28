# Hands-on Pertemuan 11: Kerangka Kerja FastAPI

Membangun API mata kuliah dengan FastAPI: GET daftar dan detail, POST dengan validasi Pydantic, PUT dan DELETE, query penyaring, lalu menyambungkannya ke halaman Next.js dari P7 dengan CORS.

| Tingkat | Waktu | Yang dilatih | Sub-CPMK |
|---|---|---|---|
| Tingkat 1, Dasar | 10 menit | path operation, path parameter, query parameter, dan 404 | 11.2 |
| Tingkat 2, Menengah | 15 menit | model Pydantic, POST 201, PUT, DELETE 204, dan 422 | 11.1, 11.2 |
| Tingkat 3, Tantangan | 10 menit | CORS dan menyambungkan Next.js P7 ke API | 11.2 |
| Pengayaan | sisa | APIRouter dan dependency sederhana | 11.1 |

Soal ada di `Lembar Hands-on P11.pdf`. Setelah setiap tingkat, tukar laptop dengan teman sebelah untuk saling memeriksa sebelum lanjut. Berkas awal ada di `starter/`; salin foldernya, lalu kerjakan bagian bertanda `TODO`. Angka $A$ adalah digit terakhir NIM (kalau 0, pakai 5) dan $B$ digit kedua dari belakang (kalau 0, pakai 3).

## Persiapan

Aktifkan venv, jalankan `pip install -r requirements.txt` di `starter/`, lalu `fastapi dev main.py`. Uji setiap endpoint di `http://localhost:8000/docs`. Data disimpan di list Python dan hilang saat server dimatikan; P12 menggantinya dengan PostgreSQL.

Solusi rujukan (`solusi/`) dan kunci (`kunci/`) dipegang pengajar dan tidak ikut di repo.
