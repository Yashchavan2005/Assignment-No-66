import math

#------------------------------------------------------
# 01 : Take ACtual And Prediced
#------------------------------------------------------

def ActualPrediced():

    actual = (1,0,1,1,0)

    predicted = (0.2,0.3,0.8,0.3,0.9)

    print("ACtual Values:",actual)

    print("Predicted Values:",predicted)

    return actual,predicted


#------------------------------------------------------
# 02 : Calculated Mean Sequred Error
#------------------------------------------------------

def MSECalculate (actual,predicted):

    MSE=0

    for i in range(len(actual)):

        Error = actual[i] - predicted[i]

        MSE = MSE +(Error **2)

    MSE = MSE/len(actual)

    print("Mean Squared Error:",MSE)
    print("Mse Mainly Used For Regression")
    print("-------------------------------------------------------------------------------")

    return MSE


#------------------------------------------------------
# 03 : Calculated Binary Cross Entropy
#------------------------------------------------------

def BinaryCrossEntropy(actual,predicted):

    BCE =0 

    for i in range(len(actual)):

        BCE = BCE+(
            actual[i] *math.log(predicted[i])
            
            +
            (1-actual[i]) * math.log(1-predicted[i])
        )

    BCE = -BCE/len(actual)

    print("Binary Cross Entropy :",BCE)
    print("Binary Cross Entropy Used For Binary Classfication")
    print("----------------------------------------------------------------------")

    return BCE

        
def main():

    actual,predicted = ActualPrediced()

    MSE = MSECalculate(actual,predicted)

    BCE = BinaryCrossEntropy(actual,predicted)

    
if __name__ == "__main__":
    main()