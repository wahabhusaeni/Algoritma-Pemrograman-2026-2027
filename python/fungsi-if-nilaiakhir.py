def hitung_grade(nilai: float) -> str:
    if nilai > 80: return "A"
    if nilai > 70: return "B"
    if nilai > 60: return "C"
    if nilai > 50: return "D"
    return "E"

tugas = float(input("Input nilai Tugas: "))
uts = float(input("Input nilai UTS: "))
uas = float(input("Input nilai UAS: "))

nilai = 0.15 * tugas + 0.35 * uts + 0.50 * uas
grade = hitung_grade(nilai)
status = "Lulus" if nilai > 60 else "Tidak Lulus"

print(f"Nilai Akhir: {nilai:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")