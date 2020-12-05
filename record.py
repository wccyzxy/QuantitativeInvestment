# from . import util
import datetime
from typing import Any, Dict, List
from typing_extensions import Literal
import pandas as pd
import numpy as np
import statistics
from scipy import optimize

class Book:
    '''
    某一投资基金的记账本

    Members
    ---------
    name : 基金名称；
    data : 投资、收入的金额记录。

    '''

    def __init__(self, name: str):
        self.name = name
        self.data = pd.DataFrame(columns=('Date', 'CashFlow'))

    def invest(self, date: str, money: float):
        '''
        Params
        --------
        date : 日期(yyyy/mm/dd)；
        money : 投入的本金
        '''
        self.data = self.data.append({'Date': pd.to_datetime(date), 'CashFlow': -money},
                                     ignore_index=True)

    def take_back(self, date: str, money: float):
        '''
        Params
        --------
        date : 日期(yyyy/mm/dd)；
        money : 收回的本金
        '''
        self.data = self.data.append({'Date': pd.to_datetime(date), 'CashFlow': money},
                                     ignore_index=True)

    def get_statistics(self):
        '''
        计算本金，收益，算术收益

        Params
        --------
        capital : 本金；
        profit : 收益
        arithmetical_profit ：  算术收益
        '''
        capital=0
        profit=0    
        arithmetical_profit=0   
        for (date,money) in self.data:
            if money < 0:
                capital+=-money
            else:
                profit+=money
        profit-=capital
        arithmetical_profit=profit/capital
        return (capital,profit,arithmetical_profit)
    
    def xirr(self):
        '''
        计算xirr收益

        Params
        --------
        xirr_profit: xirr收益
        guess: 对函数 xirr 计算结果的估计值
        '''
        guess = 0.1
        try:
            return optimize.newton(lambda r: xnpv(r,self.data),guess)
        except:
            print('Calc Wrong')
    
    def xnpv(rate, cashflows):
        '''
        用于计算xirr相关的函数
        '''
        return sum([cf/(1+rate)**((t-cashflows[0][0]).days/365.0) for (t,cf) in cashflows])    

    def to_dict(self) -> List[Dict[str, Any]]:
        '''
        返回一系列dict
        '''
        return self.data.to_dict(orient='records')


class Fund:
    '''
    基金类，用于爬取跟踪数据
    占坑，暂时没有填坑打算
    '''
    def __init__(self, name: str):
        self.name = name
        self.last_update_time = 0

        # 数据
        self.url = ''
        self.market_cap = []

        # 指标
        self.max_draw_down = 0.0
        self.sharpe_ratio = 0.0
        self.xirr = 0.0
        self.annual_volatility = 0.0

    def pull_data(self):
        pass

    def update_data(self):
        pass

    def max_drawdown(list):
        '''
        最大回撤率

        Params
        --------
        i : 结束位置
        j : 开始位置 
        '''
        i=np.argmax((np.maximun.accumulate(list)-list)/np.maximum.accumulate(list))
        if i==0:
            return 0
        j=np.argmax(list[:i])
        return (list[j]-list[i])/(list[j])
    
    def get_stdev(list):
        '''
        计算样本标准差
        '''
        return statistics.stdev(list)
    
    def get_stdevp(list):
        '''
        计算整体标准差 
        '''
        return statistics.pstdev(list)



class User:
    '''
    用户类，存有用户所有记账本
    '''
    def __init__(self, user_name: str):
        self.name = user_name
        self.book: Dict[str, Book] = {}

    def new_record_book(self, name: str):
        if name in self.book:
            raise ValueError('存在重名的账本。')
        self.book[name] = Book(name)

    def rename_book(self, old_name: str, new_name: str):
        self.book[old_name].name = new_name
        self.book[new_name] = self.book.pop(old_name)

    def delete_book(self, book_name: str):
        self.book.pop(book_name)

    def add_record(self, target_book: str, date: str, money: float, action: Literal['invest', 'take_back']):
        if action == 'invest':
            self.book[target_book].invest(date, money)
        elif action == 'take_back':
            self.book[target_book].take_back(date, money)
        else:
            raise ValueError("无效参数，action应为'invest'或'take_back'。")

    def delete_record(self, target_book: str):
        pass

    def to_dict(self) -> Dict[str, list]:
        result = {}
        for book_name, book in self.book.items():
            result[book_name] = book.to_dict()
        return result
    
    @classmethod
    def load_from_json(cls,filename):
        pass



if __name__ == "__main__":
    # 暂时用来测试
    user = User('AAAA')
    user.new_record_book('a')
    user.add_record('a', '20010101', 1000, 'invest')
    user.add_record('a', '20021122', 550, 'take_back')

    a = user.to_dict()
    print(a)
    # for _, d, m in b.data.itertuples():
    #     print(d, m)
    # print(b.data)
