#!/usr/bin/env python3
"""
Reproduce the posterior SPARC confrontation of the regime-transition protocol.
Analysis date: 2026-07-09.  Pre-registered scale g_crit = 1.0e-11 m/s^2.

DATA (public, not redistributed here):
  - SPARC_Lelli2016c.mrt        (galaxy sample: L[3.6], MHI, Vflat, Q)
  - MassModels_Lelli2016c.mrt   (rotation-curve mass models: R, Vobs per point)
  Both from http://astroweb.cwru.edu/SPARC/  (Lelli, McGaugh & Schombert 2016).
Set the two paths below to your local copies.
"""
import numpy as np

T1 = "SPARC_Lelli2016c.mrt"           # <- set path
MM = "MassModels_Lelli2016c.mrt"      # <- set path

G=6.674e-11; Msun=1.989e30; km=1e3; kpc=3.0857e19
g_crit=1.0e-11          # PRE-REGISTERED (coherence-model, 2026-03-02)
a0=1.2e-10              # posterior: a0 = 4*pi*g_crit (RAR/McGaugh scale)
UPS=0.5                 # M/L at 3.6um (McGaugh & Schombert 2014)

# --- baryonic mass per galaxy (Q<=2) ---
gal={}
for ln in open(T1):
    p=ln.split()
    if len(p)<18: continue
    try: name=p[0]; L36=float(p[7]); MHI=float(p[13]); Q=int(p[17])
    except: continue
    if Q>=3: continue
    Mbar=(UPS*L36+1.33*MHI)*1e9*Msun
    if Mbar>0: gal[name]=Mbar

# --- rotation-curve profiles ---
prof={}
for ln in open(MM):
    p=ln.split()
    if len(p)<8: continue
    try: name=p[0]; R=float(p[2]); Vobs=float(p[3])
    except: continue
    if R>0 and Vobs>0: prof.setdefault(name,[]).append((R,Vobs))

def plateau(pts):
    """Longest consecutive window with velocity variation (max-min)/mean < 5%
       (NOT the last 3 points). Returns (V_flat mean, R_flat = last radius)."""
    V=[v for r,v in pts]; R=[r for r,v in pts]; n=len(pts); best=None
    for i in range(n):
        for j in range(i+1,n):
            w=V[i:j+1]
            if (max(w)-min(w))/np.mean(w)*100 < 5.0:
                L=j-i+1
                if best is None or L>best[0] or (L==best[0] and R[j]>best[1]):
                    best=(L,R[j],np.mean(w))
    return (best[2],best[1]) if best else None

rows=[]; ai_col=[]; ai_rest=[]
for name,Mbar in gal.items():
    if name not in prof: continue
    pl=plateau(sorted(prof[name]))
    if pl is None: continue
    Vf,Rf=pl
    a_impl=(Vf*km)**4/(G*Mbar)
    g_int=(Vf*km)**2/(Rf*kpc)
    if g_int<g_crit:   # COLLECTIVE
        RT=np.sqrt(G*Mbar/g_crit)/kpc
        Vpred=(G*Mbar*g_crit)**0.25/km
        err=abs(Vpred-Vf)/Vf*100; ratio=RT/Rf
        verd="CONFIRMS" if (err<=20 and 0.5<=ratio<=2.0) else ("FALSIFIES" if err>20 else "ratio-out")
        rows.append((name,Vf,Rf,g_int,RT,Vpred,err,ratio,verd)); ai_col.append(a_impl)
    else:
        ai_rest.append(a_impl)

print(f"g_crit={g_crit:.1e}  |  COLLECTIVE: {len(rows)}")
print(f"{'Galaxy':<11}{'Vflat':>6}{'Rflat':>6}{'g_int':>9}{'R_T':>6}{'Vpred':>6}{'err%':>6}{'ratio':>6}  verdict")
for n,Vf,Rf,gi,RT,Vp,er,ra,ve in sorted(rows,key=lambda r:r[6]):
    print(f"{n:<11}{Vf:>6.1f}{Rf:>6.2f}{gi:>9.1e}{RT:>6.2f}{Vp:>6.1f}{er:>6.1f}{ra:>6.2f}  {ve}")
c=sum(1 for r in rows if r[8]=='CONFIRMS')
print(f"\nCONFIRMS={c}/{len(rows)}  FALSIFIES={sum(1 for r in rows if r[8]=='FALSIFIES')}")
print(f"\nSelection-bias check  (a_impl = V^4/GM):")
print(f"  COLLECTIVE median a_impl = {np.median(ai_col):.2e} = {np.median(ai_col)/a0:.2f} a0")
print(f"  Rest       median a_impl = {np.median(ai_rest):.2e} = {np.median(ai_rest)/a0:.2f} a0")
