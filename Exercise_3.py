class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if self.head == None:
            newNode = ListNode(self,data)
            self.head = newNode
        else:
            self.last = self.head
            while(self.last != None):
                self.last = self.head.next
            self.next = ListNode(self,data)
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        self.last = self.head
        while(self.last != None):
            if self.data == key :
                return self
            self.last = self.last.next
        return None
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        current = self.head
        previous = None

        while current!=None:
            if current.data == key:
                if previous==None:
                    previous.next = current.next
                else:
                    self.head = current.next
                return current
            previous = current
            current = current.next
        return None

