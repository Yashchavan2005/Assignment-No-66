#-----------------------------------------------------------------
# Step 01 : Take Input , Weight,Bias,Target And Learning Rate
#-----------------------------------------------------------------

def TakeInput():

    Input = 2
    Weights =0.5
    Bias =0.1
    Target =1
    Leraningrate =0.1

    print("Input :",Input)
    print("Weights:",Weights)
    print("Bias:",Bias)
    print("Target:",Target)
    print("Leraningrate:",Leraningrate)
    print("-----------------------------------------------")

    return Input,Weights,Bias,Target,Leraningrate

#-----------------------------------------------------------------
# Step 02:  Calculation Prediction
#-----------------------------------------------------------------

def CalculationPrediction(Input,Weights,Bias):

    prediction = (Input *Weights) + Bias

    print("prediction:",prediction)
    print("---------------------------------------------")

    return prediction


#-----------------------------------------------------------------
# Step 03:  Calculaate Error
#-----------------------------------------------------------------

def CalculateError(prediction,Target):

    Error = Target - prediction
    print("Error:",Error)
    print("------------------------------------------------")

    return Error


#-----------------------------------------------------------------
# Step 04 : Update Weights Using Gradient Descent
#-----------------------------------------------------------------

def UpdateWeights(Weights,Input,Error, Leraningrate):

    oldweight = Weights

    Gradient = Error * Input

    Weight = Weights+(Leraningrate * Gradient)

    print("OldWeight:",oldweight)
    print("Gradient:",Gradient)
    print("Weight:",Weight)
    print("-------------------------------------------------")

    return  oldweight , Gradient,Weight


#-----------------------------------------------------------------
# Step 05 : Display Old Weight And Updated Weight
#-----------------------------------------------------------------

def OldInfoAndUpdated(oldweight,weight):

    print("Old Weight :",oldweight)
    print("Updated Weight:",weight)



def main():

    Input,Weights,Bias,Target,Leraningrate = TakeInput()

    prediction = CalculationPrediction(Input,Weights,Bias)

    Error = CalculateError(prediction,Target)

    oldweight , Gradient,Weight = UpdateWeights(Weights,Input,Error, Leraningrate)

    OldInfoAndUpdated(oldweight,Weight)


if __name__ == "__main__":
    main()
