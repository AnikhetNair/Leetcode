class Solution(object):

    def superPow(self, a, b):
        """
        :type a: int

        :type b: List[int]

        :rtype: int
        """
        MOD = 1337
        result = 1
        a %= MOD  # Reduce 'a' immediately

        for digit in b:
            # Formula: (previous_result^10 * a^digit) % 1337
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD

        return result