from cx_Freeze import setup, Executable, sys

includeFiles = ['icon.ico']
excludes = []
packages = []
base = None

if sys.platform == "win32":
    base = "win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "Billing System",
     "TARGETDIR",
     "[TARGETDIR]\main.exe",
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

bdist_msi_options = {"data": msi_data}
setup(
    version="0.1",
    description="Billing System",
    author="Avinash Bhumraj Parchake",
    name="Billing System",
    option={"build.exe": {"include_files": includeFiles}, "bdist_msi": bdist_msi_options},
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon="icon.ico",
        )
    ]
)
