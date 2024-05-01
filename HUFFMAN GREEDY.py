import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(chars, freq):
    nodes = [Node(f, c) for c, f in zip(chars, freq)]
    heapq.heapify(nodes)
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'
        heapq.heappush(nodes, Node(left.freq + right.freq, left.symbol + right.symbol, left, right))
    return nodes[0]

def print_nodes(node, val=''):
    newVal = val + node.huff
    if node.left:
        print_nodes(node.left, newVal)
    if node.right:
        print_nodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

def get_input():
    chars = []
    freq = []
    num = int(input("Enter the number of characters: "))
    for _ in range(num):
        char = input("Enter character: ")
        freq_val = int(input(f"Enter frequency for {char}: "))
        chars.append(char)
        freq.append(freq_val)
    return chars, freq

chars, freq = get_input()
root = huffman_encoding(chars, freq)
print_nodes(root)
