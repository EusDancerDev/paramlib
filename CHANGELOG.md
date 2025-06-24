# paramlib Changelog

All notable changes to this project will be documented in this file.

---

## [3.4.2] - 2025-06-25

### Changed (3.4.2)

#### **Global Parameters** (changing; 3.4.2)

- Update variable names and key names:
  - Changes have been made in the original file `global_parameters.py` in the `paramlib` package.
  - These include abbreviation addressing and variable/key name standardisation.

| Old variable name | New variable name |
|:-----------------:|:-----------------:|
| `BASIC_FOUR_RULES` | `BASIC_ARITHMETIC_OPERATORS` |
| `COMMON_DELIM_LIST` | `COMMON_DELIMITER_LIST` |
| `NON_STD_TIME_FORMAT_STRS` | `NON_STANDARD_TIME_FORMAT_STRS` |
| `OPERATIONS_SETS_LIST` | `SET_OPERATIONS` |
| `REGEX_PASSWORDS` | `PASSWORD_REGEX_PATTERN` |
| `TIME_FREQUENCIES_SHORT_1` | `TIME_FREQUENCIES_ABBREVIATED` |
| `TIME_FREQUENCIES_SHORTER_1` | `TIME_FREQUENCIES_BRIEF` |

| Dictionary variable (latest name) | Old key name | New key name |
|:----------------------------------:|:------------:|:------------:|
| `BASIC_TIME_FORMAT_STRS` | `H_NODATESEP` | `H_NO_DATE_SEP` |
| `BASIC_TIME_FORMAT_STRS` | `D_NODATESEP` | `D_NO_DATE_SEP` |
| `CUSTOM_TIME_FORMAT_STRS` | `CT_EXCEL_SPANISH_NOBAR_D` | `CT_EXCEL_SPANISH_NO_BAR_D` |
| `CUSTOM_TIME_FORMAT_STRS` | `CT_EXCEL_SPANISH_NOBAR_H` | `CT_EXCEL_SPANISH_NO_BAR_H` |
| `NON_STANDARD_TIME_FORMAT_STRS` | `CFT_D` | `CTIME_D` |
| `NON_STANDARD_TIME_FORMAT_STRS` | `CFT_H` | `CTIME_H` |
| `NON_STANDARD_TIME_FORMAT_STRS` | `CFT_M` | `CTIME_M` |

---

## [3.4.1] - 2025-04-24

### Changed (3.4.1)

#### **Configuration Management** (changing; 3.4.1)

- Module `global_parameters`:
  - Convert all constant names to uppercase following Python naming conventions
  - Update module documentation to reflect the uppercase naming convention

---

## [3.4.0] - 2025-04-24

### Changed (3.4.0)

#### **General** (changing; 3.4.0)

- Refactored package import structure:
  - Replace direct imports with `__all__` definitions in the only package initiator file.
  - Improved control over exported symbols when using 'from package import *'
  - Maintained consistent public API while following Python best practices.
- Toggle uppercase all constant names in all modules.

#### **Configuration Management** (changing; 3.4.0)

- Module `config_params`:
  - Add `port` field to `DATABASE_CREDENTIALS` dictionary.
  - Rename variable `DATA_UPLOADING_ERROR_DICT` to `DB_ERROR_CODE_DICT` for better clarity and conciseness.

---

## [3.3.2] - 2025-02-18

### Changed (3.3.2)

#### **General** (changing; 3.3.2)

- In all modules, replace `method` with `function` to accurately refer to the code block that contains the function definition, where no object is instantiated.

#### **Configuration Management** (changing; 3.3.2)

- Module `config_params`:
  - Rename constant `INFO_JSON_PATH` to `USER_INFO_JSON_PATH` to better reflect its purpose of storing user-specific information.
  - This change improves code readability and maintainability.

---

## [3.3.0] - 2024-12-03

### Changed (3.3.0)

#### **Configuration Management** (changing; 3.3.0)

- Move the `data_uploading_error_dict` dictionary from the `global_parameters` to `config_params`. This object contains intuitive error messages depending on the exception code raised by a SQLAlchemy operation.
- Rename `config_dict` to `DATABASE_CREDENTIALS`. This variable will store the credentials for the database connection.

---

## [3.2.0] - 2024-11-04

### Added (3.2.0)

#### **General** (adding; 3.2.0)

- Added `__init__.py` files to all first-level and deeper sub-packages for enhanced import access

### Changed (3.2.0)

#### **General** (changing; 3.2.0)

- Remove the redundant import of the deprecated and removed `parameters_and_constants` module in all affected modules.

---

## [3.0.0] - 2024-11-01

### Changed (3.0.0)

#### **General** (changing; 3.0.0)

- For all files contained in this package, package names in the absolute imports have been relocated

---

## [2.1.0] - Initial Release - 2024-10-28

### Added (2.1.0)

- Module `config_params`: tools for defining and managing configuration parameters
- Module `global_parameters`: storage and access of global constants for centralised management
