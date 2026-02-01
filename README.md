
********************************************
Bank Transaction Ledger with Rollback
********************************************

A modular Python-based banking engine that handles transactions using professional data structures. This system simulates a real-world bank core where transactions are queued, processed, and can be "undone" using a rollback feature.

*********************************************
How It Works
*********************************************

This project is built using Modular Programming, meaning each part of the bank has its own specific job. It uses four primary data structures to ensure speed and accuracy.

1, Queue (FIFO): Acts as a "Waiting Line" for incoming transactions.

2, Stack (LIFO): Acts as an "Undo Button" for reversing the most recent successful transactions.

3, Hash Map (Dictionary): A "Filing Cabinet" that stores account balances for instant lookup.

5, Linked List: A "Permanent Ledger" (Audit Log) that records every single event in chronological order.

******************************************
Project Structure
******************************************

The project is split into four modules to keep the code clean and easy to manage:

1, structures.py: Contains the Linked List logic for the Audit Log.

2, transactions.py: Contains the Business Logic (how to Deposit, Withdraw, and Transfer).

3, engine.py: The "Brain" of the system that manages the Queue and Stack.

4, main.py: The User Interface (CLI) where you type commands.

******************************************
Installation & Running
******************************************

1, Clone or Download all four .py files into the same folder.

2, Open your terminal or command prompt.
3, Navigate to the folder and run:Bashpython main.py


********************************************
Available Commands
********************************************

Once  the program starts, you can use the following commands:

CREATE_ACCOUNT [ID] [Initial Balance] Used to open a new account in the system. You must provide a unique name (like A1) and how much money they start with.

Example: CREATE_ACCOUNT A1 1000

TXN [Type] [Account] [Optional: To_Account] [Amount] This puts a transaction into the "Waiting Line" (Queue). It doesn't move the money yet! Types can be DEPOSIT, WITHDRAW, or TRANSFER.

Example (Deposit): TXN DEPOSIT A1 500

Example (Transfer): TXN TRANSFER A1 A2 200

PROCESS Tells the bank to take the next person from the Waiting Line and actually move the money. It will tell you if the move was a "Success" or "Failed" (like if the person was too poor for the transfer).

ROLLBACK [Number] The "Undo" button. It looks at the most recent successful moves and reverses the math to put the money back exactly where it was.

Example: ROLLBACK 1 (Undo the very last success).

BALANCE [Account ID] Instantly checks the Filing Cabinet (Hash Map) and tells you exactly how many coins that person has right now.

AUDIT Prints out the entire history of the bank from the very first day until now. It shows every success, every failure, and every rollback.

EXIT Safely shuts down the Banking Engine.


********************************************
 What I Learned
 *******************************************

 State Management: How to move a system from one state to another safely.
 
 Reversibility: Using a Stack to perform inverse mathematical operations (Rollbacks).
 
 Efficiency: Using Hash Maps to find accounts in 
 O(1) time rather than searching through a list.
 
 Traceability: Using a Linked List to create an append-only audit trail that cannot be deleted.