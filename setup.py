import cx_Freeze

executables = [cx_Freeze.Executable("Game.py",)]

cx_Freeze.setup(
    name="Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["car2.png"]}},
    executables = executables

    )