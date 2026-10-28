INSERT INTO mahasiswa (nim, nama) VALUES
  ('124140101', 'Rani'), ('124140102', 'Bima'), ('124150103', 'Sari');
INSERT INTO matkul (kode, nama, sks) VALUES
  ('IF25-22014', 'Pengembangan Aplikasi Web', 3),
  ('IF25-22017', 'Pengembangan Aplikasi Mobile', 3),
  ('IF25-21012', 'Basis Data', 3),
  ('IF25-21020', 'Jaringan Komputer', 3),
  ('IF25-21099', 'Kerja Praktik', 2);
INSERT INTO krs (mahasiswa_id, matkul_id, semester) VALUES
  (1, 1, 3), (1, 2, 3), (1, 3, 3), (2, 1, 3), (2, 4, 3), (3, 3, 3);
