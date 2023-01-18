import _xxsubinterpreters
import sys
def run_payload(payload: str) -> None:
    payload = sys.argv[2]
    # ruleid: dangerous-subinterpreters-run-string-tainted-env-args
    _xxsubinterpreters.run_string(_xxsubinterpreters.create(), payload)
    # fn: dangerous-subinterpreters-run-string-tainted-env-args
def okRun():
    # ok: dangerous-subinterpreters-run-string-tainted-env-args
    _xxsubinterpreters.run_string(_xxsubinterpreters.create(), "print(123)")
