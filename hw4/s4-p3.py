#!/usr/bin/python2
from mininet import net, cli

def main():
    mn = net.Mininet()

    # Add a switch and controller
    s1 = mn.addSwitch('s1')
    s1.cmd("sysctl net.ipv6.conf.all.disable_ipv6=1")
    c0 = mn.addController('c0')

    # Add hosts h1 - h3
    h1 = mn.addHost('h1')
    h2 = mn.addHost('h2')
    h3 = mn.addHost('h3')

    # add the links
    mn.addLink(h1, s1)
    mn.addLink(h2, s1)
    mn.addLink(h3, s1)

    # we assign /8 prefixes to h1 and h3
    h1.cmd('ifconfig h1-eth0 inet6 add 2001:638:709:a:1::/8')
    h3.cmd('ifconfig h3-eth0 inet6 add 2001:638:709:b:1::/8')

    # we give h2 the bigger /64 prefixes
    h2.cmd('sysctl -w net.ipv6.conf.all.forwarding=1')
    h2.cmd('ifconfig h2-eth0 inet6 add 2001:638:709:a::/64')
    h2.cmd('ifconfig h2-eth0 inet6 add 2001:638:709:b::/64')

    # START the network
    mn.start()

    # PING TESTS

    print('h1 ping h2')
    print(h1.cmd('ping6 -c5 2001:638:709:a::'))
    print('h1 ping h3')
    print(h1.cmd('ping6 -c5 2001:638:709:b:1::'))


    print('h2 ping h1')
    print(h2.cmd('ping6 -c5 2001:638:709:a:1::'))
    print('h2 ping h3')
    print(h2.cmd('ping6 -c5 2001:638:709:b:1::'))


    print('h3 ping h1')
    print(h3.cmd('ping6 -c5 2001:638:709:a:1::'))
    print('h3 ping h2')
    print(h3.cmd('ping6 -c5 2001:638:709:b::'))


    # and clean up
    mn.stop()

if __name__ == '__main__':
    main()
