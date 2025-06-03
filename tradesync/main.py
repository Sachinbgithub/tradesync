import os

print("Welcome to TradeSync CLI")
print("1. Ingest Trades")
print("2. Reconcile Trades")
choice = input("Select an option: ")

if choice == '1':
    os.system("python3 ingest_trades.py")
elif choice == '2':
    os.system("python3 reconciliation.py")
else:
    print("Invalid choice.")
