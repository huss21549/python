import time

# Welcome message
print("💸💸💸 Welcome to the USD Withdrawal Counter 💸💸💸")
print("===============================================")
time.sleep(1)

# Take input from user
try:
    amount = int(input("🧮 Enter the amount you want to withdraw in USD: $"))
    print("\n🔄 Calculating your withdrawal breakdown...\n")
    time.sleep(1.5)

    # Denomination calculations
    note_100 = amount // 100
    note_50 = (amount % 100) // 50
    note_20 = ((amount % 100) % 50) // 20
    note_10 = (((amount % 100) % 50) % 20) // 10
    note_5  = ((((amount % 100) % 50) % 20) % 10) // 5
    note_1  = ((((amount % 100) % 50) % 20) % 10) % 5

    # Receipt display
    print("🧾 Your Stylish Withdrawal Receipt")
    print("===================================")
    if note_100 > 0:
        print(f"💵 $100 bills : {note_100}")
    if note_50 > 0:
        print(f"💵 $50 bills  : {note_50}")
    if note_20 > 0:
        print(f"💵 $20 bills  : {note_20}")
    if note_10 > 0:
        print(f"💵 $10 bills  : {note_10}")
    if note_5 > 0:
        print(f"💵 $5 bills   : {note_5}")
    if note_1 > 0:
        print(f"💵 $1 bills   : {note_1}")

    print("===================================")
    print(f"✅ Total Dispensed: ${amount}")
    print("💬 Thank you for using our ATM simulator!")

except ValueError:
    print("❌ Invalid input! Please enter a valid whole number (integer).")

