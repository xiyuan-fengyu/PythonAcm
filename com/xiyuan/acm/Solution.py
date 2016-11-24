import sys

from com.xiyuan.acm.model.TreeNode import TreeNode


class Solution:

    """
    http://www.lintcode.com/zh-cn/problem/a-b-problem/problem
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        if b == 0:
            return a
        else:
            return self.aplusb(a ^ b, (a & b) << 1)






    # http://www.lintcode.com/zh-cn/problem/trailing-zeros/
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        if n < 5:
            return 0
        else:
            k = n // 5
            return k + self.trailingZeros(k)





    # http://www.lintcode.com/zh-cn/problem/digit-counts/
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        count = k == 0 and 1 or 0
        for i in range(n + 1):
            temp = i
            while temp > 0:
                count += temp % 10 == k and 1 or 0
                temp //= 10

        return count





    # http://www.lintcode.com/zh-cn/problem/ugly-number-ii/
    # @param {int} n an integer.
    # @return {int} the nth prime number as description.
    def nthUglyNumber(self, n):
        if n == 1:
            return 1

        primes = [2,3,5]
        primeLen = len(primes)
        indexs= [0,0,0]
        uglys = [1]
        for i in range(n - 1):
            newMin = sys.maxsize
            for j in range(primeLen):
                temp = uglys[indexs[j]] * primes[j]
                if temp < newMin:
                    newMin = temp
            uglys.append(newMin)

            for j in range(primeLen):
                while uglys[indexs[j]] * primes[j] <= newMin:
                    indexs[j] += 1
        return uglys[-1]






    # http://www.lintcode.com/zh-cn/problem/kth-largest-element/
    # @param k & arr a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, arr):
        arrLen = len(arr)
        return self.kthLargestElement1(arrLen - k, arr, 0, arrLen - 1)

    def kthLargestElement1(self, k, arr, left, right):
        if left == right:
            return arr[left]
        else:
            key = arr[left]
            i = left
            j = right
            while i < j:
                while i < j and arr[j] >= key:
                    j -= 1
                arr[i] = arr[j]

                while i < j and arr[i] <= key:
                    i += 1
                arr[j] = arr[i]

            arr[i] = key
            if i == k:
                return key
            elif k < i:
                return self.kthLargestElement1(k, arr, left, i - 1)
            else:
                return self.kthLargestElement1(k, arr, i + 1, right)




    # http://www.lintcode.com/zh-cn/problem/merge-two-sorted-arrays/
    #@param arrA and arrB: sorted integer array arrA and arrB.
    #@return: A new sorted integer array
    def mergeSortedArray(self, arrA, arrB):
        lenA = len(arrA)
        lenB = len(arrB)
        if lenA == 0:
            return arrB
        elif lenB == 0:
            return arrA
        else:
            arrNew = []
            index = 0
            i = 0
            j = 0
            while i < lenA and j < lenB:
                if arrA[i] <= arrB[j]:
                    arrNew.append(arrA[i])
                    i += 1
                else:
                    arrNew.append(arrB[j])
                    j += 1
                index += 1
            if i < lenA:
                arrNew[index:] = arrA[i:]
            else:
                arrNew[index:] = arrB[j:]
            return arrNew






    # http://www.lintcode.com/zh-cn/problem/binary-tree-serialization/
    # @param root: An object of TreeNode, denote the root of the binary tree.
    # This method will be invoked first, you should design your own algorithm
    # to serialize a binary tree which denote by a root node to a string which
    # can be easily deserialized by your own "deserialize" method later.
    def serialize(self, root):
        nodes = []
        nodes.append(root)

        ser = ""
        index = 0
        while index < len(nodes):
            node = nodes[index]
            index += 1
            if node != None:
                ser += str(node.val) + ","
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                ser += "#,"

        if ser == "":
            return "#"
        else:
            end = len(ser) - 2
            while end > -1:
                if ser[end] == '#':
                    end -= 2
                else:
                    break
            return ser[0:end + 1]

    # @param data: A string serialized by your serialize method.
    # This method will be invoked second, the argument data is what exactly
    # you serialized at method "serialize", that means the data is not given by
    # system, it's given by your own serialize method. So the format of data is
    # designed by yourself, and deserialize it here as you serialize it in
    # "serialize" method.
    def deserialize(self, data):
        split = data.split(",")
        if split[0] == '#':
            return None

        nodes = []
        nodes.append(TreeNode(int(split[0])))
        index = 0
        splitLen = len(split)
        while index < splitLen:
            node = nodes[index]
            if node != None:
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




if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    ser = solution.serialize(root)
    print(ser)
    print(solution.deserialize(ser).val)
    print(solution.deserialize(ser).right.left.val)





    # A=[1,2,3,4,6,7]
    # B=[2,4,5]
    # print(solution.mergeSortedArray(A, B))




    # arr = [1,2,3,4,5]
    # k = 1
    # print(solution.kthLargestElement(k, arr))




    # for n in range(1,12):
    #     print(n, solution.nthUglyNumber(n))




    # n = 12
    # k = 0
    # print(solution.digitCounts(k, n))



    # n = 15
    # print(solution.trailingZeros(n))



    # print(solution.aplusb(3,4))