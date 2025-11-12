# -*- coding: utf-8 -*-
from mininet.topo import Topo
from mininet.node import Host, OVSKernelSwitch

# Nouvelle classe de topologie MeshTopo
class MeshTopo(Topo):  # Topologie maillée

    def __init__(self):
        # Initialisation de la topologie
        Topo.__init__(self)

        # Création de 4 hotes avec des IP et des MAC specifiques
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', mac='10:00:00:00:00:01')
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', mac='10:00:00:00:00:02')
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', mac='10:00:00:00:00:03')
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', mac='10:00:00:00:00:04')

        # Création de 8 commutateurs (switches)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')

        # Liaison des hotes à deux des switches
        self.addLink(h1, s1, bw=10, delay='5ms')
        self.addLink(h2, s1, bw=10, delay='4ms')
        self.addLink(h3, s8, bw=10, delay='6ms')
        self.addLink(h4, s8, bw=10, delay='3ms')

        # Creation des liens mailles entre switches avec des debits et latences configures
        self.addLink(s1, s2, bw=10, delay='12ms')
        self.addLink(s1, s3, bw=10, delay='3ms')
        self.addLink(s1, s6, bw=10, delay='5ms')
        self.addLink(s2, s8, bw=10, delay='4ms')
        self.addLink(s3, s4, bw=10, delay='6ms')
        self.addLink(s4, s5, bw=10, delay='3ms')
        self.addLink(s5, s8, bw=10, delay='2ms')
        self.addLink(s6, s7, bw=10, delay='10ms')
        self.addLink(s7, s8, bw=10, delay='1ms')

# Declaration du nom de la topologie à utiliser avec Mininet (--topo mesh)
topos = { 'mesh': (lambda: MeshTopo()) }

