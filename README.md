# IF25-22014 Pengembangan Aplikasi Web

Pengembangan Aplikasi Web melatih mahasiswa Teknik Informatika membangun aplikasi web utuh: sisi client dengan HTML, CSS, JavaScript, dan React (dijalankan dengan Next.js), sisi server dengan Python dan FastAPI, basis data PostgreSQL, sampai integrasi AI. Separuh pertama semester membangun sisi client, separuh kedua sisi server, lalu keduanya disambung dalam proyek kelompok.

Setiap pertemuan punya tiga bahan yang saling melengkapi: slide di `01 Slide/` untuk kelas, hands-on di `02 Hands-on/` untuk latihan bertingkat, dan modul di `03 Modul/` untuk belajar mandiri.

## Identitas Mata Kuliah

| Data | Deskripsi |
|---|---|
| Kode | IF25-22014 |
| Nama | Pengembangan Aplikasi Web |
| Bobot | 3 SKS (2 teori, 1 praktikum), 16 pertemuan × 150 menit |
| Rumpun | Rekayasa Perangkat Lunak dan Sistem Informasi |
| Program Studi | S1 Teknik Informatika, Institut Teknologi Sumatera |
| Bahasa dan alat | HTML, CSS, JavaScript, React dengan Next.js, Python, FastAPI, PostgreSQL; VS Code, browser dengan DevTools, GitHub |
| Rujukan | Dokumentasi resmi React, Next.js, FastAPI, dan PostgreSQL; Algifari dkk., *Dasar-Dasar Pemrograman Web dengan Kerangka Kerja Python Pyramid dan React JS*, ITERA Press, 2024, untuk dasar HTML, CSS, JavaScript, dan Python |
| Tim pengajar | Tim Pengajar Pengembangan Aplikasi Web, Program Studi Teknik Informatika ITERA |
| Tahun | 2026 |

## Capaian Pembelajaran

**CPL05.** Mampu menganalisis dan menerapkan konsep rekayasa perangkat lunak untuk pengembangan sistem cerdas secara profesional.

| CPMK | Deskripsi | Bobot |
|---|---|---|
| CPMK0501 | Mahasiswa mampu **menerapkan** konsep pemrograman untuk pengembangan perangkat lunak | 65 |
| CPMK0502 | Mahasiswa mampu **menjelaskan** konsep pemrograman untuk pengembangan perangkat lunak | 29 |
| CPMK0503 | Mahasiswa mampu **menerapkan** teknologi sistem cerdas dalam pengembangan perangkat lunak | 6 |

Setiap pertemuan menurunkan CPMK menjadi Sub-CPMK n.1 dan n.2. Daftar lengkapnya ada di RPS.

## Siklus Setiap Pertemuan

| Fase | Waktu | Isi |
|---|---|---|
| Pembuka | 15 menit | Soal dari pertemuan sebelumnya dan masalah minggu ini |
| Coba dulu | 20 menit | Misi yang dikerjakan sebelum ada penjelasan |
| Materi | 50 menit | Pola tebak lalu buktikan, contoh lengkap ke setengah jadi ke mandiri, dua atau tiga pertanyaan engsel |
| Hands-on | 35 menit | Latihan bertingkat di `02 Hands-on/` |
| Papan | 20 menit | Presentasi hasil hands-on dengan rubrik |
| Exit ticket | 10 menit | Satu soal per Sub-CPMK dan satu kalimat refleksi, tanpa catatan |

## Peta 16 Pertemuan

Urutan mengikuti Kontrak Kuliah dan RPS, dengan stack yang diperbarui: React JS tetap, dijalankan dengan Next.js; FastAPI menggantikan Pyramid. Kolom Sisi menunjukkan bagian aplikasi web yang dibangun.

Arsitektur proyek: halaman React di Next.js (`localhost:3000`) memanggil API FastAPI (`localhost:8000`) yang menyimpan data di PostgreSQL.

