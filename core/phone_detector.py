# Preprost detektor sumljivih telefonskih številk

SUSPICIOUS_PREFIXES = [
    "+371", "+234", "+92", "+63", "+255"
]

def is_suspicious_phone(number: str) -> bool:
    number = number.replace(" ", "").replace("-", "")
    for prefix in SUSPICIOUS_PREFIXES:
        if number.startswith(prefix):
            return True
    return False


if __name__ == "__main__":
    test_number = input("Vnesi telefonsko številko: ")
    if is_suspicious_phone(test_number):
        print("⚠️ POZOR: Številka je lahko prevara!")
    else:
        print("✅ Številka ni zaznana kot prevara.")
