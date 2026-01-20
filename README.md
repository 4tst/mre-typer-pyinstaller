# mre-typer-pyinstaller


## steps to reproduce

1. clone this repo
2. run `scripts/build`
3. run `dist/main/main.exe test1` or `dist/main/main.exe test2`

## introduction


截止到[https://github.com/4tst/mre-typer-pyinstaller/commit/296e067d16bba5c1990e582d68122373200f697d](https://github.com/4tst/mre-typer-pyinstaller/commit/296e067d16bba5c1990e582d68122373200f697d)是正常的，但是在我的项目里报错

```console
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    from typer import Typer
  File "pyimod02_importers.py", line 457, in exec_module
  File "typer\__init__.py", line 7, in <module>
  File "pyimod02_importers.py", line 457, in exec_module
  File "click\__init__.py", line 10, in <module>
  File "pyimod02_importers.py", line 457, in exec_module
  File "click\core.py", line 21, in <module>
  File "pyimod02_importers.py", line 457, in exec_module
  File "click\types.py", line 13, in <module>
  File "pyimod02_importers.py", line 457, in exec_module
  File "click\_compat.py", line 513, in <module>
  File "pyimod02_importers.py", line 457, in exec_module
  File "click\_winconsole.py", line 16, in <module>
  File "pyimod02_importers.py", line 457, in exec_module
  File "ctypes\__init__.py", line 8, in <module>
ImportError: DLL load failed while importing _ctypes: 找不到指定的模块。
[PYI-31380:ERROR] Failed to execute script 'main' due to unhandled exception!

```