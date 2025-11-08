class Node:
    def __init__(self, rep, freq, left=None, right=None):
        self.left = left
        self.right = right
        self.rep = rep
        self.freq = freq

    def __repr__(self):
        return f"({self.rep} ,{self.freq}, left: {self.left}, right: {self.right})"

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.freq > other.freq
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.freq < other.freq
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Node):
            return self.freq >= other.freq
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Node):
            return self.freq <= other.freq
        return NotImplemented


class Tree:
    def __init__(self, nodes: list[Node]):
        self.nodes: list[Node] = nodes

    def __repr__(self) -> str:
        return "\n".join(str(node) for node in self.nodes)

    def sort(self) -> None:
        self.nodes.sort(key=lambda node: node.freq)

    def is_minimal(self) -> bool:
        return len(self.nodes) == 1

    def combine_last_two(self) -> None:
        n1 = self.nodes[0]
        n2 = self.nodes[1]
        self.nodes.remove(n1)
        self.nodes.remove(n2)
        self.nodes.append(
            Node(rep=f"{n1.rep}-{n2.rep}", freq=n1.freq + n2.freq, left=n1, right=n2)
        )


def frequency(text):
    result = dict()
    for l in text:
        if result.get(l, False):
            result[l] += 1
        else:
            result[l] = 1
    return result


def dfs_preorder(root: Node, current_str="", code={}):
    if root.left:
        current_str += "0"
        dfs_preorder(root.left, current_str, code)
    if root.right:
        if len(current_str) > 0:
            current_str = current_str[0 : len(current_str) - 1]
        current_str += "1"
        dfs_preorder(root.right, current_str, code)
    if not root.right and not root.left:
        code[root.rep] = current_str
    return code


text = "AABCADDEEEF"

freq = frequency(text)
nodes = [Node(rep=key, freq=value) for (key, value) in freq.items()]
tree = Tree(nodes=nodes)
tree.sort()

while not tree.is_minimal():
    tree.combine_last_two()
    tree.sort()


code = dfs_preorder(tree.nodes[0])
print(code)
