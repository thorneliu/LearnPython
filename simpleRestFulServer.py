#!/usr/bin/env python
import web

urls = (
        '/clusters', 'allClusters',
        '/clusters/(.*)', 'oneCluster'
        )

app = web.application(urls, globals())

class cluster:
    def __init__(self, clusterId, healthStatus, vrrpState):
        self.clusterId = clusterId
        self.healthStatus = healthStatus
        self.vrrpState = vrrpState

    def __str__(self):
        return 'id: %d, status: %s, role: %s' % (self.clusterId, self.healthStatus, self.vrrpState)

    def setHealthStatus(self, healthStatus):
        self.healthStatus = healthStatus

    def setVrrpState(self, vrrpState):
        self.vrrpState = vrrpState

cluster1 = cluster(1, "Healthy",   "MASTER")
cluster2 = cluster(2, "Unhealthy", "BACKUP") 

clusterList = [cluster1, cluster2]

class allClusters:        
    def GET(self):
        output = 'clusters:\n';
        for item in clusterList:
            print item
            output += str(item) + '\n'
        return output

class oneCluster:
    def GET(self, cluster):
        for item in clusterList:
            if str(item.clusterId) == str(cluster):
                return item

    def POST(self, cluster):
        newRole = web.data()
        print 'clusterId: ' + str(cluster) + ' notified role :' + newRole
        for item in clusterList:
            if str(item.clusterId) == str(cluster):
                item.setVrrpState(newRole)

if __name__ == "__main__":
    app.run()
