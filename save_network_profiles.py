import subprocess
import openpyxl
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_network_profiles():
    logging.debug("Retrieving network profiles")
    try:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8', errors='backslashreplace').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in profiles_data if "All User Profile" in i]
        logging.debug(f"Found profiles: {profiles}")
        return profiles
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to retrieve network profiles: {e}")
        return []

def get_profile_info(profile):
    try:
        logging.debug(f"Retrieving profile info for: {profile}")
        profile_info = subprocess.run(f'netsh wlan show profile "{profile}" key=clear', shell=True, capture_output=True, text=True, errors='backslashreplace').stdout.split('\n')
        info = {}
        for line in profile_info:
            if "SSID name" in line:
                info['SSID'] = line.split(":")[1][1:-1]
            elif "Key Content" in line:
                info['Password'] = line.split(":")[1][1:-1]
        logging.debug(f"Profile info for {profile}: {info}")
        return info
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to retrieve profile info for {profile}: {e}")
        return {}

def save_to_excel(profiles_info):
    logging.debug("Saving profiles to Excel")
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Network Profiles"
        sheet.append(["SSID", "Password"])

        for profile in profiles_info:
            sheet.append([profile.get('SSID', ''), profile.get('Password', '')])

        file_path = os.path.join(os.path.dirname(__file__), "network_profiles.xlsx")
        workbook.save(file_path)
        logging.debug(f"Profiles saved to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save profiles to Excel: {e}")

def main():
    profiles = get_network_profiles()
    if profiles:
        profiles_info = [get_profile_info(profile) for profile in profiles] 
        save_to_excel(profiles_info)
    else:
        logging.error("No network profiles found")

if __name__ == "__main__":
    main()
