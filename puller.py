"""
Script to pull files from CPython git into this package.
"""

# 3rd party
import formate
from apeye.requests_url import RequestsURL
from domdf_python_tools.paths import PathPlus

target_branch = 3.9

repo_base = PathPlus(".")

source_url = RequestsURL(f"https://raw.githubusercontent.com/python/cpython/{target_branch}/Lib/pprint.py")
stubs_url = RequestsURL("https://raw.githubusercontent.com/python/typeshed/master/stdlib/2and3/pprint.pyi")
test_pprint_url = RequestsURL(
		f"https://raw.githubusercontent.com/python/cpython/{target_branch}/Lib/test/test_pprint.py"
		)
test_set_url = RequestsURL(
		f"https://raw.githubusercontent.com/python/cpython/{target_branch}/Lib/test/test_set.py"
		)
test_support_url = RequestsURL(
		f"https://raw.githubusercontent.com/python/cpython/{target_branch}/Lib/test/support.py"
		)

test_dir = repo_base / "tests"
lib_dir = repo_base / "pprint36"
yapf_style = str(repo_base / ".style.yapf")
isort_config_file = str(repo_base / ".isort.cfg")

test_pprint_src = test_pprint_url.get().text
test_pprint_src = test_pprint_src.replace("import pprint", "import pprint36 as pprint")
test_pprint_src = test_pprint_src.replace("import test.test_set", "import tests._test_set")
test_pprint_src = test_pprint_src.replace("test.test_set", "tests._test_set")

(test_dir / "test_pprint.py").write_text(test_pprint_src)
(test_dir / "_test_set.py").write_text(test_set_url.get().text)
(lib_dir / "_pprint.py").write_text(source_url.get().text)


formate_config = formate.config.load_toml("formate.toml")
formate.reformat_file(lib_dir / "_pprint.py", formate_config)
formate.reformat_file(test_dir / "test_pprint.py", formate_config)
formate.reformat_file(test_dir / "_test_set.py", formate_config)
