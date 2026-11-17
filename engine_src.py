import json,os,random,sys,urllib.request,urllib.error
E=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no env")
V=[0,100,320,330,500,900,0]
KN=[33,31,18,14,-14,-18,-31,-33]
KI=[1,-1,16,-16,15,17,-15,-17]
BI=[15,17,-15,-17]
RI=[1,-1,16,-16]
QU=BI+RI
KEEP=[15]*128
for s,v in ((0,13),(7,14),(4,12),(112,7),(119,11),(116,3)):KEEP[s]=v
PS=[[0]*128 for _ in range(7)]
KM=[0]*64;KE=[0]*64
AD=[0,3,6,12,20,32,50,0]
for r in range(8):
 for f in range(8):
  q=r*16+f;c=min(f,7-f)+min(r,7-r);i=r*8+f
  PS[1][q]=AD[r]+(4 if f in(3,4) and 1<r<6 else 0)
  PS[2][q]=5*c-12
  PS[3][q]=3*c-6
  PS[4][q]=(15 if r==6 else 0)+(5 if r==0 and f in(3,4) else 0)
  PS[5][q]=2*c-8
  KM[i]=[20,25,10,0,0,10,25,20][f] if r==0 else max(-50,-15*r)
  KE[i]=8*c-24
R=random.Random(20261117)
Z=[R.getrandbits(64) for _ in range(1689)]
ZS=1688
INF=1000000;MATE=100000;MAXNP=6200
START="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
B=[0]*128;S=1;C=15;EP=-1;HM=0;H=0;EV=0;NP=0;MT=0;BW=0;BB=0;KW=4;KB=116;KV=0
U=[];REP=[];TT={};KIL=[[0,0] for _ in range(256)]
N=0;LIM=200000;LIMB=10**9;MC=0
class AB(Exception):pass
def pv(p,q):
 t=p if p>0 else -p
 v=V[t]+PS[t][q if p>0 else q^0x70]
 return v if p>0 else -v
def kvl():
 ph=NP if NP<MAXNP else MAXNP
 a=(KW>>4)*8+(KW&7);b=((KB^0x70)>>4)*8+(KB&7)
 return (KM[a]*ph+KE[a]*(MAXNP-ph))//MAXNP-(KM[b]*ph+KE[b]*(MAXNP-ph))//MAXNP
def atk(sq,by):
 b=B
 if by>0:
  for o in (sq-15,sq-17):
   if not(o&0x88) and b[o]==1:return 1
 else:
  for o in (sq+15,sq+17):
   if not(o&0x88) and b[o]==-1:return 1
 for d in KN:
  o=sq+d
  if not(o&0x88) and b[o]==2*by:return 1
 for d in KI:
  o=sq+d
  if not(o&0x88) and b[o]==6*by:return 1
 for d in BI:
  o=sq+d
  while not(o&0x88):
   q=b[o]
   if q:
    if q==3*by or q==5*by:return 1
    break
   o+=d
 for d in RI:
  o=sq+d
  while not(o&0x88):
   q=b[o]
   if q:
    if q==4*by or q==5*by:return 1
    break
   o+=d
 return 0
def gen():
 ms=[];b=B;s=S
 for q in range(128):
  if q&0x88:continue
  p=b[q]
  if not p or (p>0)!=(s>0):continue
  t=p if p>0 else -p
  if t==1:
   d=16 if s>0 else -16
   o=q+d
   if not(o&0x88) and not b[o]:
    r=q>>4
    if (s>0 and r==6) or (s<0 and r==1):
     for pr in (5,4,3,2):ms.append(q|(o<<7)|(pr<<14))
    else:
     ms.append(q|(o<<7))
     if ((s>0 and r==1) or (s<0 and r==6)) and not b[o+d]:ms.append(q|((o+d)<<7))
   for o in (q+d-1,q+d+1):
    if o&0x88:continue
    v=b[o]
    if v and (v>0)!=(s>0):
     r=q>>4
     if (s>0 and r==6) or (s<0 and r==1):
      for pr in (5,4,3,2):ms.append(q|(o<<7)|(pr<<14))
     else:ms.append(q|(o<<7))
    elif o==EP:ms.append(q|(o<<7))
  elif t==2 or t==6:
   for d in (KN if t==2 else KI):
    o=q+d
    if o&0x88:continue
    v=b[o]
    if not v or (v>0)!=(s>0):ms.append(q|(o<<7))
  else:
   ds=BI if t==3 else RI if t==4 else QU
   for d in ds:
    o=q+d
    while not(o&0x88):
     v=b[o]
     if v:
      if (v>0)!=(s>0):ms.append(q|(o<<7))
      break
     ms.append(q|(o<<7));o+=d
 if s>0:
  if C&1 and not B[5] and not B[6] and B[7]==4 and B[4]==6 and not atk(4,-1) and not atk(5,-1) and not atk(6,-1):ms.append(4|(6<<7))
  if C&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and B[4]==6 and not atk(4,-1) and not atk(3,-1) and not atk(2,-1):ms.append(4|(2<<7))
 else:
  if C&4 and not B[117] and not B[118] and B[119]==-4 and B[116]==-6 and not atk(116,1) and not atk(117,1) and not atk(118,1):ms.append(116|(118<<7))
  if C&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and B[116]==-6 and not atk(116,1) and not atk(115,1) and not atk(114,1):ms.append(116|(114<<7))
 return ms
def make(m):
 global S,C,EP,HM,H,EV,NP,MT,BW,BB,KW,KB,KV
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 p=B[f]
 if abs(p)==1 and t==EP and not B[t]:
  cs=t-16 if S>0 else t+16;cap=B[cs]
 else:
  cs=t;cap=B[t]
 rf=-1;rt=0
 if abs(p)==6 and abs(t-f)==2:
  if t>f:rf=f+3;rt=f+1
  else:rf=f-4;rt=f-1
 U.append((m,cap,cs,C,EP,HM,H,EV,NP,MT,BW,BB,KW,KB,KV))
 H^=Z[ZS]
 if EP>=0:H^=Z[1680+(EP&7)]
 oc=C;C&=KEEP[f]&KEEP[t]
 if C!=oc:
  if oc:H^=Z[1664+oc]
  if C:H^=Z[1664+C]
 H^=Z[(p+6)*128+f]
 B[f]=0
 if pr:
  np=pr*S
  H^=Z[(np+6)*128+t];B[t]=np
  EV-=pv(p,f);EV+=pv(np,t)
  NP+=V[pr];MT+=V[pr]-100
  if pr==3:
   if S>0:BW+=1
   else:BB+=1
 else:
  H^=Z[(p+6)*128+t];B[t]=p
  EV-=pv(p,f);EV+=pv(p,t)
 if abs(p)==6:
  if S>0:KW=t
  else:KB=t
 if cap:
  if cs!=t:B[cs]=0
  H^=Z[(cap+6)*128+cs]
  EV-=pv(cap,cs)
  MT-=V[abs(cap)]
  if abs(cap)!=1:
   NP-=V[abs(cap)]
   if abs(cap)==3:
    if S>0:BB-=1
    else:BW-=1
 if rf>=0:
  r=B[rf];B[rf]=0;B[rt]=r
  H^=Z[(r+6)*128+rf]^Z[(r+6)*128+rt]
  EV-=pv(r,rf);EV+=pv(r,rt)
 if abs(p)==1 and abs(t-f)==32:
  EP=f+16 if S>0 else f-16
  H^=Z[1680+(EP&7)]
 else:EP=-1
 HM=0 if abs(p)==1 or cap else HM+1
 S=-S
 if abs(p)==6 or NP!=U[-1][8]:KV=kvl()
 if S>0:
  if atk(KB,1):unmake();return 0
 else:
  if atk(KW,-1):unmake();return 0
 return 1
