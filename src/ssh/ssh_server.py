from asyncssh import SSHServer, create_server
from abc import ABC, abstractmethod
from pathlib import Path
import importlib.util
import asyncio
import sys
import threading
from ..util import kill_port_process

class SSHServerUser(ABC):
    @property
    @abstractmethod
    def username(self) -> str:
        ...
    @property
    @abstractmethod
    def password(self) -> str:
        ...
    
    @abstractmethod
    def onEntry(__self__, process):
        ...
    
    @abstractmethod
    def onExit(__self__, process):
        ...
        
    @abstractmethod
    def onCommand(__self__, process, command):
        ...
    
    @abstractmethod
    def __init__(self):
        ...

class SSHServerManager(SSHServer):
    def password_auth_supported(self):
        return True
    
    @staticmethod
    def gather_users():
        users = []
        ssh_dir = Path(__file__).parent / "ssh"
        
        ssh_files = []
        for item in ssh_dir.iterdir():
            if item.is_file() and item.suffix == ".py":
                ssh_files.append(item)
        
        for ssh_file in ssh_files:
            spec = importlib.util.spec_from_file_location(f"ssh_{ssh_file.stem}", ssh_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[f"ssh_{ssh_file.stem}"] = module
            spec.loader.exec_module(module)
            
            if hasattr(module, 'SSHUser'):
                user_class = module.SSHUser
                if issubclass(user_class, SSHServerUser):
                    users.append(user_class())
        return users
            
    @staticmethod
    def handle_client(process):
        print("Received SSH connection")
    
    
    def validate_password(self, username, password):
        users = self.gather_users()
        for user in users:
            if user.username == username and user.password == password:
                return True
        return False

def start_ssh_server(host: str, port: int, host_key_path: Path):
    async def start():
        kill_port_process(port) # Won't do anything if the server isn't running
        
        async with await create_server(
            SSHServerManager,
            host, port,
            server_host_keys=[host_key_path],
            process_factory=SSHServerManager.handle_client
        ) as ssh_server:
            print(f"SSH Server running on {host}:{port}")
            await ssh_server.wait_closed()
    asyncio.run(start())


def start_ssh_server_background(host: str, port: int, host_key_path: Path):
    thread = threading.Thread(
        target=start_ssh_server,
        args=(host, port, host_key_path),
        daemon=True
    )
    thread.start()
