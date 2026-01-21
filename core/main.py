from phone_detector import is_suspicious_phone

def main():
    print("🔍 Detektor prevar – zagon")

    phone = input("Vnesi telefonsko številko: ")
    if is_suspicious_phone(phone):
        print("⚠️ POZOR: Možna telefonska prevara!")
    else:
        print("✅ Telefonska številka ni zaznana kot prevara.")

if __name__ == "__main__":
    main()
