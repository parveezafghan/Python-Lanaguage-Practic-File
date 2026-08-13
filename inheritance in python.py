class AFghanistan:
    def __init__(self,province1,province2,province3,province4):
        self.province1=province1
        self.province2=province2
        self.province3=province3
        self.province4=province4

        return print("famous provinec of Afghanistan\n first is [{}] and second is [{}] and third is [{}] finialy is [{}]".format(self.province1,self.province2,self.province3,self.province4))


class sbout_Afghanistan(AFghanistan):
    def __init__(self,histry,first_name,second_name,third_name):
        self.first_name=first_name
        self.second_name=second_name
        self.third_name=third_name

        return print("the first name of AFghanistan was [{}], the second name of Afghanistan was[{}] and third name of Afghanistan is[{}]".format(self.first_name,self.second_name,self.third_name))


class king_of_AFghistan(AFghanistan):

    def __init__(self,first_king):
        self.first_king=first_king

        return print("the first name of AFghanistan was [{}]".format(self.first_king))

obj=king_of_AFghistan("wama")
class president_of_AFghanistan(AFghanistan):
    print('------------------------------------------------------------------------------------------')

    def __init__(self,first_president,second_president,third_presiden):
        self.first_presiden=first_president
        self.second_president=second_president
        self.third_president=third_presiden
        #self.fourth_president=fourth_president
        return print("the first president of AFghanistan is[{}] ,second president of AFghanistan is[{}] ,third president of AFghanistan is [{}] ".format(self.first_presiden,self.second_president,self.third_president))
    
obj2=president_of_AFghanistan("sardar mohammad dawad",'hamad karzi',"mohammad ashrap ghani")
print("------------------------------------------------------------------------------")
class history_of_AFghanistan(AFghanistan):

    def __init__(self,start_point_of_histor,first_period,second_period,third_period,fourth_period,province1,province2,province3,province4):
        AFghanistan.__init__(self,province1,province2,province3,province4)
    
        self.start_point_of_histor=start_point_of_histor
        self.first_period=first_period
        self.second_period=second_period
        self.third_period=third_period
        self.fourth_period=fourth_period
   

        return print("start date of Afghanistan is [{}] ,first period is started was [{}] the second period is start was [{}] the theird period is was started [{}] the fouth period was started [{}]".format(self.start_point_of_histor,self.second_period,self.second_period,self.third_period,self.fourth_period))
    
     


obj1=history_of_AFghanistan("5000 yers ago","2500 yers ago AD",'100 AD',"200 Bc","1750 Bc","Bamvan","Norastan","paktya","Konar")
print("---------------------------------------------------------------------------------------")