import socket
import requests

def get_ip_address():
    try:
        # İnternet üzerinden bağlantı oluştur
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Google DNS sunucusuna geçici bir bağlantı oluştur

        # Bağlantı yapıldığında yerel IP adresini al
        ip_address = sock.getsockname()[0]

        return ip_address
    except socket.error:
        return "IP adresi alınamadı"


def get_location_by_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    return data

ip = get_ip_address()

print(f"Your Location is: {get_location_by_ip(ip)}")
