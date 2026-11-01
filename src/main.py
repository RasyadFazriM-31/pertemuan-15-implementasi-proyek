"""Program Rekap dan Analisis Nilai Matematika Kelas.

Penggunaan:
    python3 src/main.py [path_file_nilai]

Kode keluar: 0 bila berhasil, 1 bila file bermasalah atau tidak ada data valid.
"""
import sys

from analisis import buat_laporan, hitung_ketuntasan, hitung_statistik
from data_io import baca_data, simpan_laporan
from utilitas import KKM_DEFAULT, PATH_DATA_DEFAULT, PATH_LAPORAN_DEFAULT


def main(argv=None, path_laporan=PATH_LAPORAN_DEFAULT):
    argv = sys.argv[1:] if argv is None else argv
    path = argv[0] if argv else PATH_DATA_DEFAULT

    try:
        data, kesalahan = baca_data(path)
    except FileNotFoundError:
        print(f"Kesalahan: file tidak ditemukan: {path}")
        return 1
    except (OSError, UnicodeDecodeError) as e:
        print(f"Kesalahan: file tidak dapat dibaca ({type(e).__name__}): {path}")
        return 1

    for pesan in kesalahan:
        print(f"Peringatan - {pesan}")

    if not data:
        print("Tidak ada data valid yang dapat dihitung.")
        return 1

    statistik = hitung_statistik(data)
    tuntas, belum = hitung_ketuntasan(data, KKM_DEFAULT)

    print(f"Jumlah data : {statistik['jumlah']}")
    print(f"Rata-rata   : {statistik['rata_rata']:.2f}")
    print(f"Minimum     : {statistik['minimum']:g}")
    print(f"Maksimum    : {statistik['maksimum']:g}")
    print(f"Tuntas      : {tuntas} | Belum tuntas: {belum} (KKM {KKM_DEFAULT})")

    try:
        simpan_laporan(buat_laporan(data, statistik, kesalahan), path_laporan)
    except OSError as e:
        print(f"Kesalahan: laporan tidak dapat disimpan ({type(e).__name__}): {path_laporan}")
        return 1
    print(f"Laporan disimpan di {path_laporan}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
