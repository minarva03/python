matrix1=[[[10,20,30],[40,50,60],[70,80,90]],[[100,200,300],[400,500,600],[700,800,900]]]
matrix2=[[[10,20,30],[40,50,60],[70,80,90]],[[101,200,300],[400,500,600],[777,800,900]]]
matrices=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
for i in range(2):
    for j in range(3):
        for k in range(3):
          matrices[i][j][k]=matrix1[i][j][k]+matrix2[i][j][k]
          print( matrices[i][j][k])
            