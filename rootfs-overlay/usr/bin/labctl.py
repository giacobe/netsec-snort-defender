#!/usr/bin/env python3
import os,socket,sys
sys.path.insert(0,"/usr/lib/snort-lab")
from scenario import identity
def send(message):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1); sock.sendto(message.encode(),("10.0.0.255",9999)); sock.close()
email,date,code=identity()
if len(sys.argv)==1 or sys.argv[1]=="status":
    print("Email: %s\nExercise code: %s\nDate: %s"%(email,code,date.isoformat())); print("Use: labctl stage 1|2|3")
elif len(sys.argv)==3 and sys.argv[1]=="stage" and sys.argv[2] in ("1","2","3"):
    send("STAGE|"+sys.argv[2]); open("/var/lib/snort-lab/stage","w").write(sys.argv[2]+"\n"); print("Stage %s traffic started."%sys.argv[2])
else:
    print("Usage: labctl [status | stage 1|2|3]",file=sys.stderr); raise SystemExit(2)
