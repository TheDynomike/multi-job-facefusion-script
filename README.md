# Description

This script uses the tkinter library to provide the user with an easy to use GUI to select source images and target videos for facefusion CLI execution.

This tool will not pass any configuration args to the underlying facefusion cli command. You must alter your facefusion.ini with your desired configuration. See the example facefusion.ini in this repo.

# Setup

Copy the multi_job.py file to your facefusion directory (should be same location as the run.py).

Add `tk` to the requirements.txt file in the facefusion directory (See example requirements.txt here).

In the facefusion directory, activate your virtual environment.

Run `pip install -r requirements.txt`

Run `python multi_job.py`
