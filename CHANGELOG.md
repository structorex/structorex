# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2026-04-29

### Added
- Professional project structure using `src/structorex` layout.
- Fully featured Command Line Interface (CLI) replacing interactive inputs.
- Support for configuration files: `.structorex.yaml`, `.structorex.json`, and `pyproject.toml`.
- Parallel file reading using `ThreadPoolExecutor` for significant performance boost.
- Progress bar integration with `tqdm`.
- Multiple export formats: Markdown, JSON, HTML (interactive), and Text.
- Advanced security filtering for secrets (e.g., `.env`, `id_rsa`) and sensitive file types.
- Native `.gitignore` support using `pathspec`.
- ZIP snapshot export feature (`--export-zip`).
- Comprehensive test suite with `pytest`.
- Multi-language documentation (EN, DE, RU) in `docs/` and READMEs.
- Automatic text encoding detection with `charset-normalizer`.
- GitHub Actions CI/CD workflows for testing, linting, and PyPI publishing.

### Changed
- Migrated from `os.listdir` to `os.scandir` for better performance.
- Refactored core logic using the **Visitor Pattern** for better extensibility.
- Updated project name to **Structorex**.

### Fixed
- Various PEP 8 linting issues and encoding errors.
- Corrected package import issues in CI pipelines.

## [0.1.0] - 2026-04-14
- Initial release as a basic file tree generator.
