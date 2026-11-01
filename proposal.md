# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

Mata kuliah: Algoritma dan Pemrograman (S1 Pendidikan Matematika FKIP Untirta, 2026/2027 Ganjil)
Dosen pengampu: Dr. Aan Hendrayana, S.Si., M.Pd.
Penyusun: Rasyad Fazri Mulyono (NIM 2225250023), kelas 3A
Asesmen: Proposal Proyek (Pertemuan 14, bobot 5%) dan Proyek Akhir (Pertemuan 15, bobot 10%)

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas (versi console, Python).

## 2. Latar Belakang

Setelah ulangan atau kuis, guru matematika harus menghitung rata-rata, nilai tertinggi dan terendah, lalu menentukan siswa yang sudah dan belum mencapai KKM. Jika dilakukan manual, proses ini lambat dan mudah salah hitung, apalagi bila data tercampur nilai yang salah ketik (misalnya 105 atau huruf). Program sederhana yang membaca data dari file, memvalidasinya, dan menghasilkan laporan akan mempercepat rekap dan membuat hasilnya konsisten.

Pernyataan masalah: guru matematika membutuhkan program console untuk membaca data nilai dari file, menghitung statistik kelas, menentukan status ketuntasan, dan menyimpan laporan ringkas sehingga rekap dapat dilakukan lebih cepat dan konsisten.

## 3. Pengguna dan Tujuan

- Pengguna utama: guru matematika (SMP/SMA) yang menyimpan nilai siswa dalam file teks.
- Tujuan: memperoleh statistik kelas dan status ketuntasan secara otomatis, serta laporan yang dapat disimpan.

User story: sebagai guru matematika, saya ingin membaca data nilai siswa dari file, agar saya mendapat statistik dan status ketuntasan secara otomatis.

## 4. Ruang Lingkup

Fitur wajib:
1. Membaca file nilai (format `nama,nilai`).
2. Memvalidasi nilai pada rentang 0 sampai 100.
3. Menghitung rata-rata, minimum, maksimum.
4. Menentukan status Tuntas/Belum Tuntas berdasarkan KKM (default 75) dan menghitung jumlahnya.
5. Menyimpan laporan ke file teks.

Fitur tambahan (hanya bila fitur wajib stabil): statistik per kategori nilai.

Batasan: berbasis terminal, tanpa antarmuka grafis/web, tanpa layanan eksternal, data contoh fiktif.

## 5. Kebutuhan

| ID | Kebutuhan fungsional | Prioritas |
|----|----------------------|-----------|
| F01 | Program dapat membaca data nilai | Wajib |
| F02 | Program dapat memvalidasi nilai 0-100 | Wajib |
| F03 | Program menghitung rata-rata, minimum, maksimum | Wajib |
| F04 | Program menentukan status tuntas/belum tuntas | Wajib |
| F05 | Program menyimpan laporan | Wajib |
| F06 | Statistik per kategori | Tambahan |

Kebutuhan nonfungsional: mudah dijalankan dari terminal VS Code; pesan kesalahan mudah dipahami; nama fungsi dan variabel jelas; data contoh tanpa informasi pribadi nyata; dapat diuji ulang dengan test case yang sama.

## 6. Input, Proses, Output (IPO)

| Input | Proses | Output |
|-------|--------|--------|
| File teks berisi baris `nama,nilai` (argumen opsional, default `data/nilai_contoh.txt`) | Baca file, validasi tiap baris, simpan ke list of dictionary, hitung statistik, klasifikasi ketuntasan | Ringkasan di layar (jumlah, rata-rata, min, max, jumlah tuntas/belum tuntas, daftar baris bermasalah) dan `output/laporan.txt` |

## 7. Algoritma (Pseudocode)

```
MULAI
  baca data dari file
  jika file tidak ditemukan:
    tampilkan pesan error
    SELESAI
  untuk setiap baris data:
    abaikan baris kosong dan komentar (#)
    validasi format dan nilai
    jika valid: simpan ke daftar data
    jika tidak: catat pesan kesalahan beserta nomor baris
  jika tidak ada data valid:
    tampilkan pesan
    SELESAI
  hitung statistik (jumlah, rata-rata, min, max)
  tentukan status ketuntasan tiap siswa berdasarkan KKM
  tampilkan ringkasan
  simpan laporan
SELESAI
```

Cek konsistensi: setiap input memiliki langkah pemrosesan, setiap kondisi penting (file hilang, data kosong, baris salah) punya tindakan, dan alur menghasilkan semua output yang dijanjikan.

## 8. Struktur Program

