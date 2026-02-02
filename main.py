from engine import BankEngine 
def start_app():
    bank = BankEngine()
    
    while True:
        user_input = input("> ").split()
        if not user_input: continue
        cmd = user_input[0].upper()

        if cmd == "CREATE_ACCOUNT":
            bank.accounts[user_input[1]] = float(user_input[2])
            print(f"Account {user_input[1]} created.")

        elif cmd == "TXN":
            # Modularly handles parameters based on length
            if user_input[1] == "TRANSFER":
                bank.queue.append({"type": "TRANSFER", "from": user_input[2], "to": user_input[3], "amount": float(user_input[4])})
            else:
                bank.queue.append({"type": user_input[1], "acc": user_input[2], "amount": float(user_input[3])})
            print("Transaction Queued.")

        elif cmd == "PROCESS":
            print(bank.process_transaction())

        elif cmd == "ROLLBACK":
            print(bank.perform_rollback(user_input[1]))

        elif cmd == "BALANCE":
            print(f"Balance: {bank.accounts.get(user_input[1], 'Not Found')}")

        elif cmd == "AUDIT":
            for log in bank.audit.get_all_logs():
                print(log)

if __name__ == "__main__":
    start_app()