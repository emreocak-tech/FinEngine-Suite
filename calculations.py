import math
from abc import ABC,abstractmethod
class AbstractInterest(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def basic_interest(self,value,rate):
        pass
    @abstractmethod
    def compound_interest(self,value,rate,time):
        pass
    @abstractmethod
    def calculate_dividient(self,value,rate,time,dividend_rate,minimum_wage):
        pass
class Interest(AbstractInterest):
    def basic_interest(self,value,rate):
        rate=rate/100
        value=(value*rate)
        return value
    def compound_interest(self,value,rate,time):
        rate=rate/100
        pre_result=math.pow(1+rate,time)
        result=value*pre_result
        return result
    def calculate_dividient(self,value,rate,time,divident_rate,minimum_wage):
        rate=rate/100
        pre_result=math.pow(1+rate,time)
        result=value*pre_result
        result=result/divident_rate
        result=result/12
        if result>minimum_wage:
            return True
        else:
            return False

class AbstractNPV(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calculate_pv(self,value,rate,time):
        pass
    @abstractmethod
    def profit_for_me(self,value,future_value,rate,time):
        pass
    @abstractmethod
    def calculate_terminal_value(self,value,growth_rate,rate,time):
        pass
    @abstractmethod
    def calculate_stock_value(self,value_one,value_two,value_three,rate,growth_rate,stock_shares):
        pass
class Npv(AbstractNPV):
    def calculate_pv(self,value,rate,time):
        rate=rate/100
        pre_result=math.pow(1+rate,time)
        result=value/pre_result
        return result
    def profit_for_me(self,value,future_value,rate,time):
        rate=rate/100
        pre_result=math.pow(1+rate,time)
        future_value=future_value/pre_result
        if future_value>value:
            return True
        else:
            return False
    def calculate_terminal_value(self,value,growth_rate,rate,time):
        rate=rate/100
        growth_rate=growth_rate/100
        pre_result=(1+growth_rate)/(rate-growth_rate)
        result=value*pre_result
        return result
    def calculate_stock_value(self,value_one,value_two,value_three,rate,growth_rate,stock_shares):
        rate=rate/100
        growth_rate=growth_rate/100
        pre_result_one=math.pow(1+rate,1)
        result_one=value_one/pre_result_one
        pre_result_two=math.pow(1+rate,2)
        result_two=value_two/pre_result_two

        terminal_value=value_three*((1+growth_rate)/(rate-growth_rate))

        pre_result_three=math.pow(1+rate,3)
        result_three=(value_three+terminal_value)/pre_result_three

        result=result_one+result_two+result_three

        result=result/stock_shares

        return result
