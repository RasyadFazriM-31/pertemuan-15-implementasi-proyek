# Hasil Eksekusi Test Case

| ID | Kategori | Input/Kondisi | Expected | Actual | Status |
|----|----------|---------------|----------|--------|--------|
| TC01 | Normal | Nilai 80, 70, 90 | rata-rata 80.0 | rata-rata 80.0 | PASS |
| TC02 | Batas | Nilai 0 | diterima: 1 data, 0 kesalahan | diterima: 1 data, 0 kesalahan | PASS |
| TC03 | Batas | Nilai 100 | diterima: 1 data, 0 kesalahan | diterima: 1 data, 0 kesalahan | PASS |
| TC04 | Invalid | Nilai 105 | ditolak: 0 data, 1 kesalahan | ditolak: 0 data, 1 kesalahan | PASS |
| TC05 | Invalid | File tidak ada | kode 1, file tidak ditemukan | kode 1, file tidak ditemukan | PASS |
| TC06 | Normal | Nilai 80, 90, 75 (KKM 75) | tuntas 3 dari 3 | tuntas 3 dari 3 | PASS |
| TC07 | Batas | Nilai 75 dan 74 (KKM 75) | 75 Tuntas, 74 Belum Tuntas | 75 Tuntas, 74 Belum Tuntas | PASS |
| TC08 | Invalid | Nilai teks abc | ditolak: 0 data, 1 kesalahan | ditolak: 0 data, 1 kesalahan | PASS |
| TC09 | Kosong | File kosong | kode 1, tidak ada data valid | kode 1, tidak ada data valid | PASS |
| TC10 | File | Data valid, simpan laporan | kode 0, laporan berisi rata-rata | kode 0, laporan berisi rata-rata | PASS |
| TC11 | Kosong | List kosong ke hitung_statistik | rata-rata 0, min None, maks None | rata-rata 0, min None, maks None | PASS |
| TC12 | Integrasi | data/nilai_contoh.txt | kode 0, 12 data | kode 0, 12 data | PASS |
| TC13 | Campuran | Valid, abc, baris kosong, 105, valid | 2 valid, 2 kesalahan, rata-rata 75.0 | 2 valid, 2 kesalahan, rata-rata 75.0 | PASS |
| TC14 | Invalid | Baris tanpa koma | ditolak: 0 data, 1 kesalahan | ditolak: 0 data, 1 kesalahan | PASS |

Ringkasan: 14 PASS, 0 FAIL dari 14 test case.
