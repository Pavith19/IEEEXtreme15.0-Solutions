import numpy as np

dic = {"#":1, '.':0, '?':0}
T = int(input())
for test in range(T):
    R, C = [int(x) for x in input().split()]
    
    image = []
    for row in range(R):
        image.append(input().split()[0])  
    # print(image) 
    image2 = np.zeros((R, C)) 
    for row in range(R):
        for c in range(C):
            image2[row,c] = dic[image[row][c]]
    print(image2)
    
    A, B = [int(x) for x in input().split()]
    pattern = []
    for row in range(A):
        pattern.append(input().split()[0]) 
    pattern2 = np.zeros((A, B)) 
    for row in range(A):
        for c in range(B):
            pattern2[row,c] = dic[pattern[row][c]]

    
    p = 0
    for row in range(0,(R-A+1)):
        for column in range(0,(C-B+1)):
            sumOfOverlap = np.sum(np.multiply(image2[row:row+A, column:column+B],pattern2))
            if sumOfOverlap == np.sum(pattern2):
                p+=1
    print("Answer: ", p)

