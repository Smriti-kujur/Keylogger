# Keylogger
This repository contains my keylogger project, an application designed for educational and ethical purposes. A keylogger records keystrokes on a computer to understand and analyze user input. Please note that the use of keyloggers for unauthorized or malicious activities is illegal and unethical.


**Key Features**:
Captures every keystroke made on the system.
Sends email notifications containing the logged keystrokes to a specified recipient.

**Usage:**
This keylogger is designed to capture keystrokes and, optionally, send email notifications containing the captured keystrokes. Follow these steps to use the keylogger responsibly and ethically:

**1. Installation:**

Clone or download the project repository to your local machine.

Ensure you have Python installed on your system.

Install any necessary dependencies by running pip install -r requirements.txt.

**2. Configuration:**

Open the file in a text editor.

Modify the configuration options as needed, such as specifying email notification settings or changing the log file location.

**3. Running the Keylogger:**

Open your terminal/command prompt and navigate to the project directory.

Run the keylogger script using the following command:

bash
Copy code
python keylogger.py
**4. Capturing Keystrokes:**

The keylogger will start capturing keystrokes and display them on the terminal.

The captured keystrokes will be logged to the specified log file (default: keystrokes.log) in the project directory.

**5. Email Notifications (Optional):**

If you configured email notifications in the config.json file, the keylogger will send email notifications containing the captured keystrokes to the specified recipient's email address.
**6. Ethical Considerations:**

This keylogger is intended solely for ethical and educational purposes.

Using this keylogger for unauthorized or malicious activities is strictly prohibited and illegal.

**7. Stopping the Keylogger:**

To stop the keylogger, press the 'Esc' key.
