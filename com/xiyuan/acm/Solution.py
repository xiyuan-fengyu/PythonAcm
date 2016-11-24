import sys


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

if __name__ == "__main__":
    solution = Solution()

    for n in range(1,12):
        print(n, solution.nthUglyNumber(n))




    # n = 12
    # k = 0
    # print(solution.digitCounts(k, n))



    # n = 15
    # print(solution.trailingZeros(n))



    # print(solution.aplusb(3,4))