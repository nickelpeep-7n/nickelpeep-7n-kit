# nickelpeep-7n-kit

Summarize numeric CSV columns (n / min / max / mean).

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m nickelpeep_7n_kit.cli --help
```

```python
from nickelpeep_7n_kit.core import Nickelpeep7nTool

tool = Nickelpeep7nTool()
print(tool)
```

## Layout

```
nickelpeep_7n_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 nickelpeep-7n
