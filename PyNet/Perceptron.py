import numpy as np


np.random.seed(1)

class nn():
    def __init__(self,x,y,gate_name, lr=0.01):

        self.x = x    # x of shape(m, n)
        self.y = y    # y of shape(m, 1)
        self.lr = lr
        self.gate_name = gate_name # name
            
    def initialize_params(self,x,y):

        theta = np.random.rand(x.shape[1],y.shape[0])      # initialize the weight matrix of shape(n, 1)
        b = 0                                              # bias of shape (1) or (1,)

        return theta, b


    def sigmoid(self,z):                                    # calculate sigmoid
        return 1/(1+np.exp(-z))

    def forward(self, x, theta, b):                         # forward pass

        z = np.dot(x,theta) + b                             # dot product of (m, n) , (n,1) => (m,1)

        A = self.sigmoid(z)

        return A.T                                        # (1,m)


    def mse(self,A,y):                                      #mean squared error

        loss = np.sum((A-y)**2)/A.shape[0]

        return loss


    def update_params(self,A,x,y,lr,theta,b):                     #calculate gradients and update parameters

        theta = theta - (lr * (np.dot(x.T,(A-y).T)/A.shape[0]))    # (n,m) dot (m,1) => (n,1) 
        b = b - (lr * (np.sum(A-y)/A.shape[0]))                    # update bias
        return theta,b


    def train(self):

        theta,b = self.initialize_params(self.x, self.y)

        for i in range(0,100):                                           #train loop

            A = self.forward(self.x, theta, b)

            theta,b = self.update_params(A, self.x, self.y, self.lr, theta, b)

        self.theta = theta
        self.bias = b

        
        preds = self.forward(x, theta,b)

        loss = self.mse(preds,self.y)

        preds = preds > 0.5

        preds = preds.astype(int)

        return loss, preds


def print_results(loss, preds, labels, model):

    print("Logical operation: ", model.gate_name)
    print('Loss: ', loss)
    print('Predictions: ', preds)
    print('Actual values: ', labels)
    print('Weights: ', model.theta.ravel())
    print("Bias: ", model.bias.ravel())







#Data for AND gate
x = np.array([[1,1],[0,1],[0,0],[1,1],[1,0],[1,1],[0,0],[1,0],[0,1],[1,1],[1,1]])
y = np.array([[1,0,0,1,0,1,0,0,0,1,1]])

model = nn(x, y, gate_name='AND')
loss, preds = model.train()

print_results(loss, preds, y, model=model)



print('')



#Data for OR gate
x = np.array([[1,0],[0,1],[0,0],[1,1],[0,0],[0,0]])
y = np.array([[1,1,0,1,0,0]])

model = nn(x, y, gate_name='OR')
loss, preds = model.train()

print_results(loss, preds, y, model=model)


print('')


#Data for NOR gate
x = np.array([[1,0],[0,1],[0,0],[1,1],[0,0],[0,0],[1,0],[0,1],[0,0],[1,1],[0,0],[0,0]])
y = np.array([[0,0,1,0,1,1,0,0,1,0,1,1]])

model = nn(x, y, gate_name='NOR')
loss, preds = model.train()

print_results(loss, preds, y, model=model)






    