def unmake():
 global S,C,EP,HM,H,EV,NP,MT,BW,BB,KW,KB,KV
 m,cap,cs,oc,oep,ohm,oh,oev,onp,omt,obw,obb,okw,okb,okv=U.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 S=-S
 p=B[t]
 B[f]=S if pr else p
 if cap and cs==t:B[t]=cap
 else:B[t]=0
 if cap and cs!=t:B[cs]=cap
 if abs(p)==6 and abs(t-f)==2:
  if t>f:B[f+3]=B[f+1];B[f+1]=0
  else:B[f-4]=B[f-1];B[f-1]=0
 C=oc;EP=oep;HM=ohm;H=oh;EV=oev;NP=onp;MT=omt;BW=obw;BB=obb;KW=okw;KB=okb;KV=okv
def evl():
 if MT==0:return 0
 s=EV+KV+(30 if BW>1 else 0)-(30 if BB>1 else 0)
 return s+10 if S>0 else -s+10
def order(ms,ply,ttm):
 sc=[]
 for m in ms:
  f=m&127;t=(m>>7)&127;pr=(m>>14)&7
  s=0
  if m==ttm:s=100000
  elif pr:s=20000+V[pr]
  else:
   c=B[t]
   if c:s=10000+10*V[abs(c)]-V[abs(B[f])]
   elif EP>=0 and t==EP and abs(B[f])==1:s=10900
   elif m==KIL[ply][0]:s=5000
   elif m==KIL[ply][1]:s=4000
  sc.append((s,m))
 sc.sort(reverse=True)
 ms[:]=[m for _,m in sc]
def qs(a,b,ply):
 global N
 N+=1
 if N>=LIMB:raise AB
 if ply>200:return evl()
 if HM>=100:return 0
 ck=atk(KW if S>0 else KB,-S)
 if ck:
  ms=gen();st=-MATE-1
 else:
  st=evl()
  if st>=b:return st
  if st>a:a=st
  ms=[m for m in gen() if B[(m>>7)&127] or (m>>14) or (EP>=0 and (m>>7)&127==EP and abs(B[m&127])==1)]
 order(ms,ply,0)
 best=st;legal=0
 for m in ms:
  if not ck:
   t=(m>>7)&127;pr=(m>>14)&7;c=B[t];v=0
   if c:v=V[abs(c)]
   elif EP>=0 and t==EP and abs(B[m&127])==1:v=100
   if pr:v+=V[pr]-100
   if st+v+150<a:continue
  if not make(m):continue
  legal+=1
  s=-qs(-b,-a,ply+1)
  unmake()
  if s>best:best=s
  if s>a:a=s
  if a>=b:return a
 if ck and legal==0:return -MATE+ply
 return best
def srch(d,a,b,ply):
 global N,S,H,EP,HM
 N+=1
 if N>=LIMB:raise AB
 if ply>0:
  if HM>=100:return 0
  _n=len(REP);_s=_n-1-HM
  if _s<0:_s=0
  for _i in range(_n-3,_s-1,-2):
   if REP[_i]==H:return 0
 if d<=0:return qs(a,b,ply)
 e=TT.get(H)
 ttm=0
 if e:
  ttm=e[3]
  if e[0]>=d:
   s=e[2]
   if s>MATE-200:s-=ply
   elif s<-(MATE-200):s+=ply
   if e[1]==1:return s
   if e[1]==2 and s>=b:return s
   if e[1]==3 and s<=a:return s
 if d>=3 and ply>0 and NP and not atk(KW if S>0 else KB,-S):
  oe=EP;oh=HM
  if EP>=0:H^=Z[1680+(EP&7)]
  EP=-1;HM+=1;S=-S;H^=Z[ZS]
  REP.append(H)
  s=-srch(d-3,-b,-b+1,ply+1)
  REP.pop()
  S=-S;H^=Z[ZS];EP=oe;HM=oh
  if EP>=0:H^=Z[1680+(EP&7)]
  if s>=b:return s
 ms=gen();order(ms,ply,ttm)
 best=-MATE-1;bm=0;legal=0;a0=a
 for m in ms:
  f=m&127;t=(m>>7)&127
  cp=B[t]!=0 or (m>>14) or (EP>=0 and t==EP and abs(B[f])==1)
  if not make(m):continue
  legal+=1
  REP.append(H)
  s=-srch(d-1,-b,-a,ply+1)
  REP.pop()
  unmake()
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if not cp and KIL[ply][0]!=m:
    KIL[ply][1]=KIL[ply][0];KIL[ply][0]=m
   break
 if legal==0:
  return -MATE+ply if atk(KW if S>0 else KB,-S) else 0
 fl=3 if best<=a0 else 2 if best>=b else 1
 s=best
 if s>MATE-200:s+=ply
 elif s<-(MATE-200):s-=ply
 TT[H]=(d,fl,s,bm)
 return best
def bestmove():
 global LIMB,N
 ms=gen()
 legal=[]
 for m in ms:
  if make(m):legal.append(m);unmake()
 if len(legal)==1:return legal[0]
 sc={};best=legal[0];N=0
 for d in range(1,64):
  LIMB=10**9 if d==1 else LIM
  try:
   legal.sort(key=lambda m:-sc.get(m,0))
   a=-INF;bs=-INF;bm=best
   for m in legal:
    make(m);REP.append(H)
    s=-srch(d-1,-INF,-a,1)
    REP.pop();unmake()
    sc[m]=s
    if s>bs:bs=s;bm=m
    if s>a:a=s
   best=bm
   if abs(bs)>MATE-200:break
  except AB:
   break
 return best
def parse(fen):
 global B,S,C,EP,HM,H,EV,NP,MT,BW,BB,KW,KB,KV,U,REP
 B=[0]*128;U=[];REP=[]
 ps=fen.split()
 H=0;EV=0;NP=0;MT=0;BW=0;BB=0
 for r,row in enumerate(ps[0].split('/')):
  f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    sq=(7-r)*16+f
    p='pnbrqk'.index(ch.lower())+1
    if ch.islower():p=-p
    B[sq]=p
    H^=Z[(p+6)*128+sq]
    if abs(p)!=6:
     EV+=pv(p,sq);MT+=V[abs(p)]
     if abs(p)!=1:NP+=V[abs(p)]
     if abs(p)==3:
      if p>0:BW+=1
      else:BB+=1
    else:
     if p>0:KW=sq
     else:KB=sq
    f+=1
 S=1 if ps[1]=='w' else -1
 C=0
 for ch in ps[2]:
  if ch=='K':C|=1
  elif ch=='Q':C|=2
  elif ch=='k':C|=4
  elif ch=='q':C|=8
 if C:H^=Z[1664+C]
 EP=-1
 if ps[3]!='-':
  EP=(ord(ps[3][0])-97)+(int(ps[3][1])-1)*16
  H^=Z[1680+(EP&7)]
 HM=int(ps[4])
 if S<0:H^=Z[ZS]
 KV=kvl()
def uci(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 s='abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[t&7]+str((t>>4)+1)
 if pr:s+='nbrq'[pr-2]
 return s
def choose(fen,moves):
 global MC,LIM
 MC+=1
 LIM=200000-50000*min(3,MC//150)
 parse(fen);hf=H
 parse(START);REP=[H]
 ok=True
 for u in moves:
  f=(ord(u[0])-97)+(int(u[1])-1)*16;t=(ord(u[2])-97)+(int(u[3])-1)*16;pr=0
  if len(u)>4:pr='nbrq'.index(u[4])+2
  if not make(f|(t<<7)|(pr<<14)):ok=False;break
  REP.append(H)
 if not ok or H!=hf:
  parse(fen);REP=[H]
 return bestmove()
def post(p,b):
 req=urllib.request.Request(E+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 try:
  with urllib.request.urlopen(req) as r:return json.load(r)
 except urllib.error.HTTPError as e:
  return {'_err':e.code}
while True:
 g=post('/game',{})
 if g.get('status')=='done':break
 if '_err' in g:sys.exit(1)
 while g.get('status')=='your_move':
  m=choose(g['fen'],g.get('moves') or [])
  u=uci(m)
  legal=g.get('legal_moves') or []
  if u not in legal and legal:u=legal[0]
  h=post('/move',{'game':g['game'],'move':u})
  if '_err' in h:
   if legal and legal[0]!=u:h=post('/move',{'game':g['game'],'move':legal[0]})
   if '_err' in h:sys.exit(1)
  g=h
 print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
