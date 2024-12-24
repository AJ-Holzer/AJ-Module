import psutil  #type:ignore[import-untyped]

def kill_process(pid: int):
    """
    Terminates a process by its PID. Use aj.list_processes() to get the pid of a process.

    :param pid (int): Pid to terminate.
    """
    psutil.Process(pid).terminate()
