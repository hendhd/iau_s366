#!/usr/bin/ python3
# -*- coding=utf-8 -*- 

# A demo program to show as simple Cone Search

import pyvo

service=pyvo.dal.SCSService("http://vo.km3net.de/ant20_01/nu/cone/scs.xml?")
neutrinos=service.search(pos=(43,35), radius=20)

print neutrinos

