from pprint import pprint

#Diccionario que representa un dispositivo.
device = {
    "name": "RB_BORDE",
    "vendor": "Mikrotik",
    "model": "CCR1072-1G-8S+",
    "os": "RouterOS",
    "version": "v6.49.6",
    "ip": "10.19.5.1"
}

print("\n ________Pretty Print________")
pprint(device)

print("\n ________For Using F-String________")
for key, value in device.items():
    print(f"{key:>15s} : {value}")