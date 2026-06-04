#!/usr/bin/env python3
"""DevDash - Terminal Developer Dashboard. Zero dependencies."""
import os, sys, json, subprocess, socket, datetime, platform

class C:
    R="[0;31m"; G="[0;32m"; Y="[1;33m"; B="[0;34m"
    M="[0;35m"; CY="[0;36m"; W="[1;37m"; D="[2m"
    X="[0m"; BD="[1m"

def box(title, lines, w=58):
    print(f"{C.CY}+{\"-\"*(w-2)}+{C.X}")
    print(f"{C.CY}|{C.BD}{C.W} {title:<{w-4}} {C.X}{C.CY}|{C.X}")
    print(f"{C.CY}+{\"-\"*(w-2)}+{C.X}")
    for l in lines:
        raw=l.replace(C.R,"").replace(C.G,"").replace(C.Y,"").replace(C.B,"").replace(C.M,"").replace(C.CY,"").replace(C.W,"").replace(C.D,"").replace(C.BD,"").replace(C.X,"")
        pad=w-4-len(raw)
        if pad<0: l=l[:w-7]+"..."; pad=0
        print(f"{C.CY}|{C.X} {l}{\"\"} *pad} {C.CY}|{C.X}")
    print(f"{C.CY}+{\"-\"*(w-2)}+{C.X}")

def run(cmd, default="N/A"):
    try:
        r=subprocess.run(cmd,shell=True,capture_output=True,text=True,timeout=5)
        return r.stdout.strip() or default
    except: return default

def main():
    now=datetime.datetime.now().strftime("%A, %B %d %Y  %I:%M %p")
    os_name=run("uname -srm") if os.name!="nt" else platform.platform()
    uptime=run("uptime -p","").replace("up ","") or "N/A"
    shell=os.environ.get("SHELL","").split("/")[-1] or "N/A"
    hostname=socket.gethostname()
    user=os.environ.get("USER","")
    box("System", [f"OS: {os_name}", f"Host: {hostname}", f"User: {user}", f"Shell: {shell}", f"Uptime: {uptime}", f"Python: {platform.python_version()}"])
    git_user=run("git config user.name")
    repos=run("find ~ -maxdepth 4 -name .git -type d 2>/dev/null | wc -l")
    box("Git", [f"User: {git_user}", f"Repos: {repos}"])
    disk=run("df -h / | tail -1 | awk \"{print \$3\\" / \\"\$2}\"" ,"N/A")
    mem=run("free -h | awk \"/Mem:/{print \$3\\" / \\"\$2}\"","N/A")
    box("Resources", [f"Disk: {disk}", f"Memory: {mem}"])
    ip=run("hostname -I 2>/dev/null | awk \"{print \$1}\"","N/A")
    box("Network", [f"Local IP: {ip}"])
    print(f"\n  DevDash v1.0 · {now} · github.com/mayank-dev-15/devdash\n")

if __name__=="__main__": main()
