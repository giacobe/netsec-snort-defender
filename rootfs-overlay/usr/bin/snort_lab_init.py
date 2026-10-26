#!/usr/bin/env python3
import os, sys
sys.path.insert(0,"/usr/lib/snort-lab")
from scenario import identity, stage_values
email,date,code=identity(); values=stage_values(3)
os.makedirs("/var/lib/snort-lab",exist_ok=True); os.makedirs("/root/Desktop",exist_ok=True)
open("/var/lib/snort-lab/identity","w").write("%s\n%s\n%s\n"%(email,date.isoformat(),code))
marker=" ".join("%02X"%byte for byte in values["marker"])
open("/root/Desktop/threat-intel.txt","w").write("""POLYLAB THREAT INTELLIGENCE BULLETIN

Observed family: Night Lantern
Transport: UDP
Direction: external client to monitored server
Destination port: %d
Indicator location: within the first 32 payload bytes
Binary marker: %s

Create a local Snort rule that detects the complete byte sequence. Partial
matches are insufficient. Use a local SID of 1000003 and revision 1.
"""%(values["destination_port"],marker))
print("PolyLab exercise %s initialized for %s"%(code,email))
