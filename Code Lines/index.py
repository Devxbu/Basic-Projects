import os

path = "E:\www\python\Projects\Chatting"

code_line = 0

def kod_satir_sayici(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        kod_satir_sayisi = 0

        for satir in dosya:
            satir = satir.strip()  # Boşlukları temizle

            if satir:
                kod_satir_sayisi += 1

        return kod_satir_sayisi

def dosya_listele(klasor_yolu):
    for klasor, alt_klasorler, dosyalar in os.walk(klasor_yolu):
        for dosya in dosyalar:
            dosya_yolu = os.path.join(klasor, dosya)
            yield dosya_yolu

for obj in os.listdir(path):
    obj_path = os.path.join(path, obj)
    if os.path.isdir(obj_path) and not obj_path.startswith(('.vs', '.pytest')):
        for dosya_yolu in dosya_listele(obj_path):
            code_line += kod_satir_sayici(dosya_yolu)
    elif os.path.isfile(obj_path):
        print(f'{obj} Dosyasininin satir sayisi: {kod_satir_sayici(obj_path)}')
        code_line += kod_satir_sayici(obj_path)

print("Toplam kod satırı sayısı:", code_line)
