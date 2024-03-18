# Description

This script uses the tkinter library to provide the user with an easy to use GUI to select source images and target videos for facefusion CLI execution.

Essentially, it will allow you to run multiple videos on facefusion. 

This tool will not pass any configuration args to the underlying facefusion cli command. You must alter your facefusion.ini with your desired configuration. See the example facefusion.ini in this repo.

You may use the example facefusion.ini in this repo by replacing the facefusion.ini file at the top-level of the facefusion directory (same location as run.py).

# Setup

This tool assumes you've already got facefusion up and running. If not, please follow the facefusion repo for the installation instructions.

Copy the multi_job.py file to your facefusion directory (should be same location as the run.py).

In the facefusion directory, activate your virtual environment.

Run `pip install tk`

# Run it

Run `python multi_job.py`

Click Find Image Source(s) button to use file explorer to find your source images

Click Find Video Source(s) button to use file explorer to find your target videos

Click Execute to begin

The logs will not show since I haven't done the correct piping for subprocesses

Once a fusion is complete, you'll see a "Subprocess executed successfully for argument" log

![image](https://github.com/TheDynomike/multi-job-facefusion-script/assets/10679481/41013e4d-15bb-4e2b-9d26-f55ecb9ae9e3)

# Video Trimmer Tool

Use this to trim your videos. Should be self-explanatory once you see the UI. 

Choose a video, adjust the sliders start and finish times.

Click Trim and you can open the folder location of the output video in the output video line [Open Folder].
