import numpy as np
import matplotlib.pyplot as plt



#-----------------------------------------------------
#01 : Accepet Input Values From -10 to  10
#------------------------------------------------------
def AccepetInput():

    X = np.linspace(-10 ,10 ,100)# / np.arrange(-10,10,100) # 100 Always 100 Value Create Krhnhy Okk

    print("X:",X)
    print("-----------------------------------------------------------")


    return X

#-----------------------------------------------------
#02 : Apply Sigmid Activation Function
#------------------------------------------------------

def SigmoidCalculate(X):

    sigmoid = 1/(1+np.exp(-X)) # Sigmoid Formula  = 1(1+np.exp(-X))

    print(" 1(1+np.exp(-X)) Sigmoid :",sigmoid)
    print("Sigmoid Usely for Bianry Classfications")
    print("---------------------------------------------------------------")

    return sigmoid

#-----------------------------------------------------
#03: Apply Relu ACtivation Function
#------------------------------------------------------

def Relu(X):

    relu = np.maximum(0,X) # Relu(X) = max(0,X)

    print("Relu:",relu)
    print("Relu : Commanly Used in Hideen LAyers Of Neurals Networks")
    print("------------------------------------------------------------------")

    return relu

#-----------------------------------------------------
#04 : Apply Tanh Activation Function
#------------------------------------------------------

def TANH(X):

    tan = np.tanh(X) # -1 To +1   (Tanh -1 To +1 ) 

    print("Tanh :",tan)
    print("Tanh : Produce Output Between -1 To +1")
    print("---------------------------------------------------")

    return tan


#-----------------------------------------------------
#05 : Plot All ACtivation Function 
#------------------------------------------------------

def PlotActivation(sigmoid,relu,tan,X):

    plt.plot(X,sigmoid,label="sigmoid")
    plt.plot(X,relu,label="relu")
    plt.plot(X,tan,label="tan")

    plt.xlabel("input")
    plt.ylabel("Output")

    plt.title("Activation Functions")

    plt.legend()
    plt.grid()
    plt.show()

    

def main():

    X= AccepetInput()

    sigmoid = SigmoidCalculate(X)

    relu  = Relu(X)

    tan =TANH(X)

    PlotActivation(sigmoid,relu,tan,X)




















if __name__ == "__main__":
    main()