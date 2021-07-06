#!/usr/bin/env python
# coding: utf-8


def model_imp():
    import numpy as np
    from keras.models import load_model
    
    model = load_model('dummy_data_model.h5')

    n = 0
    prediction = np.zeros((1,79))
    sfvec = np.zeros((1,79))
    pwvec = np.zeros((1,79))

    sf = 7
    while (sf<=12):
        pw = 3
        while (pw<=27):
            inpt = np.array([[distance/10000], [Walls/3], [LOS/4], [sf/12], [pw/27]])
            inpt = inpt.reshape(1,-1)
            pred = model.predict(inpt)
            prediction[0][n] = pred[0][0]
            pwvec[0][n] = pw
            sfvec[0][n] = sf
            pw = pw + 2
            n = n+1
        inpt = np.array([[distance/10000], [Walls/3], [LOS/4], [sf/12], [pw/27]])
        inpt = inpt.reshape(1,-1)
        pred = model.predict(inpt)
        prediction[0][n] = pred[0][0]
        pwvec[0][n] = pw
        sfvec[0][n] = sf
        sf = sf+1

    new_pwvec = np.zeros((1,13))
    new_prediction = np.zeros((1,13))
    n = 0
    for i in range(0,78):
        if(sfvec[0][i]==SF):
            new_pwvec[0][n] = pwvec[0][i]
            new_prediction[0][n] = format(prediction[0][i], '.2f')
            n = n+1
    for i in range(0,13):
        if(new_prediction[0][i]==PRR):
            Power = new_pwvec[0][i]
    return Power


