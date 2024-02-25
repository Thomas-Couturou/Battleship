from cx_Freeze import setup, Executable
base = None
executables = [Executable("main.py", base=base)]

packages = ["idna", "pygame", "pygame_widgets", "random"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Bataille Navale",
    options = options,
    version = "1.0",
    description = '',
    executables = executables
)