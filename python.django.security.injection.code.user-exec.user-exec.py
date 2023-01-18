import asyncio
from textwrap import dedent
def unsafe(request):
    # ruleid: user-exec
    code = request.POST.get('code')
    print("something")
    exec(code)
def unsafe_inline(request):
    exec(request.GET.get('code'))
def unsafe_dict(request):
    exec(request.POST['code'])
def safe(request):
    # ok: user-exec
    code = """
    print('hello')
    """
    exec(dedent(code))
async def run_exec_inline_get_method_by_event_loop(request):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, exec, request.POST.get("code"))
async def run_exec_inline_dict_by_event_loop(request):
    await loop.run_in_executor(None, exec, request.POST["code"])
async def run_exec_by_get_method_event_loop(request):
    code = request.POST.get("code")
    await loop.run_in_executor(None, exec, code)
async def run_exec_by_event_loop(request):
    code = request.POST["code"]
