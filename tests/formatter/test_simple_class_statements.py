import pytest

from .common import format_and_compare


# fmt: off
@pytest.mark.parametrize("input_code,expected_output_code", [
(
"""tool
tool
tool
""",
"""tool
tool
tool
""",
),
(
"""
tool
tool

tool
""",
"""tool
tool

tool
""",
),
(
"""
tool     # xxx
tool
# yyy
tool
""",
"""tool  # xxx
tool
# yyy
tool
""",
),
(
"""
# xxx
tool
tool

# zzz
tool
""",
"""# xxx
tool
tool

# zzz
tool
""",
),
(
"""
# xxx
tool
tool

# zzz
tool
# yyy
""",
"""# xxx
tool
tool

# zzz
tool
# yyy
""",
),
(
"""tool;tool;tool""",
"""tool
tool
tool
"""
),
# (
# """tool;tool;tool # xxx""",
# """tool
# tool
# tool  # xxx
# """
# ),
])
# fmt: on
def test_formatting(input_code, expected_output_code):
    format_and_compare(input_code, expected_output_code)