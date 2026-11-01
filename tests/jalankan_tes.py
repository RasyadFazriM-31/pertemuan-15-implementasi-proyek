"""Penjalan test case proyek Rekap dan Analisis Nilai.

Cara pakai (dari folder induk proyek):
    python3 tests/jalankan_tes.py            # tampilkan tabel hasil
    python3 tests/jalankan_tes.py --simpan   # tampilkan dan simpan ke tests/hasil_uji.md

Program keluar dengan kode 1 jika ada test yang FAIL.
"""
import contextlib
import io
import os
import sys
import tempfile

FOLDER_PROYEK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(FOLDER_PROYEK, "src"))

import analisis  # noqa: E402
import data_io  # noqa: E402
import main as program  # noqa: E402

FOLDER_SEMENTARA = tempfile.mkdtemp(prefix="uji_nilai_")


def tulis_sementara(isi, nama="data.txt"):
    path = os.path.join(FOLDER_SEMENTARA, nama)
    with open(path, "w", encoding="utf-8") as f:
        f.write(isi)
    return path


def jalankan_main(isi_file):
    """Jalankan main() pada file sementara; kembalikan (kode, keluaran, path_laporan)."""
    path = tulis_sementara(isi_file)
    laporan = os.path.join(FOLDER_SEMENTARA, "laporan.txt")
    if os.path.exists(laporan):
        os.remove(laporan)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        kode = program.main([path], laporan)
    return kode, buffer.getvalue(), laporan


# ---------------------------------------------------------------- test case
def tc01():
    data, _ = data_io.baca_data(tulis_sementara("A,80\nB,70\nC,90\n"))
    return f"rata-rata {analisis.hitung_statistik(data)['rata_rata']:.1f}"


def _diterima_atau_ditolak(isi):
    data, kesalahan = data_io.baca_data(tulis_sementara(isi))
    status = "diterima" if data else "ditolak"
    return f"{status}: {len(data)} data, {len(kesalahan)} kesalahan"


def tc02():
    return _diterima_atau_ditolak("A,0\n")


def tc03():
    return _diterima_atau_ditolak("A,100\n")


def tc04():
    return _diterima_atau_ditolak("A,105\n")


def tc05():
    tidak_ada = os.path.join(FOLDER_SEMENTARA, "tidak_ada.txt")
    laporan = os.path.join(FOLDER_SEMENTARA, "laporan_tc05.txt")
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        kode = program.main([tidak_ada], laporan)
    pesan = "file tidak ditemukan" if "tidak ditemukan" in buffer.getvalue() else "tanpa pesan"
    return f"kode {kode}, {pesan}"


def tc06():
    data, _ = data_io.baca_data(tulis_sementara("A,80\nB,90\nC,75\n"))
    tuntas, _ = analisis.hitung_ketuntasan(data, 75)
    return f"tuntas {tuntas} dari {len(data)}"


def tc07():
    return (f"75 {analisis.tentukan_status(75, 75)}, "
            f"74 {analisis.tentukan_status(74, 75)}")


def tc08():
    return _diterima_atau_ditolak("A,abc\n")


def tc09():
    kode, keluaran, laporan = jalankan_main("")
    pesan = ("tidak ada data valid" if "tidak ada data valid" in keluaran.lower()
             else "tanpa pesan")
    return f"kode {kode}, {pesan}"


def tc10():
    kode, _, laporan = jalankan_main("A,80\nB,70\n")
    isi = open(laporan, encoding="utf-8").read() if os.path.exists(laporan) else ""
    ada = "laporan berisi rata-rata" if "Rata-rata" in isi else "laporan tidak ada"
    return f"kode {kode}, {ada}"


def tc11():
    s = analisis.hitung_statistik([])
    return f"rata-rata {s['rata_rata']}, min {s['minimum']}, maks {s['maksimum']}"