| Fungsi | Modul | Tanggung jawab | Input | Output |
|--------|-------|----------------|-------|--------|
| `baca_data(path)` | data_io.py | Membaca file, memvalidasi baris | path | (list data valid, list kesalahan) |
| `simpan_laporan(teks, path)` | data_io.py | Menulis laporan ke file | teks, path | file |
| `validasi_nilai(nilai)` | analisis.py | Memeriksa rentang 0-100 | nilai | bool |
| `hitung_statistik(data)` | analisis.py | Ringkasan statistik | data | dictionary |
| `tentukan_status(nilai, kkm)` | analisis.py | Status ketuntasan satu nilai | nilai, kkm | string |
| `hitung_ketuntasan(data, kkm)` | analisis.py | Jumlah tuntas dan belum tuntas | data, kkm | tuple |
| `buat_laporan(...)` | analisis.py | Menyusun teks laporan | data, statistik, kesalahan | string |
| `main(argv)` | main.py | Mengatur alur program | argumen | kode keluar |

Struktur folder:

```
proyek-akhir-rekap-nilai/
|-- README.md
|-- proposal.md
|-- .gitignore
|-- data/
|   |-- nilai_contoh.txt
|   `-- nilai_bermasalah.txt
|-- src/
|   |-- main.py
|   |-- data_io.py
|   |-- analisis.py
|   `-- utilitas.py
|-- tests/
|   |-- test_case.md
|   |-- jalankan_tes.py
|   `-- hasil_uji.md
|-- docs/
|   `-- bug_log.md
`-- output/
    `-- .gitkeep
```

## 9. Struktur Data

| Kebutuhan | Struktur | Alasan |
|-----------|----------|--------|
| Kumpulan data siswa | list of dictionary `{"nama": str, "nilai": float}` | Menyimpan beberapa atribut dan mudah diiterasi |
| Ringkasan statistik | dictionary | Akses berdasarkan key (`jumlah`, `rata_rata`, `minimum`, `maksimum`) |
| Daftar kesalahan | list of string | Mudah ditampilkan dan dihitung |
| Teks laporan | string | Mudah diformat dan ditulis ke file |

## 10. Test Case (dirancang sebelum implementasi)

| ID | Kategori | Input/Kondisi | Expected |
|----|----------|---------------|----------|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80.0 |
| TC02 | Batas | Nilai 0 | Diterima |
| TC03 | Batas | Nilai 100 | Diterima |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ada | Pesan jelas, tanpa crash |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas = jumlah data |
| TC07 | Batas | Nilai 75 dan 74 (KKM 75) | 75 Tuntas, 74 Belum Tuntas |
| TC08 | Invalid | Nilai teks `abc` | Ditolak, program tidak error |
| TC09 | Kosong | File tanpa data | Pesan jelas, tanpa ZeroDivisionError |
| TC10 | File | Data valid | Laporan tersimpan di file |
| TC11 | Kosong | List kosong ke `hitung_statistik` | Rata-rata 0, min/max None |
| TC12 | Integrasi | Data contoh proyek | Seluruh alur berjalan |
| TC13 | Campuran | Baris valid, teks, kosong, 105 | Hanya baris valid dihitung, kesalahan tercatat |
| TC14 | Invalid | Baris tanpa koma | Ditolak dengan nomor baris |

Definition of Done: semua fitur wajib berjalan, semua test case wajib lulus, error yang sudah diprediksi tidak menghentikan program, output mudah dibaca, README menjelaskan cara menjalankan, commit menunjukkan proses kerja.

## 11. Pembagian Tugas

Proyek dikerjakan perorangan, sehingga satu orang memegang beberapa peran (sesuai catatan modul: satu orang boleh memegang lebih dari satu peran, asalkan setiap tugas punya PIC).

| Peran | Tanggung jawab | Bukti | PIC |
|-------|----------------|-------|-----|
| Koordinator | Menjaga ruang lingkup dan integrasi | proposal.md | Rasyad |
| Programmer Data I/O | Baca/tulis file dan validasi baris | data_io.py | Rasyad |
| Programmer Logika | Statistik dan klasifikasi | analisis.py | Rasyad |
| Tester/QA | Menyusun dan menjalankan test case | tests/ | Rasyad |
| Dokumentasi | README dan catatan penggunaan | README.md | Rasyad |

## 12. Jadwal Milestone

| Waktu | Target |
|-------|--------|
| Pertemuan 14 | Proposal, struktur repo, pseudocode, test case, pembagian tugas |
| Antara P14-P15 | Implementasi awal fitur wajib |
| Pertemuan 15 | Integrasi, testing, debugging, dokumentasi |
| Pertemuan 16 | Presentasi, demonstrasi, evaluasi/UAS |

## 13. Repository

URL repository GitHub: https://github.com/RasyadFazriM-31/proyek-akhir-rekap-nilai (aktif setelah push).
