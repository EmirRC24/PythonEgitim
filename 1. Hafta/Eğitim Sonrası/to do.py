to_do_list = []

def add_task(to_do_list):
    task = input("Yapılacak Görevi Giriniz: ")
    to_do_list.append(task)
    print("Görev Başarıyla Eklendi")

def show_tasks(to_do_list):
    print("Yapılacak Görevler: ")
    for task in to_do_list:
        print("-" + task)

def delete_task(to_do_list):
    task = input("Silmek İstediğiniz Görevi Girin: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Görev Silindi.")
    else:
        print("Görev Bulunamadı.")

while True:
    print("\nTo-Do List Uygulaması")
    print("1. Görevi Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çıkış")
    choice = input("Seçiminiz (1/2/3/4): ")

    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Uygulamadan Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")