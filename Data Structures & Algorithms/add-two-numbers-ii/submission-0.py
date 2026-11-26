
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stack1 = []
        stack2 = []

        # Store digits of first linked list
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        # Store digits of second linked list
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Add digits from right to left
        while stack1 or stack2 or carry:

            total = carry

            if stack1:
                total += stack1.pop()

            if stack2:
                total += stack2.pop()

            carry = total // 10
            digit = total % 10

            # Insert new node at beginning
            newNode = ListNode(digit)
            newNode.next = head
            head = newNode

        return head
