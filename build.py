import os
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

icon = r"icon\\app_colored_bottle.ico"

version = "0.2.0"

executables = [Executable("PetroAlchemy.py", base=base, icon=icon,)]

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    (
        "DestopShortcut",
        "DesktopFolder",
        f"PetroAlchemy {version}",
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
os.environ["TCL_LIBRARY"] = os.path.join(PYTHON_INSTALL_DIR, "tcl", "tcl8.6")
os.environ["TK_LIBRARY"] = os.path.join(PYTHON_INSTALL_DIR, "tcl", "tk8.6")

include_files = [
    os.path.join(PYTHON_INSTALL_DIR, "DLLs", "tk86t.dll"),
    os.path.join(PYTHON_INSTALL_DIR, "DLLs", "tcl86t.dll"),
    r"icon",
    r"data_example",
    r"app_settings.json",
    r"themes",
]

setup(
    name="PetroAlchemy",
    version=version,
    author="Michael Wentz",
    author_email="michaelwiv@gmail.com",
    url="https://github.com/mwentzWW/PetroAlchemy",
    python_requires=">=3.7",
    description="Open source desktop application for decline curve and financial analysis",
    options={
        "build_exe": {
            "packages": ["tkinter", "matplotlib", "mpl_toolkits"],
            "include_files": include_files,
        },
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)
