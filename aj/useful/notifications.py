from plyer import notification # type:ignore

def desktop_msg(title: str, msg: str) -> None:
    """
    Shows a desktop notification.\n
    If there is an not implemented error in your exe, just add this peace of\n
    code to your pyinstaller command:\n
    ``--hidden-import plyer.platforms.win.notification``
    """
    notification.notify(
        title=title,
        message=msg,
        timeout=0  # duration in seconds
    )