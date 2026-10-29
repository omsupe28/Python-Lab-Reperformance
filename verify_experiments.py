from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import importlib.util
import math
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def load_program(number):
    path = ROOT / f"Experiment-{number}" / f"experiment_{number}.py"
    spec = importlib.util.spec_from_file_location(f"experiment_{number}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    for number in (1, 2, 3):
        folder = ROOT / f"Experiment-{number}"
        with TemporaryDirectory() as working_directory:
            result = subprocess.run(
                [sys.executable, "-B", str(folder / f"experiment_{number}.py")],
                cwd=working_directory, capture_output=True, text=True,
                encoding="utf-8", check=True,
            )
        assert result.stderr == "", result.stderr
        assert result.stdout == (folder / "output.txt").read_text(encoding="utf-8")
        print(f"PASS: Experiment {number} executes from another directory and matches output.txt")

    sys.path.insert(0, str(ROOT / "Experiment-1"))
    from MyPackage import arithmetic, geometry

    assert arithmetic.add(10, 5) == 15
    assert arithmetic.subtract(10, 5) == 5
    assert arithmetic.add(-2, 2) == 0
    assert arithmetic.subtract(0, 5) == -5
    assert arithmetic.add(1.5, 2.5) == 4
    assert math.isclose(geometry.area_of_circle(7), 153.86)
    assert math.isclose(geometry.perimeter_of_circle(7), 43.96)
    assert geometry.area_of_circle(0) == 0
    assert geometry.perimeter_of_circle(0) == 0
    assert math.isclose(geometry.area_of_circle(1.5), 7.065)
    print("PASS: Package imports, arithmetic, circle calculations, zero and decimal inputs")

    expected = "This is the original content.\nAdding some more text.\nAppending new content."
    source = ROOT / "Experiment-2" / "outputs" / "source.txt"
    destination = source.with_name("destination.txt")
    assert source.read_text(encoding="utf-8") == expected
    assert destination.read_text(encoding="utf-8") == expected
    assert source.read_bytes() == destination.read_bytes()
    second = load_program(2)
    with redirect_stdout(StringIO()):
        assert second.main() == 0
    assert source.read_text(encoding="utf-8") == expected
    with patch("builtins.open", side_effect=PermissionError("test permission denied")):
        with redirect_stdout(StringIO()) as output:
            assert second.main() == 1
    assert "File operation failed:" in output.getvalue()
    print("PASS: File write/read/append/copy, exact copied bytes, repeated run and I/O error handling")

    third = load_program(3)
    cases = [
        (10, 2, "The result is: 5.0"),
        (10, 0, "Error: Cannot divide by zero!"),
        ("ten", 2, "Error: Invalid input type."),
        (10, "two", "Error: Invalid input type."),
        (10, None, "Error: Invalid input type."),
        (-9, 3, "The result is: -3.0"),
        (0, 2, "The result is: 0.0"),
        (7.5, 2.5, "The result is: 3.0"),
    ]
    for numerator, denominator, message in cases:
        with redirect_stdout(StringIO()) as output:
            third.divide_numbers(numerator, denominator)
        assert message in output.getvalue()

    class RaisesValueError:
        def __truediv__(self, other):
            raise ValueError("test value error")

    class RaisesRuntimeError:
        def __truediv__(self, other):
            raise RuntimeError("test runtime error")

    for value, message in [
        (RaisesValueError(), "Error: Invalid input value."),
        (RaisesRuntimeError(), "An unexpected error occurred: test runtime error"),
    ]:
        with redirect_stdout(StringIO()) as output:
            third.divide_numbers(value, 2)
        assert message in output.getvalue()
    assert third.convert_to_int("25") == 25
    assert third.convert_to_int("-7") == -7
    assert third.convert_to_int("two") == "Error: Invalid input!"
    assert third.find_index([10, 20, 30], 20) == 1
    assert third.find_index([], 10) == "Error: Element not found!"
    print("PASS: All five original division cases, extra numeric cases, ValueError and fallback handlers")
    print("PASS: Integer conversion and list-search question functions, including invalid values")
    print("All verification checks passed.")


if __name__ == "__main__":
    main()
