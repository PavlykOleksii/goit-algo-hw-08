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

def find_min_value(root: Node | None) -> int | None:
    if root is None:
        return None
    current = root

    while current.left:
        current = current.left

    return current.val

if __name__ == "__main__":
    root = None

    for value in [5, 3, 2, 4, 7, 6, 8]:
        root = insert(root, value)
    
    minimum = find_min_value(root)
    print(f"Найменше значення в дереві: {minimum}")