# LaTeX How-To

First, ensure that you have TeX Live installed.

## Ubuntu

Install the full version:

```bash
sudo apt update
sudo apt upgrade
sudo apt install texlive-full
```

After installing TeX Live, use `make` to build the PDF. If `make` is not yet
installed:

```bash
sudo apt update
sudo apt upgrade
sudo apt install make
```

Change directories (`cd`) to the folder containing the `Makefile` and use
`make`:

```bash
cd /path/to/directory/
make
```

## macOS

Install [MacTeX](https://www.tug.org/mactex/), the standard TeX Live distribution for macOS.

After installing TeX Live, use `make` to build the PDF. If `make` is not yet
installed:

```bash
xcode-select --install
```

Change directories (`cd`) to the folder containing the `Makefile` and use
`make`:

```bash
cd /path/to/directory/
make
```

## WSL (Windows Subsystem for Linux)

Inside your WSL Ubuntu instance, install the full version:

```bash
sudo apt update
sudo apt upgrade
sudo apt install texlive-full
```

After installing TeX Live, use `make` to build the PDF. If `make` is not yet
installed:

```bash
sudo apt update
sudo apt upgrade
sudo apt install make
```

Change directories (`cd`) to the folder containing the `Makefile` and use
`make`:

```bash
cd /path/to/directory/
make
```

## Windows

This choice is the worst option. Install
[TeX Live for Windows](https://www.tug.org/texlive/windows.html).

After installing TeX Live, use `make` to build the PDF. Windows does not have
`make`, but it can be installed via Chocolatey or `winget`:

```powershell
choco install make
# OR
winget install GnuWin32.Make
```

Change directories (`cd`) to the folder containing the `Makefile` and use
`make`:

```bash
cd \\path\\to\\directory\\
make
```

