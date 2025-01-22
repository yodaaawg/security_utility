# Malware Scanner Application

A Python-based desktop application designed to scan files and folders for malware and suspicious code patterns, such as SQL-Injections. The app supports drag-and-drop functionality for user convenience and generates detailed scan reports. It is designed as a general-purpose security software, featuring tools for penetration testing, troubleshooting, and virus scanning for USB drives and individual files.

---

## Features

- **Drag-and-Drop Interface**: Easily drag files or folders onto the application.
- **Malware Scanning**: Uses antivirus engines like ClamAV for detecting malicious files.
- **Code Analysis**: Searches for suspicious patterns such as SQL-Injections or dangerous commands.
- **Penetration Testing Tools**: Includes features to simulate attacks and identify vulnerabilities.
- **Troubleshooting Utilities**: Helps diagnose and resolve potential security issues.
- **USB Drive Scanning**: Quickly scan USB drives for viruses and threats.
- **Detailed Reports**: Outputs the results of the scan as an HTML or text-based report.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## Installation

### Prerequisites

1. Install Python 3.8 or higher.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Install ClamAV for enhanced malware detection.

### Setting Up

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/malware-scanner.git
cd malware-scanner
```

---

## Usage

1. **Run the Application**:

```bash
python main.py
```

2. **Drag and Drop**:
   - Drag files or folders onto the application window to start scanning.

3. **Reports**:
   - View the scan results directly in the app or export them for later use.

---

## Technologies Used

- **Python**: Core programming language.
- **tkinter**: For creating the GUI.
- **ClamAV (via pyclamd)**: For malware scanning.
- **Regular Expressions**: For analyzing suspicious code patterns.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to the open-source community for providing tools and resources that made this project possible.

