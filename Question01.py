import math


#----------------------------------------
# Step 01 : Input
#----------------------------------------

def input():

    x1 = 2
    x2 = 3

    w1 = 0.4
    w2 =0.6

    bias = 0.5

    print("x1,x2,w1,w2,bias:",x1,x2,w1,w2,bias)
    print("Input Created SUcessfully")

    return x1,x2,w1,w2,bias

#------------------------------------------
# Step 02 : Calculated Weighted sum
#-------------------------------------------

def CalculatedWeighted(x1,x2,w1,w2,bias):

    weightedsum = (x1*w1) + (x2*w2)+bias

    print("Weightedsum:",weightedsum)

    return weightedsum

#---------------------------------------------
# Step 03 : Apply Sigmoid Activation Function
#---------------------------------------------

def ActiavtionFunction( weightedsum):

    output = 1/(1+math.exp(-weightedsum)) # Formula Sigmoid (x) =1/(1 + e ^_(-x)) # math.exp Eulers Number Calculate Krhnhr Function Aha 

    print("Sigmoid Output:",output)

    return output


#---------------------------------------------
# Step 04 : Display Output
#---------------------------------------------

def DisplayOut(output):

    if output >= 0.5:
        print("Output is Close to 01")
    else:
        print("Output is Close to 0")



def main():

    x1,x2,w1,w2,bias = input()

    weightedsum = CalculatedWeighted(x1,x2,w1,w2,bias)

    output = ActiavtionFunction(weightedsum)

    DisplayOut(output)



if __name__ == "__main__":
    main()