# Program Rekap dan Analisis Nilai Matematika Kelas

Proyek akhir mata kuliah Algoritma dan Pemrograman, S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa, 2026/2027 Ganjil.

## Deskripsi

Guru matematika sering harus merekap nilai ulangan secara manual. Program console berbasis Python ini membaca data nilai dari file teks, memvalidasi isinya, menghitung statistik kelas, menentukan status ketuntasan berdasarkan KKM, dan menyimpan laporan ke file. Pengguna sasaran: guru matematika. Proposal dan rancangan proyek ini ada di folder terpisah `pertemuan-14-proposal-proyek`.

## Fitur

- Membaca file nilai berformat `nama,nilai` (baris kosong dan komentar `#` diabaikan).
- Validasi: nilai harus angka pada rentang 0-100; baris bermasalah dilaporkan dengan nomor barisnya dan tidak menghentikan program.
- Statistik: jumlah data, rata-rata, minimum, maksimum.
- Status Tuntas/Belum Tuntas berdasarkan KKM (default 75) beserta jumlahnya.
- Laporan tersimpan di `output/laporan.txt`.
- Penanganan kondisi khusus: file tidak ada, file kosong, tidak ada data valid.

## Persyaratan

- Python 3.x (diuji dengan Python 3.13). Tidak memerlukan pustaka tambahan.

## Cara Menjalankan

Dari folder induk proyek:

```
git clone <url-repositori>
cd proyek-akhir-rekap-nilai
python3 src/main.py                              # memakai data/nilai_contoh.txt
python3 src/main.py data/nilai_bermasalah.txt    # contoh data dengan baris bermasalah
python3 src/main.py path/ke/file_anda.txt        # data sendiri
```

Format file nilai:

```
# komentar (opsional)
Ayu,85
Budi,78
```

Contoh keluaran (`data/nilai_contoh.txt`):

```
Jumlah data : 12
Rata-rata   : 77.17
Minimum     : 55
Maksimum    : 100
Tuntas      : 7 | Belum tuntas: 5 (KKM 75)
```

Kode keluar: `0` bila berhasil, `1` bila file tidak ditemukan/tidak terbaca atau tidak ada data valid.

## Struktur Folder

```
proyek-akhir-rekap-nilai/
|-- README.md             dokumentasi utama
|-- .gitignore
|-- data/
|   |-- nilai_contoh.txt        data contoh fiktif (12 siswa)
|   `-- nilai_bermasalah.txt    data demo dengan baris tidak valid
|-- src/
|   |-- main.py           alur program dan antarmuka console
|   |-- data_io.py        membaca file + validasi baris, menyimpan laporan
|   |-- analisis.py       validasi nilai, statistik, ketuntasan, teks laporan
|   `-- utilitas.py       konstanta (KKM, rentang nilai, path default)
|-- tests/
|   |-- jalankan_tes.py   penjalan 14 test case
|   |-- test_case.md      deskripsi test case
|   `-- hasil_uji.md      hasil eksekusi terakhir
|-- docs/
|   `-- bug_log.md        catatan bug dan perbaikan
`-- output/               hasil laporan (isi tidak dicommit)
```

## Test Case

Jalankan `python3 tests/jalankan_tes.py`. Ringkasan hasil terakhir: **14 PASS, 0 FAIL**.

| ID | Kategori | Input/Kondisi | Expected | Status |
|----|----------|---------------|----------|--------|
| TC01 | Normal | Nilai 80, 70, 90 | rata-rata 80.0 | PASS |
| TC02 | Batas | Nilai 0 | diterima | PASS |
| TC03 | Batas | Nilai 100 | diterima | PASS |
| TC04 | Invalid | Nilai 105 | ditolak | PASS |
| TC05 | Invalid | File tidak ada | kode 1, pesan jelas | PASS |
| TC06 | Normal | Semua nilai >= KKM | tuntas = jumlah data | PASS |
| TC07 | Batas | Nilai 75 dan 74 (KKM 75) | Tuntas / Belum Tuntas | PASS |
| TC08 | Invalid | Nilai teks `abc` | ditolak tanpa error | PASS |
| TC09 | Kosong | File kosong | pesan jelas, kode 1 | PASS |
| TC10 | File | Data valid | laporan tersimpan | PASS |
| TC11 | Kosong | List kosong ke `hitung_statistik` | rata-rata 0, min/max None | PASS |
| TC12 | Integrasi | `data/nilai_contoh.txt` | 12 data terbaca | PASS |
| TC13 | Campuran | Valid, teks, kosong, 105 | 2 valid, 2 kesalahan | PASS |
| TC14 | Invalid | Baris tanpa koma | ditolak dengan nomor baris | PASS |

Tabel lengkap dengan kolom Actual: [tests/hasil_uji.md](tests/hasil_uji.md). Riwayat bug: [docs/bug_log.md](docs/bug_log.md).

## Known Issues

- Nilai desimal harus memakai titik (`85.5`); format koma (`85,5`) ditolak karena koma adalah pemisah kolom.
- Nama siswa tidak boleh mengandung koma.
- KKM bernilai tetap 75; untuk mengubahnya, ubah `KKM_DEFAULT` di `src/utilitas.py`.
- Fitur tambahan F06 (statistik per kategori) belum diimplementasikan karena berstatus opsional pada proposal.

## Anggota dan Kontribusi

| Nama | NIM | Kontribusi |
|------|-----|-----------|
| Rasyad Fazri Mulyono | 2225250023 | Seluruh peran: koordinator, programmer data I/O dan logika, tester/QA, dokumentasi |

## Referensi/Bantuan

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14 dan 15 (Dr. Aan Hendrayana, S.Si., M.Pd.).
- Python Software Foundation, Python 3 Documentation.
- Bantuan AI (Claude, Anthropic): digunakan untuk menyusun kerangka proposal, kode awal, test case, dan draf dokumentasi. Seluruh isi telah ditinjau dan dapat dijelaskan oleh penyusun.

## Repositori

https://github.com/RasyadFazriM-31/proyek-akhir-rekap-nilai (aktif setelah push)
