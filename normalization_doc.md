## Image Analysis
----------
**Normalization**
 * Program Name: normalize_tif.py
 * Overview:
 
    Normalize the surface using the 100 grayscale cards
    
    ```Input```: 32 bit TIFF images
    
        - format (n: number)
            1. n_square.tif: testing surface
            2. n_left.tif: left half of the grayscale cards
            3. n_right.tif: right half of the grayscale cards
             
    ```Output```: normalized greyscale value of each surface
        0: all black; 100: all white
 * Instruction: 
 
        Put the test_images in the same folder
        (currently running over ten test images)
        Add more images following the input format and update the n_file variables in the program
        Debugging: print and imshow for debuggin
        
* Normalization Algorithm Overview:
    
        The grayscale value is normalized over the set of 100 cards. 
            Top left of the left half = 100 
            Right bottom  = 0

        Perform a linear fit and normalize the surface with the linear function

        Variance is calculated using numpy.var(arr).
    
    ![plot](https://github.com/cniii/Passive-Sampler/blob/master/normalize_sample_plot.png)
   
    - green dots represents the grayscale card value distribution
    - blue line: linear fit using the grayscale crad
    - red dot: normalized value of the surface
* Sample Output:
```
    Before normalized:[ 54273.42140471  54058.35790876  53742.35974447 54213.20244741 54095.79387108  54237.24743609  54200.52404824 54086.53051569 54327.61574371  54288.37671013]
    before variance: 26156.8288344
    After normalized:[ 87.30039135  87.88139563  87.85408988  87.47142909 87.24704568 87.21176816  86.55381496  87.76954148  87.07606351  86.98609516]
    after variance: 0.159859399264
```
