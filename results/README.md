# 1Mbps
ovs-vsctl set port eth1 qos=@qoseth1 -- --id=@qoseth1 create qos type=linux-htb other-config:max-rate=1000000

# 200kbps
sudo ovs-vsctl set interface eth2 ingress_policing_rate=2000
ovs-vsctl set port eth2 qos=@qoseth2 -- --id=@qoseth2 create qos type=linux-htb other-config:max-rate=200000

link speed before speed limit between sw1c1 and sw1cache1
```txt
clarkzjw@sw1c1:~$ iperf3 -c 10.10.10.8
Connecting to host 10.10.10.8, port 5201
[  4] local 10.10.10.10 port 57588 connected to 10.10.10.8 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec  13.9 MBytes   117 Mbits/sec  166   90.5 KBytes
[  4]   1.00-2.00   sec  11.4 MBytes  95.9 Mbits/sec    0    161 KBytes
[  4]   2.00-3.00   sec  11.4 MBytes  95.4 Mbits/sec    0    209 KBytes
[  4]   3.00-4.00   sec  11.4 MBytes  95.9 Mbits/sec    0    247 KBytes
[  4]   4.00-5.00   sec  11.4 MBytes  95.4 Mbits/sec    0    281 KBytes
[  4]   5.00-6.00   sec  11.4 MBytes  95.4 Mbits/sec    0    311 KBytes
[  4]   6.00-7.00   sec  11.4 MBytes  95.9 Mbits/sec    0    338 KBytes
[  4]   7.00-8.00   sec  11.4 MBytes  95.4 Mbits/sec    0    363 KBytes
[  4]   8.00-9.00   sec  11.4 MBytes  95.9 Mbits/sec    0    387 KBytes
[  4]   9.00-10.00  sec  11.4 MBytes  95.4 Mbits/sec    0    409 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec   117 MBytes  97.7 Mbits/sec  166             sender
[  4]   0.00-10.00  sec   114 MBytes  96.0 Mbits/sec                  receiver

iperf Done.
```