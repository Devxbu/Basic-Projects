from random import choice
import matplotlib.pyplot as plt

oprions = ['Heads', 'Tails']
times = 1000
data = []
for i in range(0,times):
    data.append(choice(oprions))

# Tails ve Heads sayılarını hesapla
tails_count = data.count('Tails')
heads_count = data.count('Heads')

# Etiketler ve veriler
labels = ['Tails', 'Heads']
values = [tails_count, heads_count]

# Pasta grafiği oluştur
plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Tails vs Heads Dağılımı')
plt.axis('equal')  # Daireyi çember şeklinde yapar

# Grafiği göster
plt.show()
