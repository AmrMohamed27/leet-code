var mergeTwoLists = function (list1, list2) {
  let last1 = list1;
  while (last1.next !== null) {
    last1 = last1.next;
  }
  last1.next = list2;

  let iterator = list1;
  while (iterator !== null) {
    console.log(iterator.val);
    iterator = iterator.next;
  }
};

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val; // Value of the node
    this.next = next === undefined ? null : next; // Reference to the next node
  }
}
const a1 = new ListNode(1);
const a2 = new ListNode(2);
const a3 = new ListNode(4);
const b1 = new ListNode(1);
const b2 = new ListNode(3);
const b3 = new ListNode(4);
a1.next = a2;
a2.next = a3;
b1.next = b2;
b2.next = b3;

console.log(mergeTwoLists(a1, b1));
