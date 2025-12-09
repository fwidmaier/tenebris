from tenebris import d


def solve(f: callable, b: float, x0: float = 0, n: int = 50) -> float:
    g = lambda x: f(x) - b
    dg = d(g)
    res = x0
    for _ in range(n):
        res = res - g(res) / dg(res)
    return res
