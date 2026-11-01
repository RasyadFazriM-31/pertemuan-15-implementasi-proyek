"""Konstanta dan fungsi bantu proyek Rekap dan Analisis Nilai."""
import os

KKM_DEFAULT = 75
NILAI_MINIMUM = 0
NILAI_MAKSIMUM = 100

FOLDER_PROYEK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DATA_DEFAULT = os.path.join(FOLDER_PROYEK, "data", "nilai_contoh.txt")
PATH_LAPORAN_DEFAULT = os.path.join(FOLDER_PROYEK, "output", "laporan.txt")
