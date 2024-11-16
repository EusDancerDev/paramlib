# paramlib

**paramlib** is a Python library dedicated to managing configuration parameters and constants for applications. It provides structured modules for storing, accessing, and organizing global parameters and configuration data.

## Features

- **Configuration Parameters**:
  - Organised storage of application-wide parameters and constants.
- **Global Parameter Handling**:
  - Easy access to global variables, aiding in consistent and centralised management of constants.


---

## Installation Guide

### Dependency Notice

- As of these days, no third-party nor any package developed by the same author is required.

### Unconventional Installation Instructions

Until this package is available on PyPI or Anaconda, please follow these steps:

1. **Clone the Repository**: Download the repository to your local machine by running:
   ```bash
   git clone https://github.com/EusDancerDev/paramlib.git
   ```

2. **Check the Latest Version**: Open the `CHANGELOG.md` file in the repository to see the latest version information.

3. **Build the Package**: Navigate to the repository directory and run:
   ```bash
   python setup.py sdist
   ```
   This will create a `dist/` directory containing the package tarball.

4. **Install the Package**:
   - Navigate to the `dist/` directory.
   - Run the following command to install the package:
     ```bash
     pip3 install paramlib-<latest_version>.tar.gz
     ```
     Replace `<latest_version>` with the version number from `CHANGELOG.md`.

**Note**: Once available on PyPI and Anaconda, installation will be simpler and more conventional.

---

### Package Updates

To stay up-to-date with the latest version of this package, follow these steps:

1. **Check the Latest Version**: Open the `CHANGELOG.md` file in this repository to see if a new version has been released.

2. **Pull the Latest Version**:
   - Navigate to the directory where you initially cloned the repository.
   - Run the following command to update your local copy:
     ```bash
     git pull origin main
     ```

This will download the latest changes from the main branch of the repository. After updating, you may need to rebuild and reinstall the package as described in the [Installation Guide](#installation-guide) above.
