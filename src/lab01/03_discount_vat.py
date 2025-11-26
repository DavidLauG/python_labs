# Задание 3 — Чек: скидка и НДС
# Show the Receipt with the final Discount and VAT
price = float(input("Write the price in ₽ (roubles): "))
descount = float(input("Write the descount in ₽ (roubles): "))
vat = float(input("Write the VAT in ₽ (roubles): "))

base = price * (1 - descount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:>20.2f} ₽")
print(f"Итого к оплате: {total:>10.2f} ₽")
