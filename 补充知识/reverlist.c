
# include <stdio.h>

typedef struct Node {
    int data;
    struct Node* next;
} ListNode;

ListNode* reverseList(ListNode* head) {

    if(head == NULL|| head->next == NULL) {
        return head; // If the list is empty or has only one node, return it as is
    }
    ListNode* prev = NULL;
    ListNode* current = head;
    ListNode* temp = NULL;

    while (current != NULL) {
        temp = current->next; // Store the next node
        current->next = prev; // Reverse the current node's pointer
        prev = current; // Move prev to the current node
        current = temp; // Move to the next node
    }
    return prev; // At the end, prev will be the new head of the reversed list
}

ListNOde *kGroupReverse(ListNode* head, int k) {
    if(head == NULL || head->next == NULL || k <= 1) {
        return head; // If the list is empty, has only one node, or k is less than or equal to 1, return it as is
    }

    int count = 0;
    ListNode* current = head;

    while(current!=NULL && count < k) {
        current = current->next;
        count++;
    }

    if(count == k){

        current = kGroupReverse(current, k); 

        while(count>0){
            ListNode* temp = head->next; // Store the next node
            head->next = current; // Reverse the current node's pointer
            current = head; // Move current to the current node
            head = temp; // Move to the next node
            count--;
        }

        return current; // Return the new head of the reversed group
    }
}