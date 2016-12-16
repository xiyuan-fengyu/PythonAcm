import sys
from datetime import datetime

from com.xiyuan.acm.model.MinStack import MinStack
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

        primes = [2, 3, 5]
        primeLen = len(primes)
        indexs = [0, 0, 0]
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
    # @param arrA and arrB: sorted integer array arrA and arrB.
    # @return: A new sorted integer array
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

    # http://www.lintcode.com/zh-cn/problem/rotate-string/
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset, start=None):
        if start is None:
            sLen = len(s)
            if sLen == 0:
                return

            offset %= sLen
            if offset != 0:
                count = 0
                for i in range(offset):
                    if count < sLen:
                        count += self.rotateString(s, offset, i)
                    else:
                        break
        else:
            sLen = len(s)
            curChar = s[start]
            count = 0
            nextI = (start + offset) % sLen
            if nextI != start:
                while nextI != start:
                    temp = s[nextI]
                    s[nextI] = curChar
                    curChar = temp
                    count += 1
                    nextI = (nextI + offset) % sLen
                s[start] = curChar
                count += 1
            return count

    # http://www.lintcode.com/zh-cn/problem/search-range-in-binary-search-tree/
    # @param root: The root of the binary search tree.
    # @param k1 and k2: range k1 to k2.
    # @return: Return all keys that k1<=key<=k2 in ascending order.
    def searchRange(self, root, k1, k2):
        if root is None:
            return []
        else:
            val = root.val
            result = []
            if k1 < val:
                lenR = len(result)
                result[lenR:] = result
                result[0:lenR] = self.searchRange(root.left, k1, k2)

            if root.val in range(k1, k2 + 1):
                result.append(root.val)

            if k2 > val:
                result[len(result):] = self.searchRange(root.right, k1, k2)

            return result

    # http://www.lintcode.com/zh-cn/problem/strstr/
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        lenS = len(source)
        lenT = len(target)
        if lenT == 0:
            return 0
        elif lenS < lenT:
            return -1
        else:
            for i in range(lenS - lenT + 1):
                count = 0
                for j in range(lenT):
                    if source[i + j] == target[j]:
                        count += 1
                    else:
                        break

                if count == lenT:
                    return i
            return -1

    # http://www.lintcode.com/zh-cn/problem/strstr/
    def strStrKmp(self, source, target):
        if source is None or target is None:
            return -1

        lenS = len(source)
        lenT = len(target)
        if lenT == 0:
            return 0
        elif lenS < lenT:
            return -1
        else:
            j = 0
            nextArr = self.getKmpNext(target)
            for i in range(lenS):
                while j > 0 and source[i] != target[j]:
                    j = nextArr[j]
                if source[i] == target[j]:
                    j += 1
                if j == lenT:
                    return i - j + 1
            return -1

    def getKmpNext(self, target):
        lenT = len(target)
        nextArr = [0 for i in range(lenT + 1)]
        j = 0
        for i in range(1, lenT):
            while j > 0 and target[i] != target[j]:
                j = nextArr[j]
            if target[i] == target[j]:
                j += 1
            nextArr[i + 1] = j
        return nextArr



    # http://www.lintcode.com/zh-cn/problem/first-position-of-target/
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target, left = None, right = None):
        if left is None and right is None:
            if len(nums) == 0:
                return -1
            else:
                return self.binarySearch(nums, target, 0, len(nums))
        else:
            if left >= right:
                if nums[left] == target:
                    return left
                else:
                    return -1
            else:
                mid = (left + right) // 2
                midVal = nums[mid]
                if midVal > target:
                    return self.binarySearch(nums, target, left, mid - 1)
                elif midVal == target:
                    return self.binarySearch(nums, target, left, mid)
                else:
                    return self.binarySearch(nums, target, mid + 1, right)



    # http://www.lintcode.com/zh-cn/problem/permutations/
    # @param nums: A list of Integers.
    # @return: A list of permutations.
    def permute(self, nums):
        le = len(nums)
        if le == 0:
            return [[]]
        elif le == 1:
            return [nums]
        else:
            result = []
            for i in range(le):
                item = nums[i]
                subNums = nums[0:i] + nums[i + 1: le]
                subResults = self.permute(subNums)
                for subResult in subResults:
                    resultItem = [item]
                    resultItem[1:] = subResult
                    result.append(resultItem)
            return result

    def permuteNoRecursion(self, nums):
        le = len(nums)
        if le == 0:
            return [[]]
        elif le == 1:
            return [nums]
        else:
            result = []
            cur = sorted(nums)
            result.append(cur[0:])
            isLast = False
            while not isLast:
                i = le - 2
                while i > -1 and cur[i] >= cur[i + 1]:
                    i -= 1
                if i > -1:
                    j = le - 1
                    while j > i and cur[j] <= cur[i]:
                        j -= 1
                    if j > i:
                        temp = cur[i]
                        cur[i] = cur[j]
                        cur[j] = temp
                        self.quickSortSection(cur, i + 1, le - 1)
                        result.append(cur[0:])
                    else:
                        isLast = True
                else:
                    isLast = True
            return result

    def quickSortSection(self, arr, left, right):
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1

        if left < right:
            key = arr[left]
            l = left
            r = right
            while l < r:
                while l < r and arr[r] >= key:
                    r -= 1
                arr[l] = arr[r]

                while l < r and arr[l] <= key:
                    l += 1
                arr[r] = arr[l]
            arr[l] = key
            self.quickSortSection(arr, left, l - 1)
            self.quickSortSection(arr, l + 1, right)

    # http://www.lintcode.com/problem/permutations-ii
    def permuteUnique(self, nums):
        le = len(nums)
        if le == 0:
            return [[]]
        elif le == 1:
            return [nums]
        else:
            result = []
            cur = sorted(nums)
            result.append(cur[0:])
            isLast = False
            while not isLast:
                i = le - 2
                while i > -1 and cur[i] >= cur[i + 1]:
                    i -= 1
                if i > -1:
                    j = le - 1
                    while j > i and cur[j] <= cur[i]:
                        j -= 1
                    if j > i:
                        temp = cur[i]
                        cur[i] = cur[j]
                        cur[j] = temp
                        self.quickSortSection(cur, i + 1, le - 1)
                        result.append(cur[0:])
                    else:
                        isLast = True
                else:
                    isLast = True
            return result

    # 找到前n个素数
    def primes(self, n):
        result = [2, 3]
        if n <= 2:
            return result[0:n]

        caches = [2, 3]
        indexs = [0, 0]

        while len(result) < n:
            last = caches[-1]
            next = sys.maxsize
            for i in range(0, len(result)):
                next = min(next, caches[i] * caches[indexs[i]])

            for i in range(last + 1, next + 1):
                if i != next:
                    result.append(i)
                caches.append(i)
                indexs.append(0)

            for i in range(0, len(caches)):
                while caches[i] * caches[indexs[i]] <= next:
                    indexs[i] += 1

        return result[0:n]

    # 找到不大于n的所有素数
    def primesLsThan(self, n):
        if n <= 3:
            return [2, 3][0:n - 1]

        result = []
        nums = [i for i in range(0, n + 1)]
        isPrime = [True for i in range(0, n + 1)]
        isPrime[0] = isPrime[1] = False
        for i in range(2, n + 1):
            if isPrime[i]:
                result.append(nums[i])
                for j in range(i * 2, n + 1, i):
                    isPrime[j] = False
        return result


    # http://www.lintcode.com/zh-cn/problem/subsets/
    def subsetsR(self, arr, doSort = True):
        le = len(arr)
        if le == 0:
           result = []
        elif le == 1:
            result = [arr, []]
        else:
            result = []
            if doSort:
                arr.sort()
            subResult = self.subsetsR(arr[1:], doSort = False)
            for item in subResult:
                tempArr = arr[0:1]
                tempArr[1:] = item
                result.append(tempArr)
                result.append(item)
        return result

    def subsets(self, arr):
        le = len(arr)
        if le == 0:
            result = []
        elif le == 1:
            result = [arr, []]
        else:
            result = [[]]
            arr.sort()
            for i in arr:
                curLe = len(result)
                for j in range(0, curLe):
                    tempArr = result[j][0:]
                    tempArr.append(i)
                    result.append(tempArr)
        return result

if __name__ == "__main__":
    solution = Solution()

    arr = [1,2,3]
    # 递归
    print(solution.subsetsR(arr))
    print(solution.subsets(arr))


    # print(solution.primesLsThan(10))

    # print(solution.primes(10))


    # arr = [1,2,2]
    # # 非递归，字典顺序
    # print(solution.permuteUnique(arr))


    # arr = [1,2,3]
    # # 递归
    # print(solution.permute(arr))
    # # 非递归，字典顺序
    # print(solution.permuteNoRecursion(arr))


    # arr = [1, 2, 3, 3, 4, 5, 10]
    # target = 3
    # print(solution.binarySearch(arr, target))




    # source = "abcdeabceadef"
    # target = "bcdeabcea"
    # print(solution.strStr(source, target))
    # print(solution.strStrKmp(source, target))



    # MinStack.test()



    # root = TreeNode.fromStr("20,8,22,4,12")
    # print(root)
    # print(solution.searchRange(root, 10, 22))





    # string = list("abcdef")
    # offset = 3
    # solution.rotateString(string, offset)
    # print(string)



    # root = TreeNode.fromStr("1,2,3,#,#,4")
    # ser = solution.serialize(root)
    # print(ser)
    # print(solution.deserialize(ser))





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
