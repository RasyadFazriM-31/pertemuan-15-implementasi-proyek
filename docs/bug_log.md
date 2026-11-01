# Bug Log

Bug dicatat dari hasil eksekusi nyata `python3 tests/jalankan_tes.py`. Test case ditulis sebelum implementasi (Pertemuan 14), lalu dijalankan pada versi pertama kode (Pertemuan 15).

## Riwayat Eksekusi

| Eksekusi | Kondisi | Hasil |
|----------|---------|-------|
| 1 | Implementasi awal (commit `feat: implementasi awal ...`) | 6 PASS, 8 FAIL |
| 2 | Setelah BUG-06 pada tes diperbaiki | 6 PASS, 8 FAIL (TC05 kini gagal karena penyebab sebenarnya) |
| 3 | Setelah BUG-01 sampai BUG-05 diperbaiki | 13 PASS, 1 FAIL (TC09) |
| 4 | Setelah BUG-07 pada tes diperbaiki | 14 PASS, 0 FAIL |

## Daftar Bug

| ID | Gejala | Test gagal | Penyebab | Perbaikan | Status |
|----|--------|-----------|----------|-----------|--------|
| BUG-01 | Program berhenti dengan `ValueError` saat nilai berupa teks (`abc`) | TC08, TC13 | `float()` dipanggil tanpa penanganan kesalahan | Bungkus dengan `try-except ValueError`; catat pesan "nilai bukan angka" beserta nomor baris | Closed |
| BUG-02 | Nilai 105 diterima sebagai data valid | TC04, TC13 | `validasi_nilai()` sudah ada tetapi belum dipanggil di `baca_data()` | Panggil `validasi_nilai()` untuk setiap nilai; tolak bila di luar 0-100 | Closed |
| BUG-03 | `ValueError` pada baris kosong, baris komentar `#`, dan baris tanpa koma (juga membuat `nilai_contoh.txt` gagal dibaca) | TC12, TC13, TC14 | `split(",")` langsung di-unpack menjadi dua variabel tanpa memeriksa jumlah bagian | Abaikan baris kosong dan `#`; tolak baris yang jumlah bagiannya bukan dua | Closed |
| BUG-04 | `ZeroDivisionError` saat data kosong | TC09, TC11 | `sum(nilai) / len(nilai)` dengan `len = 0` | Tambah pemeriksaan list kosong di `hitung_statistik()`; `main()` menampilkan pesan bila tidak ada data valid | Closed |
| BUG-05 | `FileNotFoundError` menghentikan program dengan traceback | TC05 | Pembacaan file tidak dibungkus `try-except` | Tangkap `FileNotFoundError` (dan `OSError`) di `main()`, tampilkan pesan, kembalikan kode 1 | Closed |
| BUG-06 | TC05 gagal dengan `ZeroDivisionError` yang bukan berasal dari skenario file tidak ada | TC05 | Kesalahan pada kode tes: `tc05()` memanggil `main()` dengan file kosong sebelum skenario sebenarnya | Hapus pemanggilan yang tidak perlu | Closed |
| BUG-07 | TC09 FAIL padahal pesan sudah tampil | TC09 | Pengecekan pesan di tes peka huruf besar-kecil ("Tidak ada..." vs "tidak ada...") | Bandingkan dengan `keluaran.lower()` | Closed |

## Regression Check

Setelah setiap perbaikan, seluruh 14 test case dijalankan ulang (bukan hanya yang gagal). Tidak ada test yang sebelumnya PASS berubah menjadi FAIL (TC01, TC02, TC03, TC06, TC07, TC10 tetap PASS pada semua eksekusi).
