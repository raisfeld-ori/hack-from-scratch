import subprocess
import platform
from typing import List


def check_port_process(port: int) -> List[str]:
    system = platform.system()
    
    try:
        if system == 'Windows':
            result = subprocess.run(
                f'netstat -ano | findstr :{port}',
                shell=True,
                capture_output=True,
                text=True
            )
            if result.stdout:
                pids = []
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        if parts:
                            pids.append(parts[-1])
                return pids
        else:
            result = subprocess.run(
                f'lsof -i :{port} -t',
                shell=True,
                capture_output=True,
                text=True
            )
            if result.stdout:
                return result.stdout.strip().split('\n')
    except Exception:
        pass
    
    return []


def kill_port_process(port: int) -> None:
    system = platform.system()
    pids = check_port_process(port)
    
    for pid in pids:
        if pid.strip():
            try:
                if system == 'Windows':
                    subprocess.run(f'taskkill /PID {pid} /F', shell=True, stderr=subprocess.DEVNULL)
                else:
                    subprocess.run(['kill', '-9', pid], stderr=subprocess.DEVNULL)
                print(f"Killed existing process (PID {pid}) on port {port}")
            except Exception:
                pass
