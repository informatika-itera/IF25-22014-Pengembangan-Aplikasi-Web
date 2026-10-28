CREATE TABLE mahasiswa (
  id SERIAL PRIMARY KEY,
  nim CHAR(9) UNIQUE NOT NULL,
  nama TEXT NOT NULL
);
CREATE TABLE matkul (
  id SERIAL PRIMARY KEY,
  kode VARCHAR(12) UNIQUE NOT NULL,
  nama TEXT NOT NULL,
  sks INT NOT NULL CHECK (sks BETWEEN 1 AND 6)
);
CREATE TABLE krs (
  mahasiswa_id INT REFERENCES mahasiswa(id) ON DELETE CASCADE,
  matkul_id INT REFERENCES matkul(id),
  semester INT NOT NULL,
  PRIMARY KEY (mahasiswa_id, matkul_id, semester)
);