def tc12():
    contoh = os.path.join(FOLDER_PROYEK, "data", "nilai_contoh.txt")
    laporan = os.path.join(FOLDER_SEMENTARA, "laporan_contoh.txt")
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        kode = program.main([contoh], laporan)
    data, _ = data_io.baca_data(contoh)
    return f"kode {kode}, {len(data)} data"


def tc13():
    data, kesalahan = data_io.baca_data(
        tulis_sementara("A,80\nB,abc\n\nC,105\nD,70\n"))
    rata = analisis.hitung_statistik(data)["rata_rata"]
    return f"{len(data)} valid, {len(kesalahan)} kesalahan, rata-rata {rata:.1f}"


def tc14():
    return _diterima_atau_ditolak("tanpa_koma\n")


KASUS = [
    ("TC01", "Normal", "Nilai 80, 70, 90", "rata-rata 80.0", tc01),
    ("TC02", "Batas", "Nilai 0", "diterima: 1 data, 0 kesalahan", tc02),
    ("TC03", "Batas", "Nilai 100", "diterima: 1 data, 0 kesalahan", tc03),
    ("TC04", "Invalid", "Nilai 105", "ditolak: 0 data, 1 kesalahan", tc04),
    ("TC05", "Invalid", "File tidak ada", "kode 1, file tidak ditemukan", tc05),
    ("TC06", "Normal", "Nilai 80, 90, 75 (KKM 75)", "tuntas 3 dari 3", tc06),
    ("TC07", "Batas", "Nilai 75 dan 74 (KKM 75)", "75 Tuntas, 74 Belum Tuntas", tc07),
    ("TC08", "Invalid", "Nilai teks abc", "ditolak: 0 data, 1 kesalahan", tc08),
    ("TC09", "Kosong", "File kosong", "kode 1, tidak ada data valid", tc09),
    ("TC10", "File", "Data valid, simpan laporan", "kode 0, laporan berisi rata-rata", tc10),
    ("TC11", "Kosong", "List kosong ke hitung_statistik",
     "rata-rata 0, min None, maks None", tc11),
    ("TC12", "Integrasi", "data/nilai_contoh.txt", "kode 0, 12 data", tc12),
    ("TC13", "Campuran", "Valid, abc, baris kosong, 105, valid",
     "2 valid, 2 kesalahan, rata-rata 75.0", tc13),
    ("TC14", "Invalid", "Baris tanpa koma", "ditolak: 0 data, 1 kesalahan", tc14),
]


def jalankan():
    hasil = []
    for id_, kategori, masukan, harapan, fungsi in KASUS:
        try:
            aktual = fungsi()
        except Exception as e:  # noqa: BLE001 - kegagalan dicatat sebagai FAIL
            aktual = f"Program error: {type(e).__name__}"
        status = "PASS" if aktual == harapan else "FAIL"
        hasil.append((id_, kategori, masukan, harapan, aktual, status))
    return hasil


def tabel_markdown(hasil):
    baris = ["| ID | Kategori | Input/Kondisi | Expected | Actual | Status |",
             "|----|----------|---------------|----------|--------|--------|"]
    for h in hasil:
        baris.append("| " + " | ".join(h) + " |")
    return "\n".join(baris)


if __name__ == "__main__":
    hasil = jalankan()
    tabel = tabel_markdown(hasil)
    lulus = sum(1 for h in hasil if h[-1] == "PASS")
    print(tabel)
    print(f"\nRingkasan: {lulus} PASS, {len(hasil) - lulus} FAIL dari {len(hasil)} test case")
    if "--simpan" in sys.argv:
        path = os.path.join(FOLDER_PROYEK, "tests", "hasil_uji.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write("# Hasil Eksekusi Test Case\n\n" + tabel +
                    f"\n\nRingkasan: {lulus} PASS, {len(hasil) - lulus} FAIL "
                    f"dari {len(hasil)} test case.\n")
    sys.exit(0 if lulus == len(hasil) else 1)
