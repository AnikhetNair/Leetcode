class Solution(object):

    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        # The state cycle repeats every 14 days after day 1
        n = (n - 1) % 14 + 1

        for _ in range(n):
            next_day = [0] * 8  # Create a fresh array to avoid in-place mutation

            # First and last cells (index 0 and 7) remain 0
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    next_day[i] = 1
                else:
                    next_day[i] = 0

            cells = next_day  # Update cells to the new snapshot

        return cells