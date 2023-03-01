#CH3 Byes Filter: Rotbot Observe and Push Test

import math
import random
'''       Push Prediction:              '''
#---------Predict prob table:--------------
#         p_OPO = self.push_if_open
#         p_CPO = 1 - self.push_if_open
#         p_OPC = self.push_if_close
#         p_CPC = 1 - self.push_if_close

'''       Observe_Correction:           '''
#---------Correct prob table:--------------
#         p_OO = self.observe_if_open
#         p_CO = 1 - self.observe_if_open
#         p_OC = self.observe_if_close
#         p_CC = 1 - self.observe_if_close

def Normalize_Fector(bel_1,bel_2):
    Result = (bel_1 + bel_2)**-1
    return Result

#Door:
class Door():
    def __init__(self):
        self.state = "unknown"
        self.open_rate = 0.5

    def Door_define_State(self):
        if random.random() > self.open_rate:
            self.state = 1      #1: open
        else:
            self.state = 0      #0: close
        pass

#Robot:
class Robot():
    def __init__(self):
        #Observe prob:
        self.observe_if_open = 0.6       #if the door is open, observe is open = 0.6, observe is closed = 0.4
        self.observe_if_close = 0.2      #if the door is close, observe is open = 0.2,oberve is closed = 0.8
        #Push prob:
        self.push_if_open = 1            #if the door is open, push then open =1, push but closed = 0 
        self.push_if_close = 0.8         #if the door is close, push then open = 0.8, push but closed = 0.2
        #No Push prob:
        self.no_push_if_open = 1         #if the door is open, no push then open =1, no push but closed = 0  
        self.no_push_if_close = 0       

        
        #Robot's Observation:
        self.oberve_record = 0.5   #Robot's Observation Result
        self.p_o_X = 0   #Robot's Observation Result
        self.p_c_X = 0   #Robot's Observation Result
        self.prob_observ = 0   #Robot's Observation Result

    def Observe(self, door):
        print("Robot Observe the Door..")
        if door.state == 1:                             #door is open in reality
            if random.random() < self.observe_if_open:
                self.oberve_record = 1 
                self.prob_observ = self.observe_if_open
                self.p_o_X = 0.6                        #no matter the Xt-1 is, Xt = open after push
                self.p_c_X = 0.4                        #no matter the Xt-1 is, Xt = close after push

            else:                                       
                 self.oberve_record = 0
                 self.prob_observ = 1 - self.observe_if_open
                 self.p_o_X = 0.2                       #no matter the Xt-1 is, Xt = open after push
                 self.p_c_X = 0.8                       #no matter the Xt-1 is, Xt = close after push

        else:                                           #door is close in reality
            if random.random() < self.observe_if_close:
                self.oberve_record = 1
                self.prob_observ = self.observe_if_close
                self.p_o_X = 0.6                        #no matter the Xt-1 is, Xt = open after push
                self.p_c_X = 0.4                        #no matter the Xt-1 is, Xt = close after push
            else:
                self.oberve_record = 0
                self.prob_observ = 1 - self.observe_if_close
                self.p_o_X = 0.2                        #no matter the Xt-1 is, Xt = open after push
                self.p_c_X = 0.8                        #no matter the Xt-1 is, Xt = close after push

    def Push(self, door):
        print("Robot Push the Door !")
        if door.state == 1:
            if random.random() < self.push_if_open:
                door.state = 1
            else:
                 door.state = 0        
        else:
            if random.random() < self.push_if_close:
                door.state = 1
            else:
                 door.state = 0
                
    
'''Main'''
door = Door()
robot  =  Robot()
bel_open = door.open_rate
bel_close = 1 - door.open_rate
print("-"*15+"Start"+"-"*15)

#0. No Push Prediction:
Predict_bel_open = robot.no_push_if_open * bel_open + robot.no_push_if_close * bel_close
Predict_bel_close = (1 - robot.no_push_if_open)* bel_open + (1-robot.no_push_if_close)*bel_close
#1.Correction/ Observation:
robot.Observe(door)
obserevation = robot.oberve_record              #observation : test record

bel_open = Predict_bel_open * robot.p_o_X  
bel_close = Predict_bel_close * robot.p_c_X
#Normalize Fector
N = Normalize_Fector(bel_open, bel_close)
bel_open = N * bel_open
bel_close = N * bel_close
#print result
print("Robot observe record (0:close , 1:open) : ",obserevation)
#print(robot.prob_observ)       #only a prob of robot's. It's Robot's observation attribute
print("Predict_[bel_open, bel_close]: ",Predict_bel_open, Predict_bel_close)
print("Correct_[bel_open, bel_close]: ",bel_open, bel_close)


#Action: Push 
print("")
robot.Push(door)
#2.Prediction
Predict_bel_open = robot.push_if_open * bel_open + robot.push_if_close * bel_close
Predict_bel_close = (1 - robot.push_if_open)* bel_open + (1-robot.push_if_close)*bel_close
#3.Correction/ Observation:
robot.Observe(door)                              #observation : test record
obserevation = robot.oberve_record

bel_open = Predict_bel_open * robot.p_o_X  
bel_close = Predict_bel_close * robot.p_c_X
#Normalize Fector
N = Normalize_Fector(bel_open, bel_close)
bel_open = N * bel_open
bel_close = N * bel_close

print("Robot observe record (0:close , 1:open) : ",obserevation)
#print(robot.prob_observ)                       #only a prob of robot's. It's Robot's observation attribute
print("Predict_[bel_open, bel_close]: ",Predict_bel_open, Predict_bel_close)
print("Correct_[bel_open, bel_close]: ",bel_open, bel_close)


print("-"*15+"Finish"+"-"*15)






