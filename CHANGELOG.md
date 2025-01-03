# paramlib changelog

All notable changes to this project will be documented in this file.

---

## [v3.3.0] - 2024-12-03

### Changed

- Move the `data_uploading_error_dict` dictionary from the `global_parameters` to `config_params`. This object contains intuitive error messages depending on the exception code raised by a SQLAlchemy operation.
- Rename `config_dict` to `DATABASE_CREDENTIALS`. This variable will store the credentials for the database connection.

---

## [v3.2.0] - 2024-11-04

### Added

- Added `__init__.py` files to all first-level and deeper sub-packages for enhanced import access

### Changed

- Remove the redundant import of the deprecated and removed `parameters_and_constants` module in all affected modules.

---

## [v3.0.0] - 2024-11-01

### Changed
- For all files contained in this package, package names in the absolute imports have been relocated

---

## [2.1.0] - Initial Release - 2024-10-28

### Added
- `config_params` module: tools for defining and managing configuration parameters
- `global_parameters` module: storage and access of global constants for centralised management
