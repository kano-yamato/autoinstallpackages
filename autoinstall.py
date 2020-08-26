#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess

def fetch_env() :
    with open("env.json") as f :
        return json.load(f)

def main() :
    env = fetch_env()
    user_pass = env["user"] + ":" + env["pass"]
    package_paths = [
        str(x).replace("\\","/") for x in Path(env["path"]).iterdir()
    ]
    service_jsp = env["domain"] + "/crx/packmgr/service.jsp"
    for path in package_paths :
        command = ["curl", "-k", "-sS", "-u", user_pass, "-F", "force=true", "-F", "file=@" + path, "-F", "install=true", service_jsp]
        subprocess.run(command,stdout = subprocess.PIPE, stderr = subprocess.PIPE)

if __name__ == "__main__" :
    main()
