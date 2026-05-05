class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* curr = head;
        int count = 0;

        // Check if there are at least k nodes
        while (curr && count < k) {
            curr = curr->next;
            count++;
        }

        if (count < k) return head;

        // Reverse first k nodes
        ListNode* prev = nullptr;
        curr = head;
        ListNode* next = nullptr;
        count = 0;

        while (curr && count < k) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
            count++;
        }

        // Recursively process remaining list
        if (next) {
            head->next = reverseKGroup(next, k);
        }

        return prev;
    }
};