import numpy as np

def distance(x1,y1,x2,y2):
    dist = (x1-y1)**2 + (x2-y2)**2
    return dist

def weight_updation(w,lr,x):
    w_new = w + lr *( x - w )
    return w_new
    
def main():

    inputvector = [[0.2,0.4],[0.3,0.5],[0,1]]
    weights = [[0.5,0.1,0.1,0.6,0.9],[0.2,0.4,0.4,0.9,0.1]]
    

    lr = 0.2
    epoch = 0
    while(epoch < 5):
        print("\n\nEpoch no:",epoch)
        for t in range(len(inputvector)):
            in_vector = inputvector[t]
        #print("\n\nEpoch no:",epoch)
            dist = []
            for i in range(5):
                dist.append(distance(in_vector[0], weights[0][i], in_vector[1] ,  weights[1][i]))
            print("distance:",np.round(dist,3))
            wc = dist.index(min(dist))
            print("the winning is ",wc)
            for j in range(2):
                weights[j][wc] = weight_updation(weights[j][wc], lr,in_vector[j] )
        
            print("New Weights:",np.round((weights),3))
        epoch = epoch + 1
    
        
main()
