# Create a function to display the progress of a download.

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")


display_progress(3)
