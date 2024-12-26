
<div align="center">
  
# diec-test-gui
A graphical user interface (GUI) for the **diec** library, designed to make text encoding and decoding easier. This tool allows you to securely encode and decode text using the **diec** Python package.

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/VelisCore/diec-test-gui#license)
[![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/diec/)
[![Contributors](https://img.shields.io/github/contributors-anon/VelisCore/diec)](https://github.com/VelisCore/diec/graphs/contributors)
[![Downloads](https://static.pepy.tech/badge/diec)](https://pepy.tech/project/diec)

</div>

## Overview

`diec-test-gui` is a user-friendly test interface built using **CustomTkinter** for interacting with the **diec** encoding and decoding library. This application allows users to encode text into an encrypted format and later decrypt it using the same passphrase. It provides a convenient graphical interface for **diec**, which is otherwise command-line-based.

**diec** library supports:
- Encoding and encrypting text with a passphrase.
- Decoding and decrypting text securely.

The GUI integrates with **diec** to offer a streamlined user experience for encryption and decryption.

## Features

- **Encode Text**: Securely encrypt and save text using a passphrase.
- **Decode Text**: Decrypt previously encoded text using the same passphrase.
- **Real-time Notifications**: Get notifications once encoding or decoding is completed.
- **File Handling**: Select and load files directly for decoding, ensuring convenience and efficiency.

## Installation

To use the `diec-test-gui`, follow these steps:

1. Clone or download this repository:

   ```bash
   git clone https://github.com/VelisCore/diec-test-gui.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all dependencies including `diec`, `plyer`, and `CustomTkinter`.

## Usage

### Launching the Application

1. After installation, simply run the GUI by executing:

   ```bash
   python diec_test_gui.py
   ```

2. The GUI window will open, allowing you to encode or decode text.

### Encoding Text

1. Go to the **Encode** tab.
2. Enter the text you want to encrypt in the **Your Text** textbox.
3. Click the **Convert** button to encrypt the text using your passphrase.
4. Once encrypted, the output will be saved in a file called `encoded.diec` in the same directory.

### Decoding Text

1. Go to the **Decode** tab.
2. Click **Decode** and select the encrypted `.diec` file you wish to decode.
3. The decrypted text will appear in the **Decoded Text** textbox.

### Additional Features

- **Restart**: You can restart the application from the menu.
- **Information**: View information about the GUI and version through the **Info** menu.

## Screenshots

Here’s what the GUI looks like:

![diec-test-gui](assets/screenshots/diec_test_gui.png)

## Dependencies

- **diec**: The core Python library used for encoding and decoding.
- **CustomTkinter**: CustomTkinter for building a modern, responsive GUI.
- **plyer**: Used for desktop notifications to inform the user when encoding or decoding is complete.
- **CTkMenuBar & CTkMessagebox**: For enhanced menu and messagebox functionality.

### Install Required Libraries

Run the following command to install the required libraries:

```bash
pip install diec customtkinter plyer
```

## Contributing

We welcome contributions! If you’d like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Please make sure to follow the [contributing guidelines](CONTRIBUTING.md) when submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Author: **Eldritchy**  
Email: [eldritchy.help@gmail.com](mailto:eldritchy.help@gmail.com)  
GitHub: [https://github.com/Eldritchyl](https://github.com/VelisCore)

---

## Acknowledgments

- **CustomTkinter**: Created by [Tom Schimansky](https://github.com/TomSchimansky), used for building the modern GUI.
- **plyer**: Notifications library used in this application.
- **diec**: Main library for text encryption and decryption.
