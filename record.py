# from . import util
import datetime
from typing import Any, Dict, List
from typing_extensions import Literal
import pandas as pd
import numpy as np
import statistics

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
        '''
        i=np.argmax((np.maximun.accumulate(list)-list)/np.maximum.accumulate(list))    #结束位置
        if i==0:
            return 0
        j=np.argmax(list[:i])    #开始位置
        return (list[j]-list[i])/(list[j])



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
