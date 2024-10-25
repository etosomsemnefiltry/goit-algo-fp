import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Уникальный идентификатор для каждого узла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color_sequence(n):
    """ Генерация цветов от темного к светлому. """
    colors = []
    for i in range(n):
        hue = i / n
        lightness = 0.3 + (i / n) * 0.7  # Регулировка яркости
        color = colorsys.hls_to_rgb(hue, lightness, 1.0)
        colors.append('#%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)))
    return colors


def bfs(tree_root):
    """ Обход в ширину и раскраска узлов. """
    queue = [tree_root]
    color_sequence = generate_color_sequence(7)  # Генерируем цвета

    index = 0
    while queue:
        node = queue.pop(0)
        if node:
            node.color = color_sequence[index]  # Присваиваем узлу новый цвет
            queue.append(node.left)
            queue.append(node.right)
            index += 1


def dfs(tree_root):
    """ Обход в глубину и раскраска узлов. """
    stack = [tree_root]
    color_sequence = generate_color_sequence(7)  # Генерируем цвета

    index = 0
    while stack:
        node = stack.pop()
        if node:
            node.color = color_sequence[index]  # Присваиваем узлу новый цвет
            stack.append(node.right)
            stack.append(node.left)
            index += 1


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Выбор типа обхода
traversal_type = input("Введите 'bfs' для обхода в ширину или 'dfs' для обхода в глубину: ")

if traversal_type == 'bfs':
    bfs(root)
elif traversal_type == 'dfs':
    dfs(root)
else:
    print("Неверный выбор!")

draw_tree(root)
