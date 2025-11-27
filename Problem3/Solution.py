class Solution:
    def check_coupon(self, n, x, y, prices):
        """
        Determines whether Chef should buy the discount coupon or not.

        Parameters:
        n (int): Number of items
        x (int): Cost of the coupon
        y (int): Discount per item
        prices (List[int]): List of item prices

        Returns:
        str: "COUPON" if buying the coupon is cheaper, otherwise "NO COUPON"
        """
        total_without_coupon = sum(prices)
        total_with_coupon = x + sum(max(p - y, 0) for p in prices)
        
        if total_with_coupon < total_without_coupon:
            return "COUPON"
        else:
            return "NO COUPON"


# Example of using this class
if __name__ == "__main__":
    T = int(input())
    solution = Solution()
    for _ in range(T):
        n, x, y = map(int, input().split())
        prices = list(map(int, input().split()))
        print(solution.check_coupon(n, x, y, prices))
