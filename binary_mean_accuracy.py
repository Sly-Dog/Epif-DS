import numpy as np


def binary_mean_accuracy(Y, Y_hat):
    true_positive =  []
    true_negative =  []
    false_positive = []
    false_negative = []
    
    
    for y, y_hat in zip(Y, Y_hat):
        
        if   y == 0 and y_hat == 0:
            true_negative.append(1)
            
        elif y == 0 and y_hat == 1:
            false_negative.append(1)
            
        elif y == 1 and y_hat == 1:
            true_positive.append(1)
            
        elif y == 1 and y_hat == 0:
            false_positive.append(1)


    accuracy_positive = (
        abs( len(true_positive) - len(false_positive) )
        /  ( len(true_positive) + len(false_positive) )
    )
    
    accuracy_negative = (
        abs( len(true_negative) - len(false_negative) ) 
        /  ( len(true_negative) + len(false_negative) )
    )

    binary_mean_accuracy = np.mean([accuracy_positive, accuracy_negative])
    return binary_mean_accuracy
