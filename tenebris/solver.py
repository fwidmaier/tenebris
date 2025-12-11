from tenebris import d, Dual


def solve(f: callable, b, x0: float = 0, n: int = 10) -> Dual:
    df = d(f)
    res = Dual(x0, 0)
    for _ in range(n):
        g_res = f(res) - b
        dg_val = df(res.a)
        if dg_val == 0:
            raise ZeroDivisionError("zero derivative in solver!")  # TODO: better error mgs!
        res = res - g_res / dg_val
    return res
