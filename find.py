import os
from scapy.all import *

def get_distance(rssi):
    # Fórmula de cálculo aproximado da distância
    # Pode variar dependendo do ambiente e do dispositivo
    tx_power = -59  # Potência de transmissão do sinal em dBm
    n = 2.7  # Expoente que varia de 2 a 4 dependendo do ambiente
    return 10 ** ((tx_power - rssi) / (10 * n))

def scan_devices():
    devices = []
    print("Escaneando dispositivos na rede...")
    arp_result = os.popen("arp -a").read()

    for line in arp_result.splitlines():
        if "incomplete" not in line:
            ip, _, mac, _ = line.split()
            devices.append((ip, mac))

    return devices

def main():
    devices = scan_devices()

    for index, (ip, mac) in enumerate(devices, 1):
        print(f"Dispositivo {index}:")
        print(f"IP: {ip}")
        print(f"MAC: {mac}")
        rssi = random.randint(-90, -40)  # Simulação de um valor RSSI
        distance = get_distance(rssi)
        print(f"Distância aproximada: {distance} metros")
        print()

if __name__ == "__main__":
    main()
