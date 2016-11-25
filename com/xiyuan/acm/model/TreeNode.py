from com.xiyuan.acm.model.BasicTreeNode import BasicTreeNode


class TreeNode(BasicTreeNode):
    def __init__(self, val):
        super().__init__(val)

    @classmethod
    def fromStr(cls, str):
        split = str.split(",")
        if split[0] == '#':
            return None

        nodes = [TreeNode(int(split[0]))]
        index = 0
        splitLen = len(split)
        while index < splitLen:
            node = nodes[index]
            if node is not None:
                leftChild = index * 2 + 1
                if leftChild < splitLen:
                    newNode = split[leftChild] != '#' and TreeNode(int(split[leftChild])) or None
                    nodes.append(newNode)
                    node.left = newNode
                rightChild = index * 2 + 2
                if rightChild < splitLen:
                    newNode = split[rightChild] != '#' and TreeNode(int(split[rightChild])) or None
                    nodes.append(newNode)
                    node.right = newNode
            index += 1
        return nodes[0]
