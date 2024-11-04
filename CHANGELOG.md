# paramlib changelog

All notable changes to this project will be documented in this file.

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
- `global_parameters` module: storage and access of global constants for centralized management
