# save_network_profile
# Network Profiles

This project contains scripts to save network profiles and passwords to an Excel file. It includes a Python script for Windows and an Android application.

## Python Script

### Prerequisites

- Python 3.x
- `openpyxl` module

### Installation

1. Install the `openpyxl` module:
    ```sh
    pip install openpyxl
    ```

### Usage

1. Navigate to the directory containing the script:
    ```sh
    cd /c:/Users/209/OneDrive/Desktop/project/script/net
    ```
2. Run the script:
    ```sh
    python save_network_profiles.py
    ```

The script will create an Excel file named `network_profiles.xlsx` in the same directory, containing all the network profiles and their passwords.

## Android Application

### Prerequisites

- Android Studio
- An Android device or emulator

### Setup

1. Open Android Studio.
2. Open the project located at `/c:/Users/209/OneDrive/Desktop/project/script`.
3. Sync the project with Gradle to download the necessary dependencies.

### Permissions

The application requires the following permissions:
- `ACCESS_WIFI_STATE`
- `CHANGE_WIFI_STATE`
- `WRITE_EXTERNAL_STORAGE`
- `READ_EXTERNAL_STORAGE`

These permissions are already declared in the `AndroidManifest.xml` file.

### Running the Application

1. Connect an Android device via USB or set up an Android emulator.
2. Click the "Run" button (green play icon) in Android Studio.
3. Select the connected device or emulator and click "OK".

The application will request the necessary permissions and save the network profiles to an Excel file on the device's external storage.

### Dependencies

Add the following dependency to your `build.gradle` file:
```groovy
implementation 'org.apache.poi:poi-ooxml:5.0.0'
```

### Files

- `save_network_profiles.py`: Python script to save network profiles on Windows.
- `AndroidManifest.xml`: Android manifest file with required permissions.
- `MainActivity.java`: Main activity for the Android application.
- `build.gradle`: Gradle build file with dependencies.
