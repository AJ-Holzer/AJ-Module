import os
from ..settings import settings
from ..os.network import get_local_ip


def _get_terminal_size() -> int:
    columns, _ = os.get_terminal_size()
    return columns

class Terminal:
    """
    Beautifies the terminal.
    """
    UN: str = str(os.getenv("username")) if os.getenv("username") else "Anonymous"
    IP: str = get_local_ip()
    prompt: str = "{username}@{local_ip} > {current_path}"
    promptSymbol: str = ">>"
    questionSymbol: str = "$"
    devider: str = "\u2500"
    currentPath: str = os.getcwd()
    colors: dict[str, str] = {
        "username": settings.GREEN,
        "local_ip": settings.GREEN,
        "current_path": settings.YELLOW,
    }

    def change_prompt_symbol(self, newPromptSymbol: str) -> None:
        """
        Changes the prompt symbol
        """
        self.promptSymbol = newPromptSymbol

    def change_prompt(self, newPrompt: str) -> None:
        """
        Changes the prompt of the terminal.

        Available:
            - username
            - local_ip
            - current_path
        """
        self.prompt = newPrompt

    def __colorize_prompt(self, normalPrompt: str) -> str:
        """
        Colorizes the prompt.
        """
        for key, value in self.colors.items():
            normalPrompt = normalPrompt.replace("{"+key+"}", value+"{"+key+"}"+settings.RESET)
        return normalPrompt
    
    def update_path(self, path: str) -> None:
        """
        Updates the path of the current script.
        """
        self.currentPath = path

    def input(self) -> str:
        """
        Gets user input.
        """
        colorizedPrompt: str = self.__colorize_prompt(self.prompt)
        formattedPrompt: str = f"{settings.MAGENTA}{self.devider*_get_terminal_size()}{settings.RESET}\n{colorizedPrompt.format(username=self.UN, local_ip=self.IP, current_path=self.currentPath)} {self.promptSymbol} "

        return input(formattedPrompt)

    def print(self, txt: str) -> None:
        """
        Prints text to the terminal.
        """
        lineColor: str = settings.GRAY

        # Print the line(s)
        print("\n".join([f"{lineColor}\u250c{settings.RESET}  {txt.split("\n")[0]}"] + [f"{lineColor}\u2502{settings.RESET}  " + line for line in txt.split("\n")[1:-1:]] + [f"{lineColor}\u2514{settings.RESET}  {txt.split("\n")[-1]}"])) if len(txt.split("\n")) > 1 else print(f"{lineColor}-{settings.RESET}  {txt}")

    def ask(self, question: str) -> str:
        """
        Asks a question to the user.
        """
        colorizedPrompt: str = self.__colorize_prompt(self.prompt)
        formattedPrompt: str = f"{settings.MAGENTA}{self.devider*_get_terminal_size()}{settings.RESET}\n{colorizedPrompt.format(username=self.UN, local_ip=self.IP, current_path=self.currentPath)} {self.questionSymbol} {settings.CYAN}{question}{settings.RESET} {self.promptSymbol} "

        return input(formattedPrompt)

    def cd(self, path: str) -> None:
        """
        Changes the current directory.
        """
        try:            
            os.chdir(path)
            self.currentPath = os.getcwd()
        except OSError as e:
            raise OSError(f"Could not change the path. --> {e}")
        except Exception as e:
            raise Exception(f"There was an unexpected error while changing the directory. --> {e}")
