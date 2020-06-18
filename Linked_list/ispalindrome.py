from linked_list_class import ListNode, LinkedList

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # safety check on the head
        if not head or not head.next:
            return True

        # we create our two pointers and the tail of our reversed first half
        pt_a = head
        pt_b = head
        reversedfh = None

        # pt_b will go twice as fast, so it will reach the end when pt_a will be in the middle
        while pt_b and pt_b.next:
            tmp = pt_a

            pt_a = pt_a.next
            pt_b = pt_b.next.next

            tmp.next = reversedfh
            reversedfh = tmp

        # odd length, we jump the middle value as it is not inside our reversed list
        if pt_b is not None:
            pt_a = pt_a.next
        
        while pt_a :
            if pt_a.val != reversedfh.val:
                return False
            pt_a = pt_a.next
            reversedfh = reversedfh.next

        return True

if __name__ == '__main__' :
    inp = [1,2]
    ll = LinkedList(inp)
    sol = Solution()
    if sol.isPalindrome(ll.head):
        print("this linked list is a palindrome")
    else :
        print("this linked list is not a palindrome")