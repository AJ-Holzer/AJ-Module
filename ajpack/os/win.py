import subprocess

def get_terminal_output(command: str) -> str:
    """
    Executes a given command in the terminal and returns its output as a string.

    :param command: The command to execute.
    :return: The output from the command execution.
    """
    # Run the command and capture the output
    result = subprocess.run(
        command,
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return result.stdout.decode('cp850').strip()
