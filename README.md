# Selenium Automation Script for Registration Form

This project demonstrates how to use Selenium WebDriver with Python to automate interactions with a web-based registration form. The script opens a local HTML file, interacts with various form elements (like checkboxes and radio buttons), and submits the form.

## Project Structure

- `form.html`: The HTML file containing the registration form.
- `check_buttons.py`: The Python script that automates interactions with the registration form.
- `geckodriver.exe`: The GeckoDriver executable required for Firefox automation.

## Prerequisites

- Python 3.12 or higher
- Selenium WebDriver for Python
- Mozilla Firefox
- GeckoDriver (compatible with your Firefox version)

## Setup

1. **Install Python and Selenium**:
   - Download and install Python from [python.org](https://www.python.org/).
   - Install Selenium using pip:
     ```sh
     pip install selenium
     ```

2. **Download GeckoDriver**:
   - Download the GeckoDriver executable from the [GeckoDriver releases page](https://github.com/mozilla/geckodriver/releases).
   - Place the GeckoDriver executable in a directory and note the path.

3. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```sh
     git clone https://github.com/your-username/selenium-registration-form.git
     ```

4. **Set Up the Project**:
   - Navigate to the project directory:
     ```sh
     cd selenium-registration-form
     ```
   - Place the `geckodriver.exe` in the project directory or update the script with the correct path to your GeckoDriver.

## Usage

1. **Update Paths in Script**:
   - Ensure the `gecko_driver_path` and `firefox_binary_path` variables in `check_buttons.py` are correctly set:
     ```python
     gecko_driver_path = r"path\to\your\geckodriver.exe"
     firefox_binary_path = r"path\to\your\firefox.exe"
     ```

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Execute the script using Python:
     ```sh
     & "C:/Program Files/Python312/python.exe" c:/Users/nanda/OneDrive/Desktop/testing/check_buttons.py
     ```

3. **View Output**:
   - The script will open Firefox, navigate to `form.html`, interact with the checkbox and radio button, and print a success message if all interactions are completed successfully.

## Troubleshooting

- Ensure the `form.html` file exists at the specified location.
- Check that the GeckoDriver path is correctly set.
- Verify that the Firefox binary path is correct.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
