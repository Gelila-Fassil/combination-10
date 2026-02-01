from structures import AuditLinkedList
from transactions import apply_deposit, apply_withdraw, apply_transfer

class BankEngine:
    def __init__(self):
        self.accounts = {}       # Hash Map
        self.queue = []          # FIFO Queue
        self.stack = []          # LIFO Stack for rollbacks
        self.audit = AuditLinkedList()

    def process_transaction(self):
        if not self.queue:
            return "No transactions to process."
        
        txn = self.queue.pop(0)
        t_type = txn['type']
        
        # Dispatch to specific logic
        if t_type == "DEPOSIT":
            res = apply_deposit(self.accounts, txn)
        elif t_type == "WITHDRAW":
            res = apply_withdraw(self.accounts, txn)
        elif t_type == "TRANSFER":
            res = apply_transfer(self.accounts, txn)
        
        self.audit.add_log(res)
        if "Success" in res:
            self.stack.append(txn)
        return res

    def perform_rollback(self, n):
        rolled_count = 0
        for _ in range(int(n)):
            if not self.stack: break
            
            txn = self.stack.pop()
            # Perform inverse operations
            if txn['type'] == "DEPOSIT":
                self.accounts[txn['acc']] -= txn['amount']
            elif txn['type'] == "WITHDRAW":
                self.accounts[txn['acc']] += txn['amount']
            elif txn['type'] == "TRANSFER":
                self.accounts[txn['from']] += txn['amount']
                self.accounts[txn['to']] -= txn['amount']
            
            self.audit.add_log(f"ROLLED_BACK: {txn['type']} {txn['amount']}")
            rolled_count += 1
        return f"Rolled back {rolled_count} transactions."