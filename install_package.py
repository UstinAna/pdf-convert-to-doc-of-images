import subprocess
import sys

def upgrade_package(package):
    """Upgrade a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        print(f"Successfully upgraded {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to upgrade {package}")

def install_package(package):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

if __name__ == "__main__":
    packages = ["pip", "setuptools", "wheel"]

    for package in packages:
        upgrade_package(package)

    # List of packages to install
    packages = [
        "fitz",  # PyMuPDF
        "fpdf"
        # Add more packages here if needed
    ]

    for package in packages:
        install_package(package)
