principal = float(input("Initial Capital: "))
rate = float(input("Interest rate (e.g., 0.10 for 10%): "))
months = int(input("Number of months: "))

current_balance = principal

print("\n--- INVESTMENT GROWTH ---")

for month in range(1, months + 1):
    monthly_interest = current_balance * rate
    current_balance = current_balance + monthly_interest

    print(f"Month {month}: ${round(current_balance, 2)}")

print(f"\nFinal Total: ${round(current_balance, 2)}")
