# Hands-on Pertemuan 1: Cara Kerja Web

Hands-on ini dipakai di fase Hands-on (35 menit) Pertemuan 1 Pengembangan Aplikasi Web (IF25-22014, ITERA). Materinya ada di slide `01 Slide/P1 Bagaimana Aplikasi Web Bekerja.pdf` dan modul `03 Modul/Modul 01 - Bagaimana Aplikasi Web Bekerja.pdf`.

Belum ada kode yang ditulis minggu ini. Kalian membongkar percakapan antara browser dan server memakai tiga alat yang sudah ada di laptop: DevTools di browser, perintah `nslookup` dan `curl` di terminal, serta server bawaan Python untuk pengayaan.

| Tingkat | Waktu | Yang dilatih | Sub-CPMK |
|---|---|---|---|
| 1, Dasar | 10 menit | membongkar URL dengan angka dari NIM, `nslookup` untuk dua host | 1.1 |
| 2, Menengah | 15 menit | tab Network: lima request, header response, muat ulang biasa dan paksa | 1.2 |
| 3, Tantangan | 10 menit | `curl -I` untuk http, https, dan halaman yang tidak ada | 1.1 dan 1.2 |
| Pengayaan | sisa waktu | `python -m http.server` dan membaca log request | 1.2 |

Soal ada di `Lembar Hands-on P1.pdf`. Angka $A$ adalah digit terakhir NIM (kalau 0, pakai 5) dan $B$ digit kedua dari belakang (kalau 0, pakai 3); port kalian adalah angka 8, 0, lalu $A$ dan $B$, misalnya 8072 untuk $A=7$ dan $B=2$.

## Persiapan

Pakai Chrome, Edge, atau Firefox di laptop. DevTools dibuka dengan F12 atau klik kanan lalu Inspect. `nslookup` dan `curl` sudah tersedia di Windows 10 ke atas, macOS, dan Linux. Untuk pengayaan, pastikan `python --version` (atau `python3 --version`) menampilkan Python 3.

## Satu aturan keamanan

Jangan memotret atau menyalin nilai `Cookie`, `Set-Cookie`, atau token apa pun, terutama saat membuka aplikasi yang memerlukan login. Nilai itu sama dengan kunci akun kalian. Tutup nilainya sebelum tangkapan layar dikumpulkan.

Kunci jawaban dipegang pengajar di folder `kunci/` dan tidak ikut di repo.
