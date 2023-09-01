from datetime import *

def gun_to_tarih(yil, gun):
    # Verilen yılın 1 Ocak tarihini oluşturun
    tarih = datetime(yil, 1, 1)
    
    # Verilen gün sayısı kadar gün ekleyin (gun - 1 çünkü günler 0'dan başlar)
    tarih += timedelta(days=gun - 1)

    return tarih

start = int(input("What's your starting minute: "))

start_day = date.today()

day_of_year = start_day.strftime("%j")

k = 0

for i in range(int(day_of_year),366):
    k += 1
    with open('E:/www/python/basic-projects/Habit Generator/habit.txt', 'a') as file:
        file.write(f"{gun_to_tarih(datetime.now().year, i).strftime('%d/%m/%Y')} - Starting day is {k} - Working minute {round(start,2)}\n")

    start = start + ((start / 100) * 1)