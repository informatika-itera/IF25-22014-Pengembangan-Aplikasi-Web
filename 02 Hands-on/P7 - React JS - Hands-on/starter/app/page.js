// TODO 1.2: tampilkan 3 + (A mod 3) KartuMatkul dengan map dan key
// TODO 2: tombol Ambil mata kuliah, total SKS di atas, batas 20 + B SKS (butuh "use client")
// TODO 3: ganti array tetap dengan data dari /matkul.json (useEffect, teks memuat, pesan gagal)
import KartuMatkul from "../components/KartuMatkul";

const matkul = [
  { kode: "IF25-22014", nama: "Pengembangan Aplikasi Web", sks: 3 },
];

export default function Beranda() {
  return (
    <main>
      <h1>Mata kuliah</h1>
    </main>
  );
}
