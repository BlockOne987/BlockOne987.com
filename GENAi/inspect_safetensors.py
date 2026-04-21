import os
import subprocess
from safetensors import safe_open
import numpy as np

def ensure_dependencies():
    """Ensure that required dependencies are installed."""
    try:
        import torch
    except ImportError:
        print("PyTorch is not installed. Installing now...")
        subprocess.check_call(["pip", "install", "torch"])

def get_safe_tensor_location():
    """Prompt the user for the location of the safe tensor file."""
    while True:
        location = input("Enter the path to your safe tensor file: ").strip()
        if os.path.isfile(location):
            return location
        else:
            print("Invalid file path. Please try again.")

def display_tensor_keys(file_path):
    """Display the keys of tensors in the safe tensor file."""
    try:
        with safe_open(file_path, framework="pt") as f:
            keys = f.keys()
            print("\nAvailable Tensor Keys:")
            for key in keys:
                print(f"- {key}")
            return keys
    except Exception as e:
        print(f"Error reading tensor keys: {e}")
        return []

def display_tensor_metadata(file_path, key):
    """Display metadata and a preview of the tensor for a specific key."""
    try:
        with safe_open(file_path, framework="pt") as f:
            tensor = f.get_tensor(key)
            print(f"\nKey: {key}")
            print(f"Shape: {tensor.shape}")
            print(f"Dtype: {tensor.dtype}")
            print(f"Device: {tensor.device}")
            print("First 5 Values:", tensor.flatten()[:5])
    except Exception as e:
        print(f"Error reading tensor metadata: {e}")

def main():
    """Main function to orchestrate the script."""
    print("\n=== Safe Tensor Inspector ===")

    # Ensure dependencies are installed
    ensure_dependencies()

    # Step 1: Get the file location
    file_path = get_safe_tensor_location()

    # Step 2: Display tensor keys
    keys = display_tensor_keys(file_path)
    if not keys:
        print("No tensors found or unable to read the file.")
        return

    # Step 3: Interactive selection
    while True:
        print("\nMenu:")
        print("1. View tensor keys")
        print("2. Inspect a tensor")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tensor_keys(file_path)
        elif choice == "2":
            key = input("Enter the tensor key to inspect: ").strip()
            if key in keys:
                display_tensor_metadata(file_path, key)
            else:
                print("Invalid key. Use option 1 to view available keys.")
        elif choice == "3":
            print("Exiting the inspector. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
