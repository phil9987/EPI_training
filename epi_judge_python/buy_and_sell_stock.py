from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    max_profit = 0.0
    current_min = prices[0]
    for p in prices:
        current_min = min(current_min, p)
        max_profit = max(max_profit, p - current_min)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
