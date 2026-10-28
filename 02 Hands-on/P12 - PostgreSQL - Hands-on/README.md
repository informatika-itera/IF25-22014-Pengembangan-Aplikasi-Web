# Hands-on Pertemuan 12: Basis Data PostgreSQL

Membuat basis data KRS di PostgreSQL, menulis query SQL dengan JOIN dan GROUP BY, lalu mengganti list Python di API P11 dengan SQLAlchemy dan migrasi Alembic.

| Tingkat | Waktu | Yang dilatih | Sub-CPMK |
|---|---|---|---|
| Tingkat 1, Dasar | 10 menit | SELECT, WHERE, ORDER BY, INSERT, UPDATE di psql | 12.1 |
| Tingkat 2, Menengah | 15 menit | JOIN tiga tabel, GROUP BY, HAVING | 12.1 |
| Tingkat 3, Tantangan | 10 menit | FastAPI dengan SQLAlchemy menggantikan list Python | 12.2 |
| Pengayaan | sisa | migrasi dengan Alembic | 12.2 |

Soal ada di `Lembar Hands-on P12.pdf`. Setelah setiap tingkat, tukar laptop dengan teman sebelah untuk saling memeriksa sebelum lanjut. Berkas awal ada di `starter/`; salin foldernya, lalu kerjakan bagian bertanda `TODO`. Angka $A$ adalah digit terakhir NIM (kalau 0, pakai 5) dan $B$ digit kedua dari belakang (kalau 0, pakai 3).

## Persiapan

Buat basis data `krs_NIM` dan pengguna sendiri. Jalankan `psql -d krs_NIM -f schema.sql` lalu `-f seed.sql` dari folder `starter/`. Salin `.env.example` menjadi `.env` dan isi `DATABASE_URL`. Pasang pustaka dengan `pip install -r requirements.txt`.

Solusi rujukan (`solusi/`) dan kunci (`kunci/`) dipegang pengajar dan tidak ikut di repo.
