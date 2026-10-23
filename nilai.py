#Nama : Muhamad Wahab Husaeni
#Nim  : I.2610251

print("=== INPUT NILAI MAHASIWA ===")
nama = input("Nama Mahasiswa: ")
tugas = int(input("Nilai Tugas (0-100): "))
UTS = int(input("Nilai UTS (0-100): "))
UAS = int(input("Nilai UAS (0-100): "))
kehadiran = int(input("Kehadiran % (0-100): "))

nilai_akhir = (
    (tugas * 0.3) +
    (UTS * 0.3) +
    (UAS * 0.4)
  )

if nilai_akhir >= 80:
    grade = "A"
    keterangan = "Sangat Baik"

elif nilai_akhir >= 70:
    grade = "B"
    keterangan = "Lumayan"

elif nilai_akhir >= 60:
    grade = "C"
    keterangan = "Cukup"

elif nilai_akhir >= 50:
    grade = "D"
    keterangan = "Kurang"
else:
    grade = "E"
    keterangan = "Sangat Kurang"

data = {
    "nama" : nama,
    "tugas" : tugas,
    "uts" : UTS,
    "uas" : UAS,
    "kehadiran" : kehadiran
  }

if grade != "E": 
  if kehadiran >= 75:
    status = "Lulus"
  else:
    status = "Tidak Lulus (Kehadiran Kurang)"
else:
  status = "Tidak Lulus (Nilai Kurang)" 

print("\n====DATA NILAI====")
print(f"{'Nama Mahasiswa':<15} : {data['nama']}")
print(f"{'Nilai Tugas':<15} : {data['tugas']}")
print(f"{'Nilai UTS':<15} : {data['uts']}")
print(f"{'Nilai UAS':<15} : {data['uas']}")
print(f"{'Kehadiran %':<15} : {data['kehadiran']}%")

print("\n====Hasil====")
print("Nama :", data["nama"])
print(f"Tugas : {data['tugas']} | UTS : {data['uts']} | UAS : {data['uas']} | Kehadiran : {data['kehadiran']}%")
print("-"*80)

print(f"{'Nilai Akhir':<15}: {nilai_akhir:.2f}")
print(f"{'Nilai Huruf':<15}: {grade} {keterangan}")
print(f"{'Status':<15}: {status}")