# ParamLib

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version](https://img.shields.io/pypi/v/paramlib.svg)](https://pypi.org/project/paramlib/)

A Python library for parameter management and configuration handling.

## Features

- **Parameter Management**
  - Structured parameter definition
  - Type validation and conversion
  - Default value handling
  - Parameter grouping and hierarchy

- **Configuration Handling**
  - Multiple format support (JSON, YAML, TOML)
  - Environment variable integration
  - Configuration file loading
  - Configuration validation

- **Validation and Type Checking**
  - Built-in type validators
  - Custom validation rules
  - Parameter constraints
  - Error handling and reporting

- **Serialization**
  - Parameter serialization to various formats
  - Configuration export/import
  - Parameter state management
  - Version control support

## Installation

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager

### Using pip

```bash
pip install paramlib
```

### Using conda

```bash
conda install -c conda-forge paramlib
```

## Usage

### Basic Usage

```python
from paramlib import Parameter, ParameterGroup

# Create a parameter
param = Parameter(
    name="temperature",
    value=25.0,
    type=float,
    description="Room temperature in Celsius"
)

# Create a parameter group
group = ParameterGroup("settings")
group.add_parameter(param)

# Access parameters
print(group.temperature)  # 25.0
```

### Advanced Usage

```python
from paramlib import ConfigManager

# Load configuration from file
config = ConfigManager.from_file("config.yaml")

# Access nested parameters
value = config.get("section.subsection.parameter")

# Update parameters
config.set("section.parameter", new_value)

# Save configuration
config.save("new_config.yaml")
```

## Project Structure

```text
paramlib/
├── paramlib/              # Main package directory
│   ├── core/             # Core functionality
│   │   ├── parameter.py  # Parameter class
│   │   └── group.py      # Parameter group handling
│   ├── config/           # Configuration management
│   │   ├── manager.py    # Configuration manager
│   │   └── validators.py # Validation utilities
│   └── utils/            # Utility functions
│       ├── serializers.py # Serialization tools
│       └── helpers.py     # Helper functions
├── tests/                # Test suite
├── docs/                 # Documentation
└── examples/             # Usage examples
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/paramlib.git
   cd paramlib
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:

   ```bash
   pip install -e ".[dev]"
   ```

### Testing

Run the test suite:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped improve this library
- Inspired by various parameter management systems

## Contact

For questions or suggestions, please open an issue on GitHub or contact the maintainers.
