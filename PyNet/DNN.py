
import numpy as np


#n_h -> no. of hidden units in layer_1
#n2_h -> no. of hidden units in layer_2


x = np.random.rand(2,40)                # random numbers
y = np.random.rand(1,40)                #random numbers


def initialize_params(x,y,n_h,n2_h):

    n_x = x.shape[0]
    n_y = y.shape[0]
    n_h = n_h


    W1 = np.random.rand(n_h, n_x)                          #(4,2)       layer 1
    b1 = np.random.rand(n_h,1)

    W2 = np.random.rand(n2_h, n_h)                           #(8,4)         layer 2
    b2 = np.random.rand(n2_h,1)

    W3 = np.random.rand(n_y, n2_h)                          #(1,8)          output layer
    b3 = np.random.rand(n_y,1)



    params = {'W1':W1, 'W2':W2, 'b1':b1, 'b2':b2, 'W3':W3, 'b3':b3}

    return params


def sigmoid(z):
    return 1/(1+(np.exp(-z)))


def relu(z):
    return (z * (z > 0))


def forward_propagate(x, params):

    W1 = params['W1']
    W2 = params['W2']
    W3 = params['W3']
    b1 = params['b1']
    b2 = params['b2']
    b3 = params['b3']


    z1 = np.dot(W1, x) + b1                           #(4,2) dot (2,40) => (4,40)
    A1 = relu(z1)                                                               

    z2 = np.dot(W2, A1) + b2                           #(8,4) dot (4,40) => (8,40)
    A2 = relu(z2)

    z3 = np.dot(W3, A2) + b3                            #(1,8) dot (8,40) => (1,40) 
    A3 = sigmoid(z3)


    cache = {'A1': A1, 'A2': A2, 'A3': A3,'z1': z1, 'z2': z2, 'z3':z3 }

    return A3, cache



def backward_propagate(params,cache,x,y):

    m = x.shape[1]


    W1 = params['W1']
    W2 = params['W2']
    W3 = params['W3']

    A1 = cache['A1']
    A2 = cache['A2']
    A3 = cache['A3']


    # dZ2 = A2-y                                                      #(1,40)
    # dW2 = (1/m) * np.dot(dZ2, A1.T)                                 #(1,40) dot (40,4) => (1,4)
    # db2 = (1/m) * np.sum(dZ2, axis=1, keepdims=True)


    # dZ1 = np.dot(W2.T, dZ2) * (1- np.power(A1,2))                   #(4,1) dot (1,40) => (4,40)
    # dW1 = (1/m) * np.dot(dZ1, x.T)                                  #(4,40) dot (40,2) => (4,2)    
    # db1 = (1/m) * np.sum(dZ1, axis=1, keepdims=True)


    dZ3 = A3-y                                                     
    dW3 = (1/m) * np.dot(dZ3, A2.T)                                 
    db3 = (1/m) * np.sum(dZ3, axis=1, keepdims=True)


    dZ2 = np.dot(W3.T, dZ3) * (1- np.power(A2,2))                   
    dW2 = (1/m) * np.dot(dZ2, A1.T)                                  
    db2 = (1/m) * np.sum(dZ2, axis=1, keepdims=True)

    dZ1 = np.dot(W2.T, dZ2) * (1-np.power(A1,2))
    dW1 = (1/m) * np.dot(dZ1, x.T)
    db1 = (1/m) * np.sum(dZ1, axis=1, keepdims=True)

    grads = {   'dW1':dW1,
                'dW2':dW2,
                'dW3':dW3,
                'db1':db1,
                'db2':db2,
                'db3':db3,
                'dZ1':dZ1,
                'dZ2':dZ2,
                'dZ3':dZ3
                }

    return grads


def update_params(grads, params, lr):


    W1 = params['W1']
    W2 = params['W2']
    W3 = params['W3']
    b1 = params['b1']
    b2 = params['b2']
    b3 = params['b3']


    dW1 = grads['dW1']
    dW2 = grads['dW2']
    dW3 = grads['dW3']
    db1 = grads['db1']
    db2 = grads['db2']
    db3 = grads['db3']


    W1 = W1 - lr * dW1
    W2 = W2 - lr * dW2
    W3 = W3 - lr * dW3
    b1 = b1 - lr * db1
    b2 = b2 - lr * db2
    b3 = b3 - lr * db3

    params = {
        'W1':W1,
        'W2':W2,
        'W3':W3,
        'b1':b1,
        'b2':b2,
        'b3':b3,
    }

    return params


def mse(preds, labels):
    return np.sum((preds - labels)**2)/preds.shape[1]

def train(x,y,n_h,n2_h, epochs, lr=0.01):


    params = initialize_params(x,y,n_h,n2_h)



    for i in range(0, epochs):

        A2, cache = forward_propagate(x, params)

        

        gradients = backward_propagate(params, cache,x,y)

        params = update_params(grads=gradients, params=params, lr=lr)




    predictions, _  = forward_propagate(x, params)

    loss = mse(predictions, y)

    print('predictions:', predictions)
    print('loss:', loss)




#train model
train(x,y,n_h=4,n2_h=8, epochs=10)

























