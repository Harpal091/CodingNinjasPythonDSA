class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def Input():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
        if (currData == -1):
            break
        newNode = Node(currData)
        if (head is None):
            head = newNode
        else:
            curr = head
            while (curr.next is not None):
                curr = curr.next

            curr.next = newNode

    return head

def printLL(head):
    curr=head
    while(curr is not None):
        print(str(curr.data) +'->', end="")
        curr=curr.next
    print("None")
    return


def deleteNode(head, pos):
    # Write your code here.
    curr = head
    prev = None
    count = 0
    while (count < pos):
        prev = curr
        curr = curr.next
        count = count + 1
    curr = curr.next
    prev.next = curr

    return head

def ReverseLLIterative(head):
    prev=None
    curr=head
    while curr is not None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp

    return prev

def ReverseLLRecursive(head):
    if head is None:
        return None
    if head.next is None:
        return head
    smallhead=ReverseLLIterative(head.next)
    curr=smallhead
    while curr is not None:
        tail=curr
        curr=curr.next
    tail.next=head
    head.next=None

    return smallhead

head=Input()
printLL(head)
head=ReverseLLIterative(head)
printLL(head)
head=ReverseLLRecursive(head)
printLL(head)
head=ReverseLLRecursive(head)
printLL(head)
