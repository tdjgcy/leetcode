class Solution(object):

    # 202
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        got = set()
        while n != 1 and n not in got:
            got.add(n)
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10
            n = sum

        return n == 1
      # 204
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5) +1):
            if prime[i] == 1:
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
        return sum(prime)
