'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : 2019 KAKAO BLIND RECRUITMENT "길찾기 게임"
comment : 이진트리를 구성한 후 전위순회, 후위순회를 구하는 문제이다.
'''

import sys
sys.setrecursionlimit(2000)


class Node(object):
    def __init__(self, x, num):
        self.x = x
        self.num = num
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, x, num):
        self.root = Node(x, num)

    def insert(self, x, num):
        curr_node = self.root
        while True:
            if x < curr_node.x:
                if not curr_node.left:
                    curr_node.left = Node(x, num)
                    break
                else:
                    curr_node = curr_node.left

            if x > curr_node.x:
                if not curr_node.right:
                    curr_node.right = Node(x, num)
                    break
                else:
                    curr_node = curr_node.right

    def preorder(self):
        result = []

        def recursion(node):
            result.append(node.num)
            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)

        recursion(self.root)
        return result

    def postorder(self):
        result = []

        def recursion(node):
            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)
            result.append(node.num)

        recursion(self.root)
        return result


def solution(nodeinfo):
    info = [[node[0], node[1], i + 1] for i, node in enumerate(nodeinfo)]
    info = sorted(info, key=lambda x: x[1])
    root = info.pop()
    BT = BinaryTree(root[0], root[2])
    while info:
        node = info.pop()
        BT.insert(node[0], node[2])

    answer = []
    answer.append(BT.preorder())
    answer.append(BT.postorder())
    return answer

#Example
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
expected_result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

print(solution(nodeinfo))