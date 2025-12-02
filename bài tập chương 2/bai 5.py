from xml.dom import minidom

doc = minidom.parse('sample.xml')

root = doc.documentElement
print("Phần tử gốc:", root.tagName)
print("\nDanh sách các phần tử trong file sample.xml:\n")


saff_list = doc.getElementsByTagName("saff")


for saff in saff_list:
    print("Phần tử cha:", saff.tagName, "| ID =", saff.getAttribute("id"))
    elements = saff.getElementsByTagName("*") 
    for elem in elements:
        print("  ├──", elem.tagName)

    print("-" * 30)
