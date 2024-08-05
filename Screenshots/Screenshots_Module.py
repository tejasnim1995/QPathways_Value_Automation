import os

# Define screenshot_path
screenshot_path = r"C:\Users\tejas.nimbalkar\PycharmProjects\Qpathways_Value_Automation\Screenshots"


def clear_screenshots():
    # Check if the directory exists
    if os.path.exists(screenshot_path):
        # Delete all files in the directory
        for filename in os.listdir(screenshot_path):
            file_path = os.path.join(screenshot_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        # Create the directory if it doesn't exist
        os.makedirs(screenshot_path)
