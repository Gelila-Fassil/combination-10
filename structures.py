class AuditNode:
    """Linked List Node for persistent history."""
    def __init__(self, entry):
        self.entry = entry
        self.next = None

class AuditLinkedList:
    """An append-only linked list for the audit log."""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_log(self, text):
        new_node = AuditNode(text)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def get_all_logs(self):
        logs = []
        current = self.head
        while current:
            logs.append(current.entry)
            current = current.next
        return logs