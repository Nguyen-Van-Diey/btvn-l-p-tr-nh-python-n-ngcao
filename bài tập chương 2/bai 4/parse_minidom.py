from xml.dom import minidom
doc = minidom.parse('sample.xml')
root = doc.documentElement
print("Phần tử gốc:", root.tagName)

students = doc.getElementsByTagName("Student")

print("\nDANH SÁCH SINH VIÊN:\n")

for s in students:
    ma_sv = s.getAttribute("id")
    name = s.getElementsByTagName("Name")[0].firstChild.data
    year = s.getElementsByTagName("BirthYear")[0].firstChild.data
    class_name = s.getElementsByTagName("Class")[0].firstChild.data
    gender = s.getElementsByTagName("Gender")[0].firstChild.data

    print(f"Mã SV: {ma_sv}")
    print(f"  Họ tên: {name}")
    print(f"  Năm sinh: {year}")
    print(f"  Lớp: {class_name}")
    print(f"  Giới tính: {gender}")
    print("-" * 30)
