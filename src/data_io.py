"""Membaca data nilai dari file dan menulis laporan."""
from analisis import validasi_nilai
from utilitas import NILAI_MAKSIMUM, NILAI_MINIMUM


def baca_data(path):
    """Membaca file berformat 'nama,nilai' per baris.

    Baris kosong dan baris berawalan '#' diabaikan. Baris yang formatnya salah,
    nilainya bukan angka, atau di luar rentang 0-100 dicatat sebagai kesalahan
    (lengkap dengan nomor barisnya) dan tidak menghentikan program.

    Mengembalikan (data, kesalahan): data adalah list of dictionary
    {"nama": str, "nilai": float}, kesalahan adalah list pesan.
    Melempar FileNotFoundError bila file tidak ada (ditangani oleh main).
    """
    data = []
    kesalahan = []
    with open(path, encoding="utf-8-sig") as f:
        for nomor, baris in enumerate(f, start=1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue

            bagian = [b.strip() for b in baris.split(",")]
            if len(bagian) != 2 or not bagian[0]:
                kesalahan.append(f"Baris {nomor}: format harus 'nama,nilai' -> {baris}")
                continue

            nama, teks_nilai = bagian
            try:
                nilai = float(teks_nilai)
            except ValueError:
                kesalahan.append(f"Baris {nomor}: nilai '{teks_nilai}' bukan angka")
                continue

            if not validasi_nilai(nilai):
                kesalahan.append(
                    f"Baris {nomor}: nilai {teks_nilai} di luar rentang "
                    f"{NILAI_MINIMUM}-{NILAI_MAKSIMUM}")
                continue

            data.append({"nama": nama, "nilai": nilai})
    return data, kesalahan


def simpan_laporan(teks, path):
    """Menulis teks laporan ke file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(teks)
