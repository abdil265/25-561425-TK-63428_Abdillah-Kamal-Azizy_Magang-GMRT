import math

Kinematics = input("Pilih Forward Kinematics (F) atau Inverse Kinematics (I): ").upper()
if Kinematics == "F" :
    l1 = float(input("Masukkan panjang lengan pertama: "))
    l2 = float(input("Masukkan panjang lengan kedua: "))
    theta1 = float(input("Masukkan sudut lengan pertama (counterclockwise): "))
    theta2 = float(input("Masukkan sudut lengan kedua (counterclockwise): "))

    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)

    x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
    y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)

    print(f"Koordinat akhir kaki robot: x = {x:.2f}, y = {y:.2f}")

elif Kinematics == "I" :
    x = float(input("Masukkan koordinat x tujuan: "))
    y = float(input("Masukkan koordinat y tujuan: "))
    l1 = float(input("Masukkan panjang lengan pertama: "))
    l2 = float(input("Masukkan panjang lengan kedua: "))

    T = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    Theta2 = math.acos(T)
    Theta1 = math.atan2(y, x) - math.atan2(l2 * math.sin(Theta2), l1 + l2 * math.cos(Theta2))

    print(f"Sudut lengan pertama: {math.degrees(Theta1):.2f} derajat")
    print(f"Sudut lengan kedua: {math.degrees(Theta2):.2f} derajat")
else :
    print("Pilihan tidak valid. Silakan pilih 'F' untuk Forward Kinematics atau 'I' untuk Inverse Kinematics.")