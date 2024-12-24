from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class Volume:
    def __init__(self) -> None:
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.vol = cast(self.interface, POINTER(IAudioEndpointVolume))

    def mute(self, mute: bool = True) -> None:
        """Mutes the system vol."""
        self.vol.SetMute((1 if mute else 0), None)  #type:ignore

    def set_volume(self, volume: float) -> None:
        """Sets the system vol to the specified value."""
        self.vol.SetMasterVolumeLevelScalar(volume, None)  #type:ignore
