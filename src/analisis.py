"""Logika perhitungan statistik dan ketuntasan."""
from utilitas import KKM_DEFAULT, NILAI_MAKSIMUM, NILAI_MINIMUM


def validasi_nilai(nilai):
    """True bila nilai berada pada rentang 0 sampai 100 (inklusif)."""
    return NILAI_MINIMUM <= nilai <= NILAI_MAKSIMUM


def hitung_statistik(data):
    """Ringkasan statistik dari list of dictionary data siswa."""
    nilai = [d["nilai"] for d in data]
    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
    }


def tentukan_status(nilai, kkm=KKM_DEFAULT):
    """'Tuntas' bila nilai >= KKM, selain itu 'Belum Tuntas'."""
    return "Tuntas" if nilai >= kkm else "Belum Tuntas"


def hitung_ketuntasan(data, kkm=KKM_DEFAULT):
    """Mengembalikan (jumlah tuntas, jumlah belum tuntas)."""
    tuntas = sum(1 for d in data if d["nilai"] >= kkm)
    return tuntas, len(data) - tuntas


def buat_laporan(data, statistik, kesalahan, kkm=KKM_DEFAULT):
    """Menyusun teks laporan rekap nilai."""
    tuntas, belum = hitung_ketuntasan(data, kkm)
    baris = [
        "LAPORAN REKAP NILAI",
        "=" * 40,
        f"Jumlah data valid : {statistik['jumlah']}",
        f"Rata-rata         : {statistik['rata_rata']:.2f}",
        f"Nilai minimum     : {statistik['minimum']:g}",
        f"Nilai maksimum    : {statistik['maksimum']:g}",
        f"KKM               : {kkm}",
        f"Tuntas            : {tuntas}",
        f"Belum tuntas      : {belum}",
        "",
        "DAFTAR SISWA",
        "-" * 40,
    ]
    for d in data:
        baris.append(f"{d['nama']:<15} {d['nilai']:>6g}  {tentukan_status(d['nilai'], kkm)}")
    baris.append("")
    baris.append(f"BARIS BERMASALAH ({len(kesalahan)})")
    baris.append("-" * 40)
    baris.extend(kesalahan if kesalahan else ["(tidak ada)"])
    return "\n".join(baris) + "\n"
