import time
import os

def measure_transfer_rate(file_path, dest_path):
    """
    Measures approximate data transfer rate of a file copy operation.
    
    Args:
        file_path (str): Path to the source file
        dest_path (str): Path to copy the file to

    Returns:
        float: Transfer rate in MB/s
    """
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # File size in MB
    start_time = time.time()
    
    # Perform the file copy
    with open(file_path, 'rb') as src, open(dest_path, 'wb') as dst:
        while chunk := src.read(1024 * 1024):  # Read/write in 1 MB chunks
            dst.write(chunk)
    
    end_time = time.time()
    elapsed = end_time - start_time
    transfer_rate = file_size_mb / elapsed if elapsed > 0 else 0
    return transfer_rate

# Example usage
source_file = "test_file.bin"
destination_file = "test_file_copy.bin"

# Create a 10MB test file if it doesn't exist
if not os.path.exists(source_file):
    with open(source_file, 'wb') as f:
        f.write(os.urandom(10 * 1024 * 1024))

rate = measure_transfer_rate(source_file, destination_file)
print(f"Approx. Data Transfer Rate: {rate:.2f} MB/s")
