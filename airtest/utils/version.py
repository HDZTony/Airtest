__version__ = "1.3.5"

import os
import sys


def get_airtest_version():
    pip_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    pip_pkg_dir = os.path.abspath(pip_pkg_dir)

    # 使用sys.version_info.major和minor确保显示完整版本号（如3.13）
    return f'airtest {__version__} from {pip_pkg_dir} (python {sys.version_info.major}.{sys.version_info.minor})'


def show_version():
    sys.stdout.write(get_airtest_version())
    sys.stdout.write(os.linesep)
    sys.exit()
