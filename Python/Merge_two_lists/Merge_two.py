# Definition for singly-linked list.
#class ListNode(object):
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        merged = dummy

        while list1 and list2:
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        if list1:
            merged.next = list1
        elif list2:
            merged.next = list2
        return dummy.next


        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        while i < len(list1):
            merged.append(list1[i])
            i += 1

        while j < len(list2):
            merged.append(list2[j])
            j+=1
            
        return merged
