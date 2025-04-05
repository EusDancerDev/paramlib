# paramlib changelog

All notable changes to this project will be documented in this file.

---

## [v3.3.2] - 2025-02-18

### Changed

#### **General**

- In all modules, replace `method` with `function` to accurately refer to the code block that contains the function definition, where no object is instantiated.
- In module `config_params`, the constant `INFO_JSON_PATH` has been renamed to `USER_INFO_JSON_PATH` to better reflect its purpose of storing user-specific information. This change improves code readability and maintainability.

---

## [v3.3.0] - 2024-12-03

### Changed (v3.3.0)

- Move the `data_uploading_error_dict` dictionary from the `global_parameters` to `config_params`. This object contains intuitive error messages depending on the exception code raised by a SQLAlchemy operation.
- Rename `config_dict` to `DATABASE_CREDENTIALS`. This variable will store the credentials for the database connection.

---

## [v3.2.0] - 2024-11-04

### Added (v3.2.0)

- Added `__init__.py` files to all first-level and deeper sub-packages for enhanced import access

### Changed (v3.2.0)

- Remove the redundant import of the deprecated and removed `parameters_and_constants` module in all affected modules.

---

## [v3.0.0] - 2024-11-01

### Changed (v3.0.0)

- For all files contained in this package, package names in the absolute imports have been relocated

---

## [2.1.0] - Initial Release - 2024-10-28

### Added (v2.1.0)

- `config_params` module: tools for defining and managing configuration parameters
- `global_parameters` module: storage and access of global constants for centralised management
