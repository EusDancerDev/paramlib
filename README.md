# paramlib

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version](https://img.shields.io/pypi/v/paramlib.svg)](https://pypi.org/project/paramlib/)

**paramlib** is a centralised Python library for global parameter management and configuration constants. It provides a comprehensive collection of standardised parameters, format strings, and configuration templates commonly used across scientific computing, data processing, and application development projects. The library emphasises consistency, maintainability, and ease of access to frequently used constants and configuration patterns.

## Features

- **Global Parameter Management**:
  - Centralised storage of frequently used constants and parameters
  - Standardised naming conventions following Python best practices
  - Organised parameter categories for easy navigation and maintenance
  - Version-controlled parameter definitions with change tracking

- **Time-Related Parameters**:
  - Comprehensive time format strings (basic, non-standard, and custom)
  - Month mappings and seasonal frequency dictionaries
  - Date unit conversions and mathematical time constants
  - Support for various time representations and calculations

- **Mathematical and Programming Concepts**:
  - Basic arithmetic operators and set operations
  - Regular expression patterns for common validation tasks
  - File system and storage entity type definitions
  - Common delimiter collections for string processing

- **Configuration Management**:
  - Database credential templates and error code mappings
  - User information management paths and structures
  - Socio-economical and climate science parameter collections
  - Standardised configuration patterns for various domains

## Installation

### Prerequisites

Before installing, please ensure the following dependencies are available on your system:

- **External Tools** (required for full functionality):
  - No external tools required (pure Python library)

- **Required Third-Party Libraries**:

  ```bash
  pip install pandas numpy
  ```

  Or via Anaconda (recommended channel: `conda-forge`):

  ```bash
  conda install -c conda-forge pandas numpy
  ```

- **Internal Package Dependencies**:

  ```bash
  pip install filewise
  pip install pygenutils                    # Core functionality
  pip install pygenutils[arrow]             # With arrow support (optional)
  ```

### For regular users (from PyPI)

```bash
pip install paramlib
```

### For contributors/developers (with latest Git versions)

```bash
# Install with development dependencies (includes latest Git versions)
pip install -e .[dev]

# Alternative: Use requirements-dev.txt for explicit Git dependencies
pip install -r requirements-dev.txt
pip install -e .
```

**Benefits of the new approach:**

- **Regular users**: Simple `pip install paramlib` with all dependencies included
- **Developers**: Access to latest Git versions for development and testing
- **PyPI compatibility**: All packages can be published without Git dependency issues

**If you encounter import errors:**

1. **For PyPI users**: The package should install all dependencies automatically. If you get import errors, try:

   ```bash
   pip install --upgrade paramlib
   ```

2. **For developers**: Make sure you've installed the development dependencies:

   ```bash
   pip install -e .[dev]
   ```

3. **Common issues**:
   - **Missing dependencies**: For regular users, all dependencies are included. For developers, use `pip install -e .[dev]`
   - **Python version**: Ensure you're using Python 3.10 or higher
   - **Pure Python library**: No external system dependencies required

### Verify Installation

To verify that your installation is working correctly:

```python
try:
    import paramlib
    from paramlib.global_parameters import COMMON_DELIMITER_LIST, BASIC_TIME_FORMAT_STRS
    from paramlib.config_params import DATABASE_CREDENTIALS
    
    print("✅ All imports successful!")
    print(f"✅ paramlib version: {paramlib.__version__}")
    print("✅ Installation is working correctly.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 For regular users: pip install paramlib")
    print("💡 For developers: pip install -e .[dev]")
```

## Usage

### Basic Global Parameters Access

```python
from paramlib.global_parameters import (
    BASIC_TIME_FORMAT_STRS,
    COMMON_DELIMITER_LIST,
    BASIC_ARITHMETIC_OPERATORS
)

# Access time format strings
datetime_format = BASIC_TIME_FORMAT_STRS["H"]  # "%F %T"
date_only_format = BASIC_TIME_FORMAT_STRS["D"]  # "%F"

# Use common delimiters
delimiter = COMMON_DELIMITER_LIST[0]  # "_"
csv_delimiter = COMMON_DELIMITER_LIST[4]  # ","

# Mathematical operators
operators = BASIC_ARITHMETIC_OPERATORS  # ["+", "-", "*", "/"]
```

### Configuration Parameters

```python
from paramlib.config_params import (
    DATABASE_CREDENTIALS,
    DB_ERROR_CODE_DICT,
    USER_INFO_JSON_PATH
)

# Database configuration template
db_config = DATABASE_CREDENTIALS.copy()
db_config.update({
    "username": "myuser",
    "password": "mypassword",
    "host": "localhost",
    "port": "5432",
    "database_name": "mydb"
})

# Handle database errors
error_code = "1045"
if error_code in DB_ERROR_CODE_DICT:
    print(f"Database error: {DB_ERROR_CODE_DICT[error_code]}")
    # Output: "Database error: Wrong username"

# User information file path
user_file = USER_INFO_JSON_PATH  # "users.json"
```

### Advanced Time Handling

```python
from paramlib.global_parameters import (
    NON_STANDARD_TIME_FORMAT_STRS,
    CUSTOM_TIME_FORMAT_STRS,
    MONTH_NUMBER_DICT,
    SEASON_TIME_FREQ_DICT
)

# Non-standard time formats
ctime_format = NON_STANDARD_TIME_FORMAT_STRS["CTIME_H"]  # "%a %b %d %T %Y"

# Custom Excel-compatible formats
excel_format = CUSTOM_TIME_FORMAT_STRS["CT_EXCEL_SPANISH_D"]  # "%d/%m/%y"

# Month and season mappings
month_letter = MONTH_NUMBER_DICT[3]  # "M" (March)
spring_freq = SEASON_TIME_FREQ_DICT[3]  # "Q-MAR"
```

### Scientific and Climate Data Parameters

```python
from paramlib.global_parameters import (
    EMISSION_RCP_SCENARIOS,
    CLIMATE_FILE_EXTENSIONS,
    MATHEMATICAL_YEAR_DAYS
)

# Climate change scenarios
scenarios = EMISSION_RCP_SCENARIOS  # ["historical", "rcp26", "rcp45", "rcp85"]

# Supported climate file formats
extensions = CLIMATE_FILE_EXTENSIONS  # ["nc", "grib", "netcdf_zip", "csv"]

# Mathematical approximations
year_days = MATHEMATICAL_YEAR_DAYS  # 360 (for simplified calculations)
```

### Regular Expressions and Validation

```python
from paramlib.global_parameters import PASSWORD_REGEX_PATTERN
import re

# Password validation
password = "MySecure123!"
if re.match(PASSWORD_REGEX_PATTERN, password):
    print("Password meets security requirements")

# The pattern validates:
# - Minimum 8 characters
# - At least one lowercase letter
# - At least one uppercase letter
# - At least one digit
# - At least one special character
```

### Data Processing Utilities

```python
from paramlib.global_parameters import (
    PANDAS_DATE_UNIT_LIST,
    NUMPY_DATE_UNIT_LIST,
    UNIT_FACTOR_DICT,
    TIME_FREQUENCIES_COMPLETE
)

# Date unit handling for pandas/numpy
pandas_units = PANDAS_DATE_UNIT_LIST  # ['D', 'ms', 'ns', 's', 'us']
numpy_units = NUMPY_DATE_UNIT_LIST    # ['Y', 'M', 'D', 'h', 'm', 's', 'ms', 'us', 'ns']

# Unit conversions
ms_factor = UNIT_FACTOR_DICT["ms"]  # 1e-3

# Time frequency options
frequencies = TIME_FREQUENCIES_COMPLETE
# ["year", "season", "month", "day", "hour", "minute", "second"]
```

## Project Structure

The package is organised as a focused parameter management library:

```text
paramlib/
├── global_parameters.py         # Global constants and parameters
├── config_params.py             # Configuration templates and mappings
├── __init__.py                  # Package initialisation
├── CHANGELOG.md                 # Version history and parameter updates
└── README.md                    # Package documentation
```

## Parameter Categories

### 1. Time-Related Parameters

- **Basic Time Formats**: Standard datetime format strings for common use cases
- **Non-Standard Formats**: Alternative time representations (ctime, etc.)
- **Custom Formats**: Specialised formats for Excel, regional settings
- **Month Mappings**: Numeric to letter conversions and seasonal frequencies
- **Date Units**: Pandas and NumPy compatible unit specifications

### 2. Mathematical Concepts

- **Arithmetic Operators**: Basic mathematical operation symbols
- **Set Operations**: Set algebra operation names and definitions
- **Mathematical Constants**: Approximations and standard values

### 3. Programming Concepts

- **File System**: Module names and entity type definitions
- **Regular Expressions**: Common validation patterns
- **String Processing**: Standard delimiter collections
- **Data Types**: Storage and processing type definitions

### 4. Configuration Management

- **Database Credentials**: Template structure for database connections
- **Error Mappings**: Common database error codes and descriptions
- **File Paths**: Standard configuration file locations

### 5. Socio-Economical Concepts

- **Climate Science**: RCP scenarios and file format specifications
- **Data Standards**: Common file extensions and format definitions

## Key Constants Reference

### Time Format Strings

```python
BASIC_TIME_FORMAT_STRS = {
    "H": "%F %T",        # Full datetime
    "D": "%F",                 # Date only
    "M": "%Y-%m",                    # Year-month
    "Y": "%Y"                        # Year only
}
```

### Common Delimiters

```python
COMMON_DELIMITER_LIST = ["_", "-", ";", ":", ",", "\n", "\t", " "]
```

### Database Configuration

```python
DATABASE_CREDENTIALS = {
    "username": "username",
    "password": "cool-password",
    "host": "host",
    "port": "port",
    "database_name": "dbname"
}
```

### Climate Science Parameters

```python
EMISSION_RCP_SCENARIOS = ["historical", "rcp26", "rcp45", "rcp85"]
CLIMATE_FILE_EXTENSIONS = ["nc", "grib", "netcdf_zip", "csv"]
```

## Naming Conventions

The library follows strict Python naming conventions:

- **Constants**: All uppercase with underscores (e.g., `BASIC_TIME_FORMAT_STRS`)
- **Dictionaries**: Descriptive names ending with appropriate suffixes (`_DICT`, `_LIST`, etc.)
- **Keys**: Descriptive, abbreviated where appropriate, consistent across similar structures
- **Values**: Standardised formats following industry best practices

## Integration Examples

### With Pandas DataFrames

```python
from paramlib.global_parameters import BASIC_TIME_FORMAT_STRS, PANDAS_DATE_UNIT_LIST
import pandas as pd

# Create datetime index with standard format
date_format = BASIC_TIME_FORMAT_STRS["H"]
df = pd.DataFrame({
    'timestamp': pd.to_datetime(['2023-01-01 12:00:00'], format=date_format),
    'value': [100]
})

# Use standard date units
df['timestamp'] = pd.to_datetime(df['timestamp'], unit=PANDAS_DATE_UNIT_LIST[0])
```

### With Configuration Management

```python
from paramlib.config_params import DATABASE_CREDENTIALS, DB_ERROR_CODE_DICT
import sqlalchemy

def create_database_connection():
    try:
        # Use template for connection
        conn_str = f"postgresql://{DATABASE_CREDENTIALS['username']}:{DATABASE_CREDENTIALS['password']}@{DATABASE_CREDENTIALS['host']}:{DATABASE_CREDENTIALS['port']}/{DATABASE_CREDENTIALS['database_name']}"
        engine = sqlalchemy.create_engine(conn_str)
        return engine
    except Exception as e:
        error_code = str(e.args[0])
        if error_code in DB_ERROR_CODE_DICT:
            print(f"Connection failed: {DB_ERROR_CODE_DICT[error_code]}")
        raise
```

### With Climate Data Processing

```python
from paramlib.global_parameters import EMISSION_RCP_SCENARIOS, CLIMATE_FILE_EXTENSIONS

def process_climate_files(directory_path):
    """Process climate data files based on standard scenarios and formats."""
    valid_scenarios = EMISSION_RCP_SCENARIOS
    valid_extensions = CLIMATE_FILE_EXTENSIONS
    
    for scenario in valid_scenarios:
        for ext in valid_extensions:
            file_pattern = f"*{scenario}*.{ext}"
            # Process files matching pattern
            print(f"Processing {scenario} files with extension {ext}")
```

## Best Practices

### Parameter Usage

- Import only the parameters you need to avoid namespace pollution
- Use descriptive variable names when assigning parameter values
- Document parameter usage in your code for maintainability
- Follow the established naming conventions when extending parameters

### Configuration Management

- Always copy dictionary templates before modifying them
- Validate parameter values before using them in production code
- Use the provided error mappings for consistent error handling
- Keep configuration separate from business logic

### Version Compatibility

- Check the changelog when updating to new versions
- Test parameter-dependent code when upgrading
- Use version pinning for production deployments
- Document parameter dependencies in your project requirements

## System Requirements

- **Python**: 3.10 or higher
- **Dependencies**: pandas and numpy (optional, for enhanced functionality)
- **Memory**: Minimal (constants are loaded on import)
- **Performance**: Instant access to all parameters

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request for:

- New parameter categories or constants
- Improved naming conventions
- Additional configuration templates
- Documentation enhancements

### Development Guidelines

1. **Follow naming conventions**: All constants must be uppercase with descriptive names
2. **Maintain organisation**: Add new parameters to appropriate categories
3. **Document changes**: Update CHANGELOG.md with parameter additions/modifications
4. **Test compatibility**: Ensure changes don't break existing parameter usage
5. **Provide examples**: Include usage examples for new parameter categories

```bash
git clone https://github.com/yourusername/paramlib.git
cd paramlib
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Python Community** for establishing naming convention standards
- **Scientific Computing Community** for parameter standardisation requirements
- **Open Source Contributors** for feedback and parameter suggestions
- **Data Science Community** for real-world usage patterns and requirements

## Contact

For questions or suggestions, please open an issue on GitHub or contact the maintainers.

## Troubleshooting

### Common Issues

1. **Import Errors**:

   ```python
   # Correct import
   from paramlib.global_parameters import BASIC_TIME_FORMAT_STRS
   
   # Avoid importing everything
   # from paramlib.global_parameters import *  # Not recommended
   ```

2. **Parameter Modification**:

   ```python
   # Safe parameter usage
   from paramlib.config_params import DATABASE_CREDENTIALS
   
   # Always copy before modifying
   my_config = DATABASE_CREDENTIALS.copy()
   my_config["username"] = "myuser"
   ```

3. **Version Compatibility**:

   ```python
   # Check parameter availability
   from paramlib.global_parameters import BASIC_TIME_FORMAT_STRS
   
   if "H_NO_DATE_SEP" in BASIC_TIME_FORMAT_STRS:
       format_str = BASIC_TIME_FORMAT_STRS["H_NO_DATE_SEP"]
   ```

### Getting Help

- Check the [CHANGELOG.md](CHANGELOG.md) for parameter updates
- Review parameter definitions in the source code
- Open an issue on GitHub for missing parameters or suggestions
- Consult the examples section for usage patterns
