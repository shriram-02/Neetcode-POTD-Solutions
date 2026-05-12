class Solution {
public:
    int gcd(int a, int b) {
        while (b) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr = head;

        while (curr && curr->next) {
            int g = gcd(curr->val, curr->next->val);

            ListNode* node = new ListNode(g);
            node->next = curr->next;
            curr->next = node;

            curr = node->next;
        }

        return head;
    }
};