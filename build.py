import os
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

icon = r"icon\\app_icon.ico"

VERSION = "0.3.0-beta"

executables = [
    Executable("main.py", base=base, icon=icon, targetName="PetroAlchemy.exe")
]

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    (
        "DestopShortcut",
        "DesktopFolder",
        "PetroAlchemy",
        "TARGETDIR",
        "[TARGETDIR]PetroAlchemy.exe",
        None,
        None,
        None,
        None,
        None,
        None,
        "TARGETDIR",
    )
]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {
    "data": msi_data,
    "upgrade_code": "{b207b059-48b5-4a83-a090-5af50e0c185d}",
    "install_icon": icon,
}

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

include_files = [
    r"icon",
    r"resources",
    r"data_example",
    r"model",
    r"settings",
    r"styles",
]

setup(
    name="PetroAlchemy",
    version=VERSION,
    author="Michael Wentz",
    author_email="michaelwiv@gmail.com",
    url="https://github.com/mwentzWW/PetroAlchemy",
    description="Open source desktop application for decline curve and financial analysis",
    options={
        "build_exe": {
            "packages": ["PySide2", "matplotlib", "mpl_toolkits"],
            "include_files": include_files,
            "excludes": ["matplotlib.tests", "numpy.random._examples"],
        },
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)
