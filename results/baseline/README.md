The topology is shown below.

![topo](../topo.png)

In this experiment, `sw1-c{1,2,3,4}` start streaming at the same time. 
The nearest cache server for these clients is `cache1`. 

These four clients all stream from `cache1`.

The weight of each edge represents the maximum bandwidth of a given link. (Unit: Mbps)

The total bandwidth from `sw1-c{1,2,3,4}` exceeds the bandwidth between `sw1` and `cache1`.

So there will be competitions for best bitrate.

