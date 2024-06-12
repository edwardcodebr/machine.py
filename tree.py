class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []

    def count_pairs_with_sum_greater_than_x(self, x):
        elements = self.inorder(self.root)
        count = 0
        n = len(elements)
        for i in range(n):
            for j in range(i + 1, n):
                if elements[i] + elements[j] > x:
                    count += 1
        return count

# Função principal para leitura de dados e execução do programa
def main():
    bst = BST()
    elements = list(map(int, input("Digite os elementos da ABB (separados por espaço): ").split()))
    x = int(input("Digite o valor de X: "))

    for element in elements:
        bst.insert(element)

    result = bst.count_pairs_with_sum_greater_than_x(x)
    print(f"Número de pares com soma maior que {x}: {result}")

if __name__ == "__main__":
    main()
