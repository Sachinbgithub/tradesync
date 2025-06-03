import os

while True:
    print("Welcome to TradeSync CLI")
    print("1. Ingest Trades")
    print("2. Reconcile Trades")
    print("3. View Audit Logs")
    print("0. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        os.system("python ingest_trades.py")
    elif choice == '2':
        os.system("python reconciliation.py")
    elif choice == '3':
        os.system("python view_logs.py")
    elif choice == '0':
        print("Exiting TradeSync CLI. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
