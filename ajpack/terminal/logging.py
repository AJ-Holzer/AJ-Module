import datetime
import json
import inspect
from ..settings import settings
from concurrent.futures import ThreadPoolExecutor

GREEN: str = settings.GREEN
YELLOW: str = settings.YELLOW
RED: str = settings.RED
MAGENTA: str = settings.MAGENTA
BLUE: str = settings.BLUE
CYAN: str = settings.CYAN
RESET: str = settings.RESET

class Logger:
    """
    More advanced logging system.

    Use with 'logger = ajpack.Logger()'
    """
    def __init__(self) -> None:
        self.log_format: str = "[ {level} ] {timestamp} --> {message}"
        self.log_file_format: str = "(F: '{filename}', L: {line})  {level}  |  {timestamp}  ({message})"
        self.log_file: str | None = None  # Start with no log file
        self.print_debug: bool = True
        self.colored_log: bool = True
        self.async_logging: bool = False
        self.custom_levels: dict[str, str] = {}
        self.context: dict[str, str] = {}
        self.filters: set[str] = set()
        self.rate_limits: dict[str, tuple[int, int]] = {}
        self.structured_format: str | None = None
        self.executor: ThreadPoolExecutor | None = ThreadPoolExecutor(max_workers=1) if self.async_logging else None

        self._init_rate_limits()

    def _init_rate_limits(self) -> None:
        self.rate_limit_counters: dict[str, list[float]] = {}

    def _rate_limited(self, level: str) -> bool:
        if level not in self.rate_limits:
            return False

        max_messages, interval = self.rate_limits[level]
        current_time: float = datetime.datetime.now().timestamp()

        if level not in self.rate_limit_counters:
            self.rate_limit_counters[level] = []

        # Remove outdated timestamps
        self.rate_limit_counters[level] = [ts for ts in self.rate_limit_counters[level] if current_time - ts < interval]

        if len(self.rate_limit_counters[level]) < max_messages:
            self.rate_limit_counters[level].append(current_time)
            return False
        
        return True

    def set_format(self, format_str: str) -> None:
        self.log_format = format_str

    def set_file_format(self, format_str: str) -> None:
        self.log_file_format = format_str

    def log_to_file(self, file_path: str | None = None) -> None:
        self.log_file = file_path
        
    def disable_debug(self) -> None:
        self.print_debug = False

    def enable_colored_output(self) -> None:
        self.colored_log = True

    def disable_colored_output(self) -> None:
        self.colored_log = False

    def enable_async_logging(self) -> None:
        self.async_logging = True
        self.executor = ThreadPoolExecutor(max_workers=1)

    def disable_async_logging(self) -> None:
        self.async_logging = False
        if self.executor:
            self.executor.shutdown(wait=False)
            self.executor = None

    def add_custom_level(self, level_name: str, color: str) -> None:
        colors: dict[str, str] = {
            "green": GREEN,
            "yellow": YELLOW,
            "red": RED,
            "blue": BLUE,
            "magenta": MAGENTA,
            "cyan": CYAN,
            "white": RESET
        }

        if color in colors.keys():
            self.custom_levels[level_name.upper()] = colors[color]
        else:
            raise ValueError("Color not valid.")

    def add_context(self, **context: str) -> None:
        self.context.update(context)

    def set_filter(self, level: str) -> None:
        self.filters.add(level.upper())

    def enable_structured_logging(self, log_format: str = 'json') -> None:
        self.structured_format = log_format

    def set_rate_limit(self, level: str, max_messages: int, interval: int) -> None:
        self.rate_limits[level.upper()] = (max_messages, interval)

    def log(self, level: str, message: str, **kwargs: str) -> None:
        """
        Logs the level and the message.

        :param level: Levels: success, warning, error, debug, info
        :param message: The message to be logged.
        """
        level = level.upper()
        _print: bool = True

        if not self.print_debug and level in ["INFO", "DEBUG", "SUCCESS"]:
            _print = False
        if level in self.filters: return
        if self._rate_limited(level): return

        frame = inspect.stack()[1]
        line = frame.lineno
        filename = frame.filename  # Get the filename

        timestamp: str = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        context: str = ' '.join([f"{key}={value}" for key, value in self.context.items()])
        formatted_message: str = self.log_format.format(level=level, timestamp=timestamp, message=message, **kwargs)
        formatted_file_message: str = self.log_file_format.format(filename=filename, line=line, level=level, timestamp=timestamp, message=message, **kwargs)

        if context:
            formatted_message += f" | {context}"
        if self.colored_log:
            formatted_message = self._color_message(level, formatted_message)

        if self.structured_format == 'json':
            formatted_message = json.dumps({
                "level": level,
                "timestamp": timestamp,
                "message": message,
                **self.context
            })

        if self.async_logging and self.executor:
            if _print: self.executor.submit(self._write_log, formatted_message)
            self.executor.submit(self._write_log_to_file, formatted_file_message)
        else:
            if _print: self._write_log(formatted_message)
            self._write_log_to_file(formatted_file_message)

    def _color_message(self, level: str, message: str) -> str:
        colors: dict[str, str] = {
            "SUCCESS": GREEN,     # Green
            "WARNING": YELLOW,    # Yellow
            "ERROR": RED,         # Red
            "DEBUG": BLUE,        # Blue
            "INFO": CYAN,         # Cyan
            "ENDC": RESET,        # Reset color (white)
        }

        for key, value in self.custom_levels.items():
            colors[key] = value

        color: str = colors.get(level, colors["ENDC"])
        return f"{color}{message}{colors['ENDC']}"

    def _write_log_to_file(self, formatted_file_msg: str) -> None:
        if self.log_file:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(formatted_file_msg + '\n')

    def _write_log(self, message: str) -> None:
        print(message)
        
    def __del__(self) -> None:
        if self.executor:
            self.executor.shutdown(wait=False)