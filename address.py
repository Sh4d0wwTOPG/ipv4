class AddressIPv4:
    def __init__(self, address: str):
        self.set(address)

    def isValid(self) -> bool:
        """Ověřuje platnost IP adresy."""
        octets = self.address.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                return False
        return True

    def set(self, address: str):
        """Nastaví IP adresu a vrátí instanci objektu."""
        self.address = address
        return self

    def getAsString(self) -> str:
        """Vrací IP adresu jako řetězec."""
        return self.address

    def getAsInt(self) -> int:
        """Vrací IP adresu jako celé číslo."""
        octets = self.address.split('.')
        return sum(int(octet) << (8 * (3 - idx)) for idx, octet in enumerate(octets))

    def getAsBinaryString(self) -> str:
        """Vrací IP adresu ve formě binárního řetězce."""
        return '.'.join(f'{int(octet):08b}' for octet in self.address.split('.'))

    def getOctet(self, number: int) -> int:
        """Vrací hodnotu příslušného oktetu (1 až 4)."""
        octets = self.address.split('.')
        if 1 <= number <= 4:
            return int(octets[number - 1])
        raise ValueError("Oktet musí být v rozsahu 1 až 4.")

    def getClass(self) -> str:
        """Určuje třídu IP adresy (A, B, C, D nebo E)."""
        first_octet = int(self.address.split('.')[0])
        if first_octet < 128:
            return "A"
        elif first_octet < 192:
            return "B"
        elif first_octet < 224:
            return "C"
        elif first_octet < 240:
            return "D"
        return "E"

    def isPrivate(self) -> bool:
        """Kontroluje, zda IP adresa spadá do rozsahu privátních adres."""
        first_octet, second_octet, *_ = map(int, self.address.split('.'))
        return (first_octet == 10) or (first_octet == 172 and 16 <= second_octet <= 31) or (first_octet == 192 and second_octet == 168)

ips = ["192.168.1.1", "8.8.8.8"]

for ip in ips:
    addr = AddressIPv4(ip)
    print(f"IP Address: {addr.getAsString()}")
    print(f"Valid: {addr.isValid()}")
    print(f"As Int: {addr.getAsInt()}")
    print(f"As Binary String: {addr.getAsBinaryString()}")
    print(f"First Octet: {addr.getOctet(1)}")
    print(f"Class: {addr.getClass()}")
    print(f"Is Private: {addr.isPrivate()}\n")
