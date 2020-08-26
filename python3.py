#Parking lot
#请依次实现以下需求，每完成一个需求进行一次提交 (建议写好单元测试)
#需求1
#构造一个停车场，停车场可以停车和取车，停车成功后得到停车票。 用户取车的时候也需要提供停车票，停车票有效，才可以成功取到车。
#需求2
#构造一个停车小弟（ParkingBoy），他能够将车顺序停放到多个停车场，并可以取出
#需求3
#构造一个聪明的停车小弟（Smart Parking Boy），他能够将车停在空车位最多的那个停车场
#需求4
#构造一个超级停车小弟（Super Parking Boy），他能够将车停在空置率最高的那个停车场
#需求5
#构造停车场的经理（Parking Manager），他要管理多个停车仔，让他们停车，同时也可以自己停车
#需求6 (选做)
#构造停车场的主管（Parking Director），他希望看到一张报表，其中包括经理和每个停车仔所管理的车。 只统计角色(M:Parking Manager B:Boy P:Parking Lot) 空闲车位 已经停车位数
#报表： M 5 20 P 2 10 B 2 5 P 2 5 B 1 5 P 0 3 P 1 2
#1
class Car:
    def __init__(self,carid):
        self.carid = carid
        
class Parking_lot:
    def __init__(self,car_num,p_sum):
        self.car_num = 0                     #已停车数
        self.p_sum = p_sum                   #总车位数
        
    def parking(self,carid,ticket_num):
        if (self.p_sum - self.car_num)>0 :
           ticket_num = self.carid
           print('停车成功')
           self.car_num +=1
        print('没有空余停车位')
        
        
    def pick_up(self,carid):
        if self.carid == ticket_num :
           print('取车成功')
        print('停车票错误')

#2       
class parkingboy(object):
    def _init_(self, park_lot):
        self.park_lots = park_lot

    def check(self):
        for park_lot in self.park_lots:
            if park_lot.p_sum - park_lot.car_num:
                return park_lot
        return None

    def park(self, cars):
        for car in cars:
            if not self.check():
                print('所有停车场已停满，无法停车！')
                return
            self.car_to_parklot[car] = self.check()
        
    def pickup(self, tickets):
        for car, ticket in tickets:
            park_lot = self.car_to_parklot[car]
            park_lot.pick_up(carid)
        
#3
 class smart_parkingboy(parkingboy):  
    def check(self):
        remainder = []
        for park_lot in self.park_lots:
            temp = park_lot.p_sum - park_lot.car_num
            if temp:
                remainder.append(temp)
        myindex = remainder.index(max(remainder))
        return self.park_lots[myindex]
                   
#4   
class super_parkingboy(parkingboy):   
    def check(self):
        remainder = []
        for park_lot in self.park_lots:
            temp = park_lot.p_sum - park_lot.car_num
            temp = temp / park_lot.max_num
            if temp:
                remainder.append(temp)
        myindex = remainder.index(max(remainder))
        return self.park_lots[myindex]

#5
class parkingmanager(parkingboy):   
    def boy_park(self, cars, boy):
        boy.park(cars)
        
    def self_park(self, cars):
        self.park(cars)
               