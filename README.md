# 🧠 Backup Automation Script
The Backup Automation Script is a powerful tool designed to create periodic backups of a specified source directory, handling errors and logging the backup process. This script is ideal for developers and system administrators who need to ensure the integrity and availability of their data. With its automated backup feature, you can rest assured that your files are safe and up-to-date.

## 🚀 Key Features
* **Automated Backup**: The script automates the backup process by continuously checking for the backup time and calling the `make_backup` function with a predefined source folder.
* **Error Handling**: The script handles errors that may occur during the backup process, logging them for future reference.
* **Logging**: The script logs the backup process, including successes and failures, to a specified output file.
* **Customizable**: The script can be easily modified to accept the source folder as an argument or read it from a configuration file.

## 🛠️ Tech Stack
* **Python**: The script is written in Python, utilizing its extensive libraries and simplicity.
* **pathlib**: Used for working with file paths and directories.
* **shutil**: Utilized for copying the source directory to the backup location.
* **datetime**: Used for generating the current date and time for naming the backup directory.
* **logging**: Employed for logging the backup process, including errors and successes.
* **time**: Used for implementing a delay between backup attempts.

## 📦 Getting Started / Setup Instructions
### Prerequisites
* Python 3.x installed on your system
* The `pathlib`, `shutil`, `datetime`, `logging`, and `time` libraries are included with the Python standard library, so no additional installation is required.

### Installation
1. Clone the repository to your local machine using `git clone`.
2. Navigate to the project directory using `cd`.
3. Run the script using `python main.py`.

### Running locally
1. Modify the `source_folder` variable in the `automated_backup` function to point to the directory you want to backup.
2. Run the script using `python main.py`.
3. The script will start the automated backup process, logging the results to a file.

## 🤝 Contributing
Contributions are welcome and encouraged. If you have any ideas or improvements, please submit a pull request or issue.

## 📬 Contact
For any questions or concerns, please contact at zenabadnan10@gmail.com.

## 💖 Thanks Message
Thank you for checking out this project.
