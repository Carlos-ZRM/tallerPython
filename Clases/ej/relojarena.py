def hourglassSum(arr):
    i = 0
    j = 0 
    m_max = 0 
    while i < 4 :
        j = 0
        while j < 4 :
            print(i,":",j)
            hg = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            hg += arr[i+1][j+1]
            hg += arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            print(hg)
            if hg > m_max:
                m_max = hg
            j = j +1
        i = i + 1 
    return m_max

   static int hourglassSum(int[][] arr) {
    int hg = 0 ;
    int m = 0 ; 
    for (int i = 0; i < 4; i ++)
    {   
        
        for (int j = 0 ; j < 4 ; j ++)
        {
            hg =  arr[i][j]+arr[i][j+1]+arr[i][j+2];
            hg = hg +  arr[i+1][j+1]; 
            hg = hg + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
            if (hg > m )
            {
                m = hg ;
            }
        }
    }
    return m ; 
    }