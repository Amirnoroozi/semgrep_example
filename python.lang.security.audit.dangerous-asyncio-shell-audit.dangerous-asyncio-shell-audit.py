import asyncio
class AsyncEventLoop:
    def __enter__(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        return self.loop
    def __exit__(self, *args):
        self.loop.close()
class WaitingProtocol(asyncio.SubprocessProtocol):
    def __init__(self, exit_future):
        self.exit_future = exit_future
    def process_exited(self):
        self.exit_future.set_result(True)
def vuln1(shell_command):
    with AsyncEventLoop() as loop:
        exit_future = asyncio.Future(loop=loop)
        # ruleid: dangerous-asyncio-shell-audit
        transport, _ = loop.run_until_complete(loop.subprocess_shell(lambda: WaitingProtocol
        (exit_future), shell_command))
        loop.run_until_complete(exit_future)
        transport.close()
def vuln2(shell_command):
        proc = loop.run_until_complete(asyncio.subprocess.create_subprocess_shell
        (shell_command))
        loop.run_until_complete(proc.wait())
def ok1():
    shell_command = 'echo "Hello world"'
        # ok: dangerous-asyncio-shell-audit
def ok2():
        proc = loop.run_until_complete(asyncio.subprocess.create_subprocess_shell('echo 
        "foobar"'))
