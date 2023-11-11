# Qubes OS Offline Documentation
This package can be used to maintain an offline version of the Qubes OS documentation.

## Compilation:
- Using A Fedora 37 Minimal Airgapped VM
```
# Install the dependencies, note the DNF package of panflute throws an exception when compiling.
sudo dnf install git pandoc pip texlive texlive-ulem evince -y
pip --proxy 127.0.0.1:8082 install panflute

# Fetch the source
git config --global http.proxy 127.0.0.1:8082
git clone https://github.com/QubesOS/qubes-offline-doc.git
cd qubes-offline-doc
make get-sources
git config --global http.proxy unset

# Build
make all

# Install
sudo make install
```
- Using A Fedora 37 Minimal Internet-Connected VM
```
# Install the dependencies, note the DNF package of panflute throws an exception when compiling.
sudo dnf install git pandoc pip texlive texlive-ulem evince -y
pip install panflute

# Fetch the source
git clone https://github.com/QubesOS/qubes-offline-doc.git
cd qubes-offline-doc
make get-sources

# Build
make all

# Install
sudo make install
```
