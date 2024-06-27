import psutil

def kill_process(pid: int):
    """Kills a process by its PID. Use aj.list_processes() to get the pid of a process."""
    psutil.Process(pid).terminate()