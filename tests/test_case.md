# Test Case Proyek Rekap dan Analisis Nilai

Test case dirancang sebelum implementasi penuh (lihat `proposal.md` bagian 10) dan dijalankan dengan:

```
python3 tests/jalankan_tes.py            # tampilkan hasil
python3 tests/jalankan_tes.py --simpan   # simpan ke tests/hasil_uji.md
```

Kategori yang dicakup: normal (TC01, TC06), batas (TC02, TC03, TC07), invalid (TC04, TC05, TC08, TC14), kosong (TC09, TC11), file (TC10), integrasi (TC12), dan campuran (TC13). Total 14 test case (syarat minimal: 5).

## Hasil Eksekusi Terakhir

Lihat tabel lengkap beserta kolom Actual dan Status di [hasil_uji.md](hasil_uji.md). Ringkasan: 14 PASS, 0 FAIL.

## Catatan

- Kolom Expected ditetapkan dari spesifikasi proposal, bukan disesuaikan dengan keluaran program.
- Riwayat kegagalan dan perbaikannya ada di [../docs/bug_log.md](../docs/bug_log.md).
- Pengujian memakai file sementara, sehingga tidak menimpa `output/laporan.txt`.
