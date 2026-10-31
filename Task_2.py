from __future__ import annotations

class Node:
    left: Node | None # без лапок тому що from __future__ import annotations
    right: "Node | None"
    val: int

    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key

def insert(root: Node | None, key: int) -> Node:
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def sum_tree(root: Node | None) -> int:
    if root is None:
        return 0

    return root.val + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    root = None

    for value in [5, 3, 2, 4, 7, 6, 8]:
        root = insert(root, value)

    total_sum = sum_tree(root)
    print(f"Сума значень у дереві: {total_sum}")