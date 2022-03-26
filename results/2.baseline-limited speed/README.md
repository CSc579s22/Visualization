The topology is shown below.

![topo](./topo.png)

The setting is similar to [1.baseline](../1.baseline/README.md), but we limit the bandwidth between `sw-r->sw3->sw3-cache1`.

As shown in [1.baseline](../1.baseline/README.md), the physical bandwidth is around `95.4 Mbits/sec`. 

The highest bitrate for BigBuckBunny used is `3.9Mbps`. We are going to limit the total bandwidth between `sw-r->sw3->sw3-cache1` to 2Mbps.

In theory, there should be competition and more quality switch now.

The speed limit is set using the following command:

Login to sw3, find the corresponding ovs port for sw3-cache1, which is `eth3`. The mapping can be obtained here: https://github.com/CSc579s22/Main/blob/master/server/config.py#L43
```bash
sudo ovs-vsctl set port eth3 qos=@qoseth3 -- --id=@qoseth3 create qos type=linux-htb other-config:max-rate=2000000
```
More info here: https://csc579s22.wordpress.com/2022/03/21/openflow-qos/

Verify:
```bash
clarkzjw@sw3c1:~$ iperf3 -c 10.10.10.18
Connecting to host 10.10.10.18, port 5201
[  4] local 10.10.10.20 port 59584 connected to 10.10.10.18 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec   833 KBytes  6.82 Mbits/sec    0   97.6 KBytes
[  4]   1.00-2.00   sec   255 KBytes  2.09 Mbits/sec    0    109 KBytes
[  4]   2.00-3.00   sec   318 KBytes  2.61 Mbits/sec    0    120 KBytes
[  4]   3.00-4.00   sec   255 KBytes  2.08 Mbits/sec    0    133 KBytes
[  4]   4.00-5.00   sec   318 KBytes  2.61 Mbits/sec    0    144 KBytes
[  4]   5.00-6.00   sec   382 KBytes  3.13 Mbits/sec    0    167 KBytes
[  4]   6.00-7.00   sec   445 KBytes  3.65 Mbits/sec    0    212 KBytes
[  4]   7.00-8.00   sec   573 KBytes  4.69 Mbits/sec    0    273 KBytes
[  4]   8.00-9.00   sec   636 KBytes  5.21 Mbits/sec    0    351 KBytes
[  4]   9.00-10.00  sec   827 KBytes  6.78 Mbits/sec    0    447 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  4.73 MBytes  3.97 Mbits/sec    0             sender
[  4]   0.00-10.00  sec  2.72 MBytes  2.28 Mbits/sec                  receiver

iperf Done.
```

As the iperf3 results shown, the max bandwidth between `sw-r-c1` to `sw3-cache1` is limited to around 2Mbps.

Now run the experiment again.
