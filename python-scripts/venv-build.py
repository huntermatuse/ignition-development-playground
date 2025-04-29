import os
import sys
import subprocess

def create_venv(venv_dir=".venv"):
    """Create a virtual environment in the specified directory."""
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment at {venv_dir}...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        print("Virtual environment created.")
    else:
        print(f"Virtual environment already exists at {venv_dir}.")

    print("\nTo activate it, run the following command based on your OS:")

    if os.name == "nt":  # Windows
        activate_cmd = f".\\{venv_dir}\\Scripts\\Activate.ps1"
        print(f"  {activate_cmd}")
    else:  # MacOS/Linux
        activate_cmd = f"source {venv_dir}/bin/activate"
        print(f"  {activate_cmd}")

if __name__ == "__main__":
    create_venv()
