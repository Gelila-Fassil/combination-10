def apply_deposit(accounts, txn):
    accounts[txn['acc']] += txn['amount']
    return f"Success: DEPOSIT {txn['acc']} {txn['amount']}"

def apply_withdraw(accounts, txn):
    if accounts[txn['acc']] >= txn['amount']:
        accounts[txn['acc']] -= txn['amount']
        return f"Success: WITHDRAW {txn['acc']} {txn['amount']}"
    return f"Failed: WITHDRAW {txn['acc']} {txn['amount']} (Insufficient Funds)"

def apply_transfer(accounts, txn):
    if accounts[txn['from']] >= txn['amount']:
        accounts[txn['from']] -= txn['amount']
        accounts[txn['to']] += txn['amount']
        return f"Success: TRANSFER {txn['from']}->{txn['to']} {txn['amount']}"
    return f"Failed: TRANSFER {txn['from']}->{txn['to']} {txn['amount']} (Insufficient Funds)"