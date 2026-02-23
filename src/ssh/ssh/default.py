from ..ssh_server import SSHServerUser

class SSHUser(SSHServerUser):
    @property
    def username(self) -> str:
        return "default_user"
    @property
    def password(self) -> str:
        return "default_pass"
    def onEntry(__self__, process):
        process.stdout.write("Welcome to the SSH server!\n")