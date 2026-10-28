# Hands-on Pertemuan 13: AI pada Aplikasi Web

Menambahkan fitur ringkas pengumuman: endpoint FastAPI yang memanggil model bahasa dengan kunci aman, keluaran JSON yang divalidasi Pydantic, lalu antarmuka Next.js dengan keadaan memuat, tombol batal, label AI, dan hasil yang bisa diedit.

| Tingkat | Waktu | Yang dilatih | Sub-CPMK |
|---|---|---|---|
| Tingkat 1, Dasar | 10 menit | endpoint dengan model masukan dan keluaran dalam mode tiruan | 13.2 |
| Tingkat 2, Menengah | 15 menit | memanggil model sungguhan, prompt sistem, validasi JSON, dan 502 | 13.1, 13.2 |
| Tingkat 3, Tantangan | 10 menit | antarmuka Next.js: memuat, batal, label AI, edit, galat | 13.2 |
| Pengayaan | sisa | batas permintaan dan umpan balik pengguna | 13.1 |

Soal ada di `Lembar Hands-on P13.pdf`. Setelah setiap tingkat, tukar laptop dengan teman sebelah untuk saling memeriksa sebelum lanjut. Berkas awal ada di `starter/`; salin foldernya, lalu kerjakan bagian bertanda `TODO`. Angka $A$ adalah digit terakhir NIM (kalau 0, pakai 5) dan $B$ digit kedua dari belakang (kalau 0, pakai 3).

## Persiapan

Salin `.env.example` menjadi `.env`. Tanpa model, isi `LLM_MODE=tiruan` agar endpoint membalas contoh tetap. Dengan Ollama: pasang Ollama, jalankan `ollama pull llama3.2`, isi `LLM_BASE_URL=http://localhost:11434/v1`. Dengan penyedia berbayar: isi alamat, model, dan kunci dari dokumentasinya.

Solusi rujukan (`solusi/`) dan kunci (`kunci/`) dipegang pengajar dan tidak ikut di repo.
