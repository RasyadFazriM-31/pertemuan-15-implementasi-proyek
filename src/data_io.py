"""Membaca data nilai dari file dan menulis laporan."""


def baca_data(path):
    """Membaca file berformat 'nama,nilai' per baris.

    Mengembalikan (data, kesalahan): data adalah list of dictionary
    {"nama": str, "nilai": float}, kesalahan adalah list pesan.
    """
    data = []
    kesalahan = []
    with open(path, encoding="utf-8") as f:
        for baris in f:
            nama, nilai = baris.strip().split(",")
            data.append({"nama": nama, "nilai": float(nilai)})
    return data, kesalahan


def simpan_laporan(teks, path):
    """Menulis teks laporan ke file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(teks)
