class Node:
    def __init__(self, value, freq, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.freq = freq

    def __repr__(self):
        return f"({self.value} ,{self.freq}, left: {self.left}, right: {self.right})"

    def __gt__(self, other):
        """Overrides the > operator"""
        if isinstance(other, Node):
            return self.freq > other.freq
        return NotImplemented

    def __lt__(self, other):
        """Overrides the < operator"""
        if isinstance(other, Node):
            return self.freq < other.freq
        return NotImplemented

    def __ge__(self, other):
        """Overrides the >= operator"""
        if isinstance(other, Node):
            return self.freq >= other.freq
        return NotImplemented

    def __le__(self, other):
        """Overrides the <= operator"""
        if isinstance(other, Node):
            return self.freq <= other.freq
        return NotImplemented


class Tree:
    def __init__(self, nodes: list[Node]):
        self.nodes: list[Node] = nodes

    def __repr__(self):
        return "\n".join(str(node) for node in self.nodes)

    def sort(self):
        self.nodes.sort(key=lambda node: node.freq)


def frequency(text):
    result = dict()
    for l in text:
        if result.get(l, False):
            result[l] += 1
        else:
            result[l] = 1
    return result


text = "AABCBAD"
freq = frequency(text)

nodes = [Node(value=key, freq=value) for (key, value) in freq.items()]
tree = Tree(nodes=nodes)
tree.sort()

print(tree)