| Pertemuan | Topik | Sisi | CPMK |
|---|---|---|---|
| P1 | Bagaimana Aplikasi Web Bekerja | client dan server | 0502 |
| P2 | Mengenal HTML | client | 0502 |
| P3 | Mengenal CSS | client | 0501 |
| P4 | Tabel, Formulir, Layout, dan Web Media | client | 0501 |
| P5 | Pemrograman JavaScript | client | 0502 |
| P6 | JavaScript Generasi Baru | client | 0502 |
| P7 | Kerangka Kerja React JS | client | 0502 |
| P8 | **Ujian Tengah Semester** | | 0501 dan 0502 |
| P9 | Pemrograman Python | server | 0502 |
| P10 | OOP di Python | server | 0502 |
| P11 | Kerangka Kerja FastAPI | server | 0502 |
| P12 | Basis Data PostgreSQL | server | 0501 |
| P13 | AI pada Aplikasi Web | client dan server | 0503 |
| P14 | Proyek: iterasi sisi server | proyek | 0501 |
| P15 | Proyek: iterasi sisi client | proyek | 0501 |
| P16 | **Presentasi akhir proyek (UAS)** dan remedial | proyek | 0501 |

## Penilaian

Bobot komponen mengikuti Kontrak Kuliah; pembagian ke CPMK mengikuti tabel penilaian di RPS.

| Komponen | Pelaksanaan | Bobot | CPMK0501 | CPMK0502 | CPMK0503 |
|---|---|---|---|---|---|
| Praktikum | hands-on yang diamati di kelas | 20% | 3 | 14 | 3 |
| Tugas individu | analisis tertulis, dikumpulkan PDF | 10% | 2 | 5 | 3 |
| UTS | P8, tes tertulis | 20% | 10 | 10 | 0 |
| Proyek aplikasi web | kelompok, iterasi P14 dan P15, presentasi akhir P16 | 50% | 50 | 0 | 0 |
| **Total** | | **100%** | **65** | **29** | **6** |

Kehadiran minimal 80% menjadi syarat ikut proyek, kecuali ada surat keterangan resmi. Protes nilai dilayani paling lama satu hari setelah nilai keluar. Presentasi papan dan tugas dinilai dengan rubrik empat level (Sangat baik 75 sampai 100, Baik 65 sampai 74, Cukup 55 sampai 64, Kurang di bawah 55) pada tiga kriteria: ketepatan langkah, alasan tiap langkah, dan menjawab pertanyaan. Konversi nilai huruf mengikuti Kontrak Kuliah (A mulai 75).

**Penggunaan AI.** Boleh dipakai saat hands-on, tugas, dan proyek untuk memahami pesan error atau konsep, tidak untuk meminta solusi utuh yang tidak bisa dijelaskan sendiri. Exit ticket dan UTS dikerjakan tanpa AI.

**Angka dari NIM.** Soal memakai $A$ (digit terakhir NIM, 0 menjadi 5) dan $B$ (digit kedua dari belakang, 0 menjadi 3) untuk port, data, dan nama berkas, sehingga setiap mahasiswa punya versi soal sendiri.

## Bahan per Pertemuan

