# Hands-on Pertemuan 6: JavaScript Generasi Baru

Memoles aplikasi P5 dengan fitur ES6+: metode array, class, module, lalu mengambil data JSON secara asinkron lengkap dengan keadaan memuat dan error.

| Tingkat | Waktu | Yang dilatih | Sub-CPMK |
|---|---|---|---|
| Tingkat 1, Dasar | 10 menit | arrow function, template literal, map, filter, reduce, destructuring | 6.1 |
| Tingkat 2, Menengah | 15 menit | class dengan method, module export dan import | 6.1 |
| Tingkat 3, Tantangan | 10 menit | fetch dengan async dan await, keadaan memuat dan error | 6.2 |
| Pengayaan | sisa | `Promise.all` untuk dua request sekaligus | 6.2 |

Soal ada di `Lembar Hands-on P6.pdf`. Setelah setiap tingkat, tukar laptop dengan teman sebelah untuk saling memeriksa sebelum lanjut. Berkas awal ada di `starter/`; salin foldernya, lalu kerjakan bagian bertanda `TODO`. Angka $A$ adalah digit terakhir NIM (kalau 0, pakai 5) dan $B$ digit kedua dari belakang (kalau 0, pakai 3).

## Persiapan

Module dan fetch tidak jalan dari `file://`. Dari dalam folder `starter/` jalankan `python -m http.server 8080` lalu buka `http://localhost:8080`, atau pakai Live Server di VS Code.

Solusi rujukan (`solusi/`) dan kunci (`kunci/`) dipegang pengajar dan tidak ikut di repo.
