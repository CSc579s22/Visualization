The topology is shown below.

![topo](./topo.png)

The setting is similar to [1.baseline](../1.baseline/README.md), but we limit the bandwidth between `sw-r->sw3->sw3-cache1`.

As shown in [1.baseline](../1.baseline/README.md), the physical bandwidth is around `95.4 Mbits/sec`. 

The highest bitrate for BigBuckBunny used is `3.9Mbps`. As there are 4 client, we limit the bandwidth between `sw-r->sw3->sw3-cache1` to 10Mbps.

In theory, there should be competition and more quality switch now.

The speed limit is set using the following command:

Login to sw3, find the corresponding ovs port for sw3-cache1, which is `eth3`. The mapping can be obtained here: https://github.com/CSc579s22/Main/blob/master/server/config.py#L43
```bash
sudo ovs-vsctl set port eth3 qos=@qoseth3 -- --id=@qoseth3 create qos type=linux-htb other-config:max-rate=2000000
```
More info here: https://csc579s22.wordpress.com/2022/03/21/openflow-qos/

Verify:
```bash
clarkzjw@sw-r-c1:~$ iperf3 -c 10.10.10.18
Connecting to host 10.10.10.18, port 5201
[  4] local 10.10.10.22 port 34806 connected to 10.10.10.18 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec   830 KBytes  6.80 Mbits/sec    0    100 KBytes
[  4]   1.00-2.00   sec   255 KBytes  2.09 Mbits/sec    0    112 KBytes
[  4]   2.00-3.00   sec   318 KBytes  2.61 Mbits/sec    0    123 KBytes
[  4]   3.00-4.00   sec   318 KBytes  2.61 Mbits/sec    0    136 KBytes
[  4]   4.00-5.00   sec   255 KBytes  2.08 Mbits/sec    0    147 KBytes
[  4]   5.00-6.00   sec   382 KBytes  3.13 Mbits/sec    0    170 KBytes
[  4]   6.00-7.00   sec   509 KBytes  4.17 Mbits/sec    0    214 KBytes
[  4]   7.00-8.00   sec   509 KBytes  4.17 Mbits/sec    0    274 KBytes
[  4]   8.00-9.00   sec   700 KBytes  5.73 Mbits/sec    0    352 KBytes
[  4]   9.00-10.00  sec   764 KBytes  6.25 Mbits/sec    0    448 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  4.73 MBytes  3.96 Mbits/sec    0             sender
[  4]   0.00-10.00  sec  2.72 MBytes  2.28 Mbits/sec                  receiver

iperf Done.
```

As the iperf3 results shown, the max bandwidth between `sw-r-c1` to `sw3-cache1` is limited to around 10Mbps.

Now run the experiment again.