| P | Slide | Hands-on atau dokumen | Modul |
|---|---|---|---|
| P1 | `01 Slide/P1 Bagaimana Aplikasi Web Bekerja.pdf` | `02 Hands-on/P1 - Cara Kerja Web - Hands-on/` | `03 Modul/Modul 01 - Bagaimana Aplikasi Web Bekerja.pdf` |
| P2 | `01 Slide/P2 Mengenal HTML.pdf` | `02 Hands-on/P2 - HTML - Hands-on/` | `03 Modul/Modul 02 - Mengenal HTML.pdf` |
| P3 | `01 Slide/P3 Mengenal CSS.pdf` | `02 Hands-on/P3 - CSS - Hands-on/` | `03 Modul/Modul 03 - Mengenal CSS.pdf` |
| P4 | `01 Slide/P4 Tabel, Formulir, Layout, dan Web Media.pdf` | `02 Hands-on/P4 - Tabel Formulir Layout - Hands-on/` | `03 Modul/Modul 04 - Tabel, Formulir, Layout, dan Web Media.pdf` |
| P5 | `01 Slide/P5 Pemrograman JavaScript.pdf` | `02 Hands-on/P5 - JavaScript - Hands-on/` | `03 Modul/Modul 05 - Pemrograman JavaScript.pdf` |
| P6 | `01 Slide/P6 JavaScript Generasi Baru.pdf` | `02 Hands-on/P6 - ES6 dan Async - Hands-on/` | `03 Modul/Modul 06 - JavaScript Generasi Baru.pdf` |
| P7 | `01 Slide/P7 Kerangka Kerja React JS.pdf` | `02 Hands-on/P7 - React JS - Hands-on/` | `03 Modul/Modul 07 - Kerangka Kerja React JS.pdf` |
| P8 | `01 Slide/P8 Ujian Tengah Semester.pdf` | `04 Ujian/UTS - Kisi-kisi.pdf`, `04 Ujian/UTS - Contoh Soal.pdf` |  |
| P9 | `01 Slide/P9 Pemrograman Python.pdf` | `02 Hands-on/P9 - Python - Hands-on/` | `03 Modul/Modul 09 - Pemrograman Python.pdf` |
| P10 | `01 Slide/P10 OOP di Python.pdf` | `02 Hands-on/P10 - OOP Python - Hands-on/` | `03 Modul/Modul 10 - OOP di Python.pdf` |
| P11 | `01 Slide/P11 Kerangka Kerja FastAPI.pdf` | `02 Hands-on/P11 - FastAPI - Hands-on/` | `03 Modul/Modul 11 - Kerangka Kerja FastAPI.pdf` |
| P12 | `01 Slide/P12 Basis Data PostgreSQL.pdf` | `02 Hands-on/P12 - PostgreSQL - Hands-on/` | `03 Modul/Modul 12 - Basis Data PostgreSQL.pdf` |
| P13 | `01 Slide/P13 AI pada Aplikasi Web.pdf` | `02 Hands-on/P13 - AI - Hands-on/` | `03 Modul/Modul 13 - AI pada Aplikasi Web.pdf` |
| P14 | `01 Slide/P14 Proyek - Iterasi Sisi Server.pdf` | `05 Proyek/Panduan Proyek.pdf`, `05 Proyek/Rubrik Proyek.pdf` |  |
| P15 | `01 Slide/P15 Proyek - Iterasi Sisi Client.pdf` | `05 Proyek/` |  |
| P16 | `01 Slide/P16 Presentasi Akhir Proyek.pdf` | `05 Proyek/Rubrik Proyek.pdf` |  |

Setiap folder hands-on berisi `README.md`, `Lembar Hands-on Pn.pdf`, dan berkas awal di `starter/` bertanda `TODO`. Setiap slide memuat outline yang bisa diklik dan animasi; versi PowerPoint beranimasi dengan catatan pengajar dibagikan terpisah.

## Cara Mengikuti Materi

Setiap pertemuan disusun agar tidak ada yang tertinggal:

| Penanda | Artinya |
|---|---|
| Slide *Perjalanan kalian hari ini* | peta enam fase pertemuan: yang dilakukan, pertanyaan yang wajar muncul, dan yang dilakukan bila tersendat |
| *Fase 3 dari 6* atau *Bagian 2 dari 6, slide 3 dari 4* di atas judul | posisi kalian saat ini; di PowerPoint, tombol *Outline* kembali ke daftar bagian |
| Kotak gelap *Definisi* | kalimat inti yang harus bisa diulang dengan kata sendiri |
| Kotak merah *Tebak dulu*, lalu hijau *Jawaban* | tulis dugaan sebelum jawaban dibuka |
| *Ikuti bersama* | ketik di laptop sekarang, satu langkah setiap klik; ada *Yang harus terlihat* dan *Kalau berbeda* |
| *Periksa berpasangan* di lembar hands-on | tukar laptop dengan teman sebelah sebelum lanjut ke tingkat berikutnya |

## Proyek

Proyek kelompok (2 sampai 3 orang, 50% nilai akhir) membangun satu aplikasi web utuh dengan React (Next.js), FastAPI, dan PostgreSQL. Tahapannya: pembentukan kelompok dan tema di P9, rancangan di P12, demo iterasi server di P14, demo iterasi client di P15, dan presentasi akhir di P16. Rincian kebutuhan, daftar tema, jadwal, dan rubrik ada di `05 Proyek/`.

## Struktur Repo

```
.
├── README.md
├── 01 Slide/          # slide PDF per pertemuan
├── 02 Hands-on/       # per pertemuan: README, lembar soal, starter/
├── 03 Modul/          # modul belajar mandiri PDF
├── 04 Ujian/          # kisi-kisi dan contoh soal UTS
└── 05 Proyek/         # panduan dan rubrik proyek
```

Kunci hands-on dan ujian (`kunci/`), solusi rujukan (`solusi/`), dan sumber bahan (`src/`) disimpan tim pengajar dan tercantum di `.gitignore`, sehingga tidak ikut ter-commit. Versi PowerPoint setiap slide, lengkap dengan catatan pengajar, dibagikan terpisah.
