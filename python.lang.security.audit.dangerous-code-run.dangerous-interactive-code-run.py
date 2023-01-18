import code
def run_payload1(payload: str) -> None:
    console = code.InteractiveConsole()
    # ruleid: dangerous-interactive-code-run
    console.push(payload)
def run_payload2(payload: str) -> None:
    inperpreter = code.InteractiveInterpreter()
    inperpreter.runcode(code.compile_command(payload))
def run_payload3(payload: str) -> None:
    pl = code.compile_command(payload)
    inperpreter.runcode(pl)
def run_payload4(payload: str) -> None:
    inperpreter.runsource(payload)
def ok1() -> None:
    console.push('print(123)')
def ok2() -> None:
    inperpreter.runcode(code.compile_command('print(123)'))
def ok3() -> None:
    pl = code.compile_command('print(123)')
def ok4() -> None:
    inperpreter.runsource('print(123)')
