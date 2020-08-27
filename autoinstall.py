#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import os
import datetime
import xml.etree.ElementTree as ET

def fetch_env() :
    with open("env.json") as f :
        return json.load(f)

def write_log(path, stdout) :
    root = ET.fromstring(stdout)
    err_msg = root.findall(".//response/status[@code='500']")
    log_file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
    os.makedirs("logs", exist_ok=True)
    if err_msg :
        with open("logs/" + log_file_name, "w") as f :
            f.write(path + ": " + err_msg[0].text)


def main() :
    env = fetch_env()
    user_pass = env["user"] + ":" + env["pass"]
    package_paths = [
        str(x).replace("\\","/") for x in Path(env["path"]).iterdir()
        if ".zip" in str(x)
    ]
    service_jsp = env["domain"] + "/crx/packmgr/service.jsp"
    for path in package_paths :
        command = ["curl", "-k", "-sS", "-u", user_pass, "-F", "force=true", "-F", "file=@" + path, "-F", "install=true", service_jsp]
        stdout = subprocess.check_output(command)
        write_log(path, stdout)

if __name__ == "__main__" :
    main()
