from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import Counter

traffic_data = {
    'total_packets': 0,
    'protocol_counts': Counter(),
    'source_ips': Counter(),
    'destination_ips': Counter()
}

def packet_callback(packet):
    try:
        
        if IP in packet:
            ip_layer = packet[IP]
            
            traffic_data['total_packets'] += 1
            
            if ip_layer.proto == 6:
                traffic_data['protocol_counts']['TCP'] += 1
            elif ip_layer.proto == 17:
                traffic_data['protocol_counts']['UDP'] += 1
            elif ip_layer.proto == 1:
                traffic_data['protocol_counts']['ICMP'] += 1
            else:
                traffic_data['protocol_counts']['Otros'] += 1
            
            traffic_data['source_ips'][ip_layer.src] += 1
            traffic_data['destination_ips'][ip_layer.dst] += 1

            print(f"Paquete IPv4 de origen: {ip_layer.src} -> Destino: {ip_layer.dst} | Protocolo: {ip_layer.proto} -- (Ctrl + C) para mostrar estadísticas")

    except Exception as e:
        print(f"Error procesando paquete: {e}")

def display_statistics():
    print("\n--- Estadísticas de Tráfico ---")
    print(f"Total de paquetes capturados: {traffic_data['total_packets']}")
    
    print("\nPaquetes por protocolo:")
    for protocol, count in traffic_data['protocol_counts'].items():
        print(f"{protocol}: {count}")

    print("\nTop 5 IPs de origen:")
    for ip, count in traffic_data['source_ips'].most_common(5):
        print(f"{ip}: ({count} paquetes)")

    print("\nTop 5 IPs de destino:")
    for ip, count in traffic_data['destination_ips'].most_common(5):
        print(f"{ip}: ({count} paquetes)")

try:
    print("Capturando paquetes... presiona Ctrl+C para detener.")
    sniff(prn=packet_callback, filter="ip", count=0)
except KeyboardInterrupt:
    print("\nDeteniendo captura...")
finally:
    display_statistics()
