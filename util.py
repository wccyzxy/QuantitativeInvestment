import datetime
import numpy as np
from scipy import optimize


def max_draw_down(return_list: list):
    '''
    返回最大回撤

    Params
    ----------
    return_list : 一组数据
    '''
    max_acc = np.maximum.accumulate(return_list)
    i = np.argmax((max_acc - return_list) / max_acc)  # 结束位置
    if i == 0:
        return 0
    j = np.argmax(return_list[:i])  # 开始位置
    return return_list[j] - return_list[i]


def sharpe_ratio(return_list: list):
    '''夏普比率'''
    pass


def xnpv(rate: float, cashflows: list):
    return sum([cf / (1+rate)**((t-cashflows[0][0]).days/365.0) for (t, cf) in cashflows])


def xirr(cashflows: list, guess: float = 0.1):
    '''
    返回一组不一定定期发生的现金流的内部收益率。

    Params
    ----------
    cashflows : [(日期,现金流),...]；
    guess : 对函数 XIRR 计算结果的估计值，一般不用管

    Example
    ----------
    >>> data = [
            (datetime.date(2018, 8, 1), -1000),
            (datetime.date(2018, 9, 1), -1000),
            (datetime.date(2018, 10, 1), -1000),
            (datetime.date(2018, 11, 1), -1000),
            (datetime.date(2018, 12, 1), -1000),
            (datetime.date(2019, 1, 1), -1000),
            (datetime.date(2019, 2, 1), -1000),
            (datetime.date(2019, 3, 1), -1000),
            (datetime.date(2019, 4, 1), -1000),
            (datetime.date(2019, 5, 1), -1000),
            (datetime.date(2019, 6, 1), 12998),
        ]
    >>> xirr(data)
    0.7407757993129621
    '''

    return optimize.newton(lambda r: xnpv(r, cashflows), guess)


if __name__ == "__main__":
    # m = max_draw_down([1, 2, 8, 5, 6, 1, 5, 1])
    data = [
        (datetime.date(2018, 8, 1), -1000),
        (datetime.date(2018, 9, 1), -1000),
        (datetime.date(2018, 10, 1), -1000),
        (datetime.date(2018, 11, 1), -1000),
        (datetime.date(2018, 12, 1), -1000),
        (datetime.date(2019, 1, 1), -1000),
        (datetime.date(2019, 2, 1), -1000),
        (datetime.date(2019, 3, 1), -1000),
        (datetime.date(2019, 4, 1), -1000),
        (datetime.date(2019, 5, 1), -1000),
        (datetime.date(2019, 6, 1), 12998),
    ]
    m = xirr(data)
    print(m)
