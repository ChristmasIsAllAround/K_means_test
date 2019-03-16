import pandas as pd
import matplotlib.pyplot  as plt
from load_data import *


class KMeansCluster():
    def __init__(self, K=3,dimension=2):
        self.K = K
        self.summary=[]
        self.dimension=dimesion

    def cluster(self, data=None, K=None, MaxIretation=100):
        if data is not None:
            self.data = data
        if K is not None:
            self.K = K

        centers = [self.data[i] for i in np.random.randint(0, len(self.data), self.K)]

        distances = [[EuDis(centers[j], self.data[i]) for j in range(self.K)] for i in range(len(self.data))]
        newLabel = [distances[i].index(min(distances[i])) for i in range(len(self.data))]


        oldLabel = [44] * len(self.data)
        iretation = 0
        while not labelEqual(newLabel, oldLabel):
            oldLabel = newLabel
            classNumbers = [0] * self.K
            classSum = [[0] * self.dimension for i in range(self.K)]
            for i in range(len(self.data)):
                for j in range(self.K):
                    if newLabel[i] == j:
                        classNumbers[j] += 1
                        for v in range(self.dimension):
                            classSum[j][v] += self.data[i][v]
                        break
            for i in range(self.K):
                for j in range(self.dimension):
                    if classNumbers[i] != 0:
                        centers[i][j] = classSum[i][j] / classNumbers[i]
            iretation += 1
            if iretation > MaxIretation:
                break
            self.iretation = iretation

            distances = [[EuDis(centers[j], self.data[i]) for j in range(self.K)] for i in range(len(self.data))]
            newLabel = [distances[i].index(min(distances[i])) for i in range(len(self.data))]

        minDistances=[min(l) for l in distances]
        delMinDistances=distances
        for l in delMinDistances:
            l.remove(min(l))
        secondMinDistances = [min(l) for l in delMinDistances]
        self.label = newLabel
        self.centers = centers
        self.clusterRate=sum([minDistances[i]/(secondMinDistances[i]+minDistances[i])
                              for i in range(len(minDistances))])/len(minDistances)
        self.summary.append({"K": self.K, "ClusterRate": self.clusterRate, "Iretation":iretation})
        print("K is : ", self.K , "Cluster rate : ", self.clusterRate)
        print('')

    def resultPlot(self, data=None, K=None):
        if data is not None:
            self.data = data
        if K is not None:
            self.K = K
        if data is not None or K is not None:
            self.cluster(K=K)
        colors = ['b', 'g', 'y', 'r', 'k', 'c', 'm', 'w']
        groupPoints = [[], [], [], [], [], [], []]
        if len(self.data[0]) != 2:
            print("2D data is required for the plot! ")
            return None
        if self.K > 7:
            print("The K is too large!")
            return None
        for i in range(len(self.data)):
            groupPoints[self.label[i]].append(self.data[i])
        for j in range(self.K):
            plt.scatter(np.array(groupPoints[j])[:, 0], np.array(groupPoints[j])[:, 1], c=colors[j])
        plt.scatter(np.array(self.centers)[:, 0], np.array(self.centers)[:, 1],
                    s=np.ones((self.K)) * 100, marker='p', c=colors[-1])
        plt.show()

    def selectKfromSummary(self):
        df = pd.DataFrame(self.summary)
        self.K=df["K"][df['ClusterRate'].argmin()]
        print("The best K value for cluster rate in the summary is : ", self.K)

if __name__ == '__main__':
    x = randData()
    KMCmodel = KMeansCluster()
    KMCmodel.cluster(data=x)
    KMCmodel.resultPlot()
    KMCmodel.resultPlot(K=4)
    KMCmodel.resultPlot(K=5)
    KMCmodel.resultPlot(K=6)
    KMCmodel.selectKfromSummary()
