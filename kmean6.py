import random
import math

NUM_CLUSTERS =2
TOTAL_DATA = 5

#step to get dynamic input of clusters fro user
#p=0
#i=0
#sample_point=[]
#div=math.ceil(TOTAL_DATA/NUM_CLUSTERS)
#print(div)
#while(p<TOTAL_DATA):
# sample_point.append(p)
# p=p+div
# print(sample_point[i])
# i=i+1


LOWEST_SAMPLE_POINT = 0 #element 0 of SAMPLES.
HIGHEST_SAMPLE_POINT = 3 #element 3 of SAMPLES.
BIG_NUMBER = math.pow(10, 10)

#SAMPLES = [[0.1,0.4,0.2], [0.6,0.1,0.5], [0.4,1.6,0.9], [1.2,3.4,6.5], [9.2,9.6,8.6]]

def ReadData(fileName):
    #Read the file, splitting by lines
    f = open(fileName,'r');
    lines = f.read().splitlines();
    f.close();

    items = [];

    for i in range(0,len(lines)):
        line = lines[i].split(' ');
        itemFeatures = [];

        for j in range(len(line)):
            v = float(line[j]); #Convert feature value to float
            itemFeatures.append(v); #Add feature value to dict
    
        items.append(itemFeatures);
    return items;

SAMPLES = ReadData('data1.txt');
print("samples : ",SAMPLES)
data = []
centroids = []
meancent = []

class DataPoint:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
    def set_z(self, z):
        self.z = z
    
    def get_z(self):
        return self.z
    
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    
    def get_cluster(self):
        return self.clusterNumber

class Centroid:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
    def set_z(self, z):
        self.z = z
    
    def get_z(self):
        return self.z
    
def initialize_centroids():
    # Set the centoid coordinates to match the data points furthest from each other.
   
    # In this example, (1.0, 1.0) and (5.0, 7.0)
    centroids.append(Centroid(SAMPLES[LOWEST_SAMPLE_POINT][0], SAMPLES[LOWEST_SAMPLE_POINT][1],SAMPLES[LOWEST_SAMPLE_POINT][2]))
    centroids.append(Centroid(SAMPLES[HIGHEST_SAMPLE_POINT][0], SAMPLES[HIGHEST_SAMPLE_POINT][1],SAMPLES[HIGHEST_SAMPLE_POINT][2]))
    
    print("Centroids initialized at:")
    print("(", centroids[0].get_x(), ", ", centroids[0].get_y(),", ", centroids[0].get_z(), ")")
    print("(", centroids[1].get_x(), ", ", centroids[1].get_y(), ", ", centroids[1].get_z(),")")
    print()
    return

def initialize_datapoints():
    # DataPoint objects' x and y values are taken from the SAMPLE array.
    # The DataPoints associated with LOWEST_SAMPLE_POINT and HIGHEST_SAMPLE_POINT are initially
    # assigned to the clusters matching the LOWEST_SAMPLE_POINT and HIGHEST_SAMPLE_POINT centroids.
    for i in range(TOTAL_DATA):
        newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1],SAMPLES[i][2])
        
        if(i == LOWEST_SAMPLE_POINT):
            newPoint.set_cluster(0)
        elif(i == HIGHEST_SAMPLE_POINT):
            newPoint.set_cluster(1)
        else:
            newPoint.set_cluster(None)
            
        data.append(newPoint)
    
    return

def get_distance(dataPointX, dataPointY,dataPointZ, centroidX, centroidY, centroidZ,):
    # Calculate Euclidean distance.
   return math.sqrt(math.pow((centroidZ - dataPointZ), 2) +math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))
    
    
    
    
def recalculate_centroids():
    totalX = 0
    totalY = 0
    totalZ = 0
    totalInCluster = 0
    
    for j in range(NUM_CLUSTERS):
        for k in range(len(data)):
            if(data[k].get_cluster() == j):
                totalX += data[k].get_x()
                totalY += data[k].get_y()
                totalZ += data[k].get_z()
                
                totalInCluster += 1
                
        
        if(totalInCluster > 0):
            centroids[j].set_x(totalX / totalInCluster)
            centroids[j].set_y(totalY / totalInCluster)
            centroids[j].set_z(totalZ / totalInCluster)
        
    return

def update_clusters():
    isStillMoving = 0
    
    for i in range(TOTAL_DATA):
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        
        for j in range(NUM_CLUSTERS):
            distance = get_distance(data[i].get_x(), data[i].get_y(),data[i].get_z(), centroids[j].get_x(), centroids[j].get_y(), centroids[j].get_z())
            if(distance < bestMinimum):
                bestMinimum = distance
               
                currentCluster = j
        
     #   x.append(data[j].get_x())
     #   y.append(data[j].get_y())
     #   z.append(data[j].get_z())
        
        data[i].set_cluster(currentCluster)
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
            data[i].set_cluster(currentCluster)
            isStillMoving = 1
      
     #   print("print : ", x[i],y[i],z[i])
    
    return isStillMoving

def perform_kmeans():
    isStillMoving = 1
    
    initialize_centroids()
    
    initialize_datapoints()
    
    while(isStillMoving):
        recalculate_centroids()
        isStillMoving = update_clusters()
    
    return
    

def print_results():
    sumx=0
    sumy=0
    sumz=0
    c=0
    clustcentx=0
    clustcenty=0
    clustcentz=0
    for i in range(NUM_CLUSTERS):
        print("Cluster ", i, " includes:")
        for j in range(TOTAL_DATA):
            if(data[j].get_cluster() == i):
                print("(", data[j].get_x(), ", ", data[j].get_y(),", ", data[j].get_z(), ")")
                sumx= sumx +data[j].get_x()
                sumy= sumy +data[j].get_y()
                sumz= sumz +data[j].get_z()
                c=c+1
        clustcentx=sumx/c
        clustcenty=sumy/c
        clustcentz=sumz/c
        c=0  

        print("Cluster centroids : ",clustcentx," ",clustcenty," ",clustcentz)   
        print()
    
    return

perform_kmeans()
print_results()