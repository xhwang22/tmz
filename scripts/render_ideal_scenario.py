#!/usr/bin/env python3
"""Render author-requested ideal aggregates. Never generate claimed observations."""
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np
from render_c1_landscape import ROOT, WIDTH, HEIGHT, FAMILIES, INK, MUTED, GRID, ERA
from figure_fonts import FAMILY, configure
from matplotlib.colors import to_rgb

DATA=ROOT/"data/ideal_scenario"
D=json.loads((DATA/"scenario.json").read_text())
OUT=ROOT/"figures/ideal_scenario"
OUT.mkdir(exist_ok=True)
FILES=[]
def save(fig,name):
    for ext in ("pdf","svg","png"):
        p=OUT/f"{name}.{ext}"
        fig.savefig(p,dpi=300,metadata={"Creator":"IterEval SIMULATED IDEAL SCENARIO"} if ext=="pdf" else None)
        if ext == "svg":
            # Matplotlib leaves trailing spaces in path data; keep exports
            # diff-clean without changing SVG geometry or text.
            p.write_text("\n".join(line.rstrip() for line in p.read_text().splitlines()) + "\n")
        FILES.append(p)
    plt.close(fig)
def tex(name,rows):
    p=OUT/f"{name}.tex"
    p.write_text("% SIMULATED IDEAL SCENARIO; not experimental results.\n"+"\n".join(" & ".join(row)+r"\\" for row in rows)+"\n")
    FILES.append(p)

def tables():
    means=np.mean(D["pair"],axis=1)
    main=[]
    for i,m in enumerate(D["methods"]):
        prefix=r"\rowcolor{pEvoWash} " if m=="IterEval" else ""
        main.append([prefix+m,f"{means[i]:.1f}",f'{D["bon"][i]:.1f}',f'{D["reg"][i]:.3f}',f'{D["coverage"][i]:.1f}'])
    main.append([r"\midrule Eligible domains",*[str(len(D["design"]["domains"]))]*4])
    tex("main",main)
    tex("downstream",[[study,domain,*v[1:]] for study,domain,v in D["downstream"]])
    tex("search",D["searchRows"])
    tex("mining",D["miningRows"])
    tex("components",D["componentRows"])
    tex("downstream_detail",D["downstreamDetail"])
    per=[]
    for j,domain in enumerate(D["design"]["domains"]):
        cfg = D["design"]
        per.append([rf"\multicolumn{{6}}{{@{{}}l}}{{\textit{{{domain}; $N={cfg['N']}$, {cfg['groups_per_domain']} groups, {cfg['searches']} searches}}}}"])
        for i,m in enumerate(D["methods"]):
            offset=j-1.5
            per.append([m,f'{D["pair"][i][j]:.1f}',f'{D["top"][i]+offset:.1f}',
                        f'{D["bon"][i]+offset:.1f}',f'{D["reg"][i]-.005*offset:.3f}',"not assigned"])
        per.append([r"\addlinespace"])
    # Rows containing only spacing commands must not add another row delimiter.
    tex("domain",per)
    p=OUT/"domain.tex"
    rows = p.read_text().replace(r"\addlinespace\\",r"\addlinespace")
    p.write_text("\\newcommand{\\IdealDomainRows}{%\n" + rows + "}\n")
    tex("cost", D["resourceRows"])
    tex("annotation", D["annotationRows"])
    controls = [float(row[1]) for row in D["searchRows"]]
    mining = [float(row[4]) for row in D["miningRows"][:4]]
    c2 = [list(map(int, row[2][0].split("/"))) for row in D["downstream"] if row[0] == "C2"]
    c2_pref = 100 * sum(w + t/2 for w,t,l in c2) / sum(sum(row) for row in c2)
    values = {
        "ResultPair": f"{means[-1]:.1f}",
        "ResultSeedGain": f"{means[-1]-means[1]:.1f}",
        "ResultGepaGain": f"{means[-1]-means[4]:.1f}",
        "ResultDeployCost": f'{D["cost"][-1]/D["cost"][1]:.2f}',
        "ResultParentGain": f"{controls[3]-controls[2]:.1f}",
        "ResultDirectionGain": f"{controls[2]-controls[1]:.1f}",
        "ResultHistoryGain": f"{controls[1]-controls[0]:.1f}",
        "ResultInteraction": f"{(mining[3]-mining[2])-(mining[1]-mining[0]):.1f}",
        "ResultCtwoPreference": str(Decimal(str(c2_pref)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)),
        "ResultCthreePreference": next(row[2][1] for row in D["downstream"] if row[0] == "C3"),
    }
    p = OUT/"numbers.tex"
    p.write_text("% SIMULATED IDEAL SCENARIO; computed prose values, not observations.\n" +
                 "\n".join(r"\newcommand{\%s}{%s}" % item for item in values.items()) + "\n")
    FILES.append(p)

def setup():
    props=configure()
    plt.rcParams.update({"font.size":7,"axes.labelsize":7,"xtick.labelsize":6,"ytick.labelsize":6,
                         "axes.spines.top":False,"axes.spines.right":False})
    return props
def landscape():
    props=setup()
    fig=plt.figure(figsize=(WIDTH,HEIGHT),dpi=220,facecolor="white")
    ax=fig.add_axes([0,0,1,1],xlim=(0,WIDTH),ylim=(0,HEIGHT),aspect="equal")
    ax.set_axis_off()
    def text(x,y,value,size=7.3,role="body",**kwargs):
        prop=props[role].copy(); prop.set_size(size)
        return ax.text(x,y,value,fontproperties=prop,va="center",color=kwargs.pop("color",INK),**kwargs)
    def line(xs,ys,**kwargs):
        return ax.plot(xs,ys,color=kwargs.pop("color",GRID),lw=kwargs.pop("lw",.45),**kwargs)[0]
    def panel(letter,title,x,y):
        text(x,y,letter,size=9.2,role="strong");text(x+.18,y,title,size=10,role="serif")
    def tint(color,a):
        return tuple(1-a*(1-c) for c in to_rgb(color))
    panel("a","Evaluation scope",.13,3.25)
    cx,cy,angle=1.04,2.29,90.
    for fi in (1,3,2,0):
        family,_,count,color=FAMILIES[fi]
        ax.add_patch(Wedge((cx,cy),.48,angle-90+.65,angle-.65,width=.17,facecolor=color,edgecolor="white",lw=.3))
        mid=np.deg2rad(angle-45)
        text(cx+.40*np.cos(mid),cy+.40*np.sin(mid),family,role="strong",ha="center")
        for j in range(count):
            start,end=angle-90*(j+1)/count,angle-90*j/count
            ax.add_patch(Wedge((cx,cy),.83,start+.55,end-.55,width=.335,facecolor=tint(color,.56+.44*j/(count-1)),edgecolor="white",lw=.3))
            theta=(start+end)/2
            rotation=(theta-90+180)%360-180
            if rotation < -90: rotation+=180
            if rotation > 90: rotation-=180
            text(cx+.73*np.cos(np.deg2rad(theta)),cy+.73*np.sin(np.deg2rad(theta)),f"{family}{j+1}",
                 ha="center",rotation=rotation,rotation_mode="anchor")
        angle-=90
    text(cx,cy+.045,"22",size=14,role="serif",ha="center")
    text(cx,cy-.11,"candidate tasks",size=5.6,ha="center",color=MUTED)
    for y,value,label in ((2.87,str(len(D["design"]["domains"])),"illustrated domains"),(2.37,"Held-out","within domain"),(1.87,f'N = {D["design"]["N"]}',"selection pool")):
        text(2.28,y,value,size=12,role="serif",ha="center")
        text(2.28,y-.16,label,ha="center",color=MUTED,size=6.6)
    panel("b","Deployment cost & quality",2.88,3.25)
    text(3.,3.08,"Per-output cost; Seed = 1",size=7.1,color=MUTED)
    x0,y0,w,h=3.18,1.88,2.07,1.03
    px=lambda x:x0+(x-.2)/1.1*w
    py=lambda y:y0+(y-60)/25*h
    for y in (60,70,80):
        line([x0,x0+w],[py(y)]*2);text(x0-.07,py(y),str(y),ha="right",color=MUTED)
    for x in (.25,.75,1.25):text(px(x),y0-.08,str(x),ha="center",color=MUTED)
    text(x0+w/2,y0-.26,"Relative deployment cost",ha="center",size=8)
    text(x0-.28,y0+h/2,"Agreement (%)",ha="center",rotation=90,size=8)
    offsets=[(.07,-.02),(-.47,-.02),(-.57,.12),(.08,-.04),(-.40,-.06),(.08,-.02),(-.32,.15)]
    names=["Fixed","Seed","Fusion","SkillOpt","GEPA","Meta","IterEval"]
    for i,(cost,mean) in enumerate(zip(D["cost"],np.mean(D["pair"],axis=1))):
        col=ERA if i==6 else "#8D999E"
        ax.plot(px(cost),py(mean),marker="D" if i==6 else "o",ms=5 if i==6 else 4,mfc=col,mec="white",mew=.4)
        dx,dy=offsets[i];text(px(cost)+dx,py(mean)+dy,names[i],size=6.1,color=col)
    text(3.,1.46,"Search cost is reported separately",size=6.7,color=MUTED)
    panel("c","Agreement gains across tasks",.13,1.31)
    text(5.27,1.31,"Difference (percentage points)",ha="right",color=MUTED,size=6.7)
    left,right,bottom,bh,gap=.40,5.27,.41,.55,.12
    step=(right-left-gap*3)/22;pos=left
    for val in (0,6,12):
        line([left,right],[bottom+bh*val/14]*2);text(left-.06,bottom+bh*val/14,str(val),ha="right",color=MUTED)
    for family,name,count,color in FAMILIES:
        fw=count*step;text(pos+fw/2,bottom+bh+.18,name,size=8.1,role="italic",ha="center")
        line([pos,pos+fw],[bottom+bh+.07]*2,color=color,lw=1.4)
        for j in range(count):
            center=pos+(j+.5)*step;domain=f"{family}{j+1}"
            text(center,bottom-.1,domain,size=6.1,ha="center")
            if domain in D["design"]["domains"]:
                k=D["design"]["domains"].index(domain)
                for dx,base,col in ((-.034,1,color),(.034,4,ERA)):
                    gain=D["pair"][6][k]-D["pair"][base][k]
                    ax.bar(center+dx,bh*gain/14,bottom=bottom,width=.055,color=col,zorder=3)
            else:
                text(center,bottom+.06,"–",size=6,color="#A9AFB1",ha="center")
        pos+=fw+gap
    text(.13,.10,"Family color: vs Seed   |   lake green: vs GEPA   |   dash: not included",size=6.7,color=MUTED)
    save(fig,"landscape")

def search():
    setup();fig,axs=plt.subplots(1,3,figsize=(5.4,1.50))
    fig.subplots_adjust(left=.07,right=.985,bottom=.25,top=.82,wspace=.47)
    colors=["#8D999E","#74A9C5","#EDDDAB",ERA]
    for ax,curves,title in zip(axs[:2],[D["devCurves"],D["heldoutCurves"]],["a  Development progress","b  Held-out controls"]):
        for (name,ys),color in zip(curves.items(),colors):
            ax.plot(D["checkpoints"],ys,color=color,lw=1.2,label=name)
        ax.set_title(title,loc="left",fontsize=7);ax.set_xlabel("Search budget (%)");ax.set_ylim(68,85)
        ax.legend(fontsize=5.0,frameon=False,loc="upper left")
        ax.grid(axis="y",color=GRID,lw=.4)
    axs[0].set_ylabel("Agreement (%)")
    labels=D["directionOutcomes"]["labels"];counts=D["directionOutcomes"]["counts"]
    axs[2].barh(np.arange(4),counts,color=[ERA,"#C2E5CF","#F2B8AE","#EDDDAB"])
    axs[2].set_yticks(np.arange(4));axs[2].set_yticklabels(["Gain","No gain","Early end","Budget"],fontsize=5.5)
    axs[2].invert_yaxis();axs[2].set_xlabel("Share (%)");axs[2].set_title("c  Direction outcomes",loc="left",fontsize=7)
    save(fig,"search")

def mining():
    setup();fig,axs=plt.subplots(1,3,figsize=(5.4,1.8))
    fig.subplots_adjust(left=.08,right=.97,bottom=.25,top=.82,wspace=.5)
    for ax,x,curves,title,xlabel in [(axs[0],D["labelBudgets"],D["miningCurves"],"a  Reused labels","Revealed groups"),
        (axs[1],D["timeBudgets"],D["timeCurves"],"b  New annotation","Person-minutes")]:
        for (name,ys),col in zip(curves.items(),["#8D999E",ERA,"#74A9C5"]):
            ax.plot(x,ys,marker="o",ms=2,color=col,lw=1,label=name)
        ax.set_title(title,loc="left",fontsize=7);ax.set_xlabel(xlabel);ax.set_ylim(70,85)
        ax.legend(frameon=False,fontsize=5);ax.grid(axis="y",color=GRID)
    axs[0].set_ylabel("Agreement (%)")
    from matplotlib.colors import LinearSegmentedColormap
    mat=np.array([float(row[4]) for row in D["miningRows"][:4]]).reshape(2,2)
    cmap=LinearSegmentedColormap.from_list("paper_lake",["#F4F7F6","#C2E5CF",ERA])
    axs[2].imshow(mat,cmap=cmap,vmin=70,vmax=85,aspect="auto")
    for j in range(2):
        for k in range(2):axs[2].text(k,j,f"{mat[j,k]:.1f}",ha="center",va="center",fontsize=8,color=INK)
    axs[2].set_xticks([0,1]);axs[2].set_xticklabels(["Random","Mined"])
    axs[2].set_yticks([0,1]);axs[2].set_yticklabels(["History","IterEval"],fontsize=6)
    axs[2].set_title("c  Joint effect",loc="left",fontsize=7)
    save(fig,"mining")

tables();landscape();search();mining()
FILES.extend([DATA/"scenario.json",ROOT/"scripts/render_ideal_scenario.py",
              ROOT/"scripts/render_c1_landscape.py",ROOT/"scripts/figure_fonts.py"])
manifest={"simulation_only":True,"empirical_evidence":False,"aggregate_scenario_only":True,
          "font_family":FAMILY,
          "no_statistical_inference":True,"files":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES}}
(DATA/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
