# Bing Wallpaper Auto Downloader & Slideshow

An automated tool for downloading and managing Bing daily wallpapers, featuring auto-cleanup, slideshow support, and silent background operation on Windows.

[中文说明](README_CN.md)

## Features

1. **Automatic Bing Wallpaper Download**
   - Downloads today's Bing wallpaper
   - Automatically checks and downloads wallpapers from the last 5 days (including today)
   - Downloads in UHD resolution (3840x2160)

2. **Smart File Management**
   - Uses date as filename (e.g., 20240224.jpg)
   - Maintains folder cleanliness:
     * Keeps only the latest 5 images (sorted by filename date)
     * Automatically removes older images
     * Performs cleanup after each download
   - Skips already downloaded images to avoid duplicates

3. **Logging System**
   - Detailed logging of download process and errors
   - Auto-cleanup of oversized log files (when exceeding 1MB)
   - Clear log format with separators

4. **Silent Operation**
   - Supports background silent running
   - Automatic network connection waiting
   - Supports auto-start on Windows login

## Deployment Guide

### 1. Requirements
- Windows 10/11
- Python 3.x
- Required Python package: `pip install -r requirements.txt`

### 2. File Description
- `bing_wallpaper.py`: Main program
- `run_wallpaper.bat`: Batch file for program execution and log management
- `run_wallpaper.vbs`: VBS script for silent running
- `requirements.txt`: Python dependency list
- `wallpaper_log.txt`: Running log file

### 3. Configuration
You can modify the following settings in `bing_wallpaper.py`:
```python
CONFIG = {
    "download_dir": "E:\\WallPapers",  # Wallpaper save directory
    "keep_images": 5,                   # Number of images to keep
    "check_days": 5                     # Number of days to check
}
```

### 4. Setting Up Auto-Start

#### Method: Using Windows Task Scheduler

1. Open Task Scheduler
   - Press `Win + R`
   - Type `taskschd.msc`
   - Click OK

2. Create New Task
   - Click "Create Task" in the right panel
   - General tab:
     - Name: `Bing Wallpaper Download`
     - Select "Run with highest privileges"
     - Configure for: Windows 10

3. Trigger Settings
   - Click "Triggers" tab
   - Click "New"
   - Begin the task: "At log on"
   - Delay task for: "10 minutes"
   - Check "Enabled"

4. Action Settings
   - Click "Actions" tab
   - Click "New"
   - Action: Start a program
   - Program/script: `wscript.exe`
   - Add arguments: `"full_path\run_wallpaper.vbs"`
     - Example: `"E:\Proj\WallPaper\run_wallpaper.vbs"`

5. Conditions (Optional)
   - Click "Conditions" tab
   - Configure network conditions as needed

6. Settings Tab
   - Configure additional options as needed
   - Recommend checking "Allow task to be run on demand"

### 5. Testing
1. Direct Test:
   - Double click `run_wallpaper.vbs`
   - Check `wallpaper_log.txt` for running status

2. Check Downloaded Images:
   - Open download directory (default: `E:\WallPapers`)
   - Verify images are downloaded correctly

## Setting Up Wallpaper Slideshow (Windows 11)

1. Open Windows Settings
   - Press `Win + I`
   - Or click Start menu and select "Settings"

2. Go to Personalization
   - Click "Personalization"
   - Select "Background"

3. Set Up Slideshow
   - In "Personalize your background" dropdown, select "Slideshow"
   - Click "Browse" to select image folder
   - Choose program's download directory (default: `E:\WallPapers`)

4. Configure Slideshow Options
   - Choose picture change interval (Recommended: 30 minutes or 1 hour)
   - Optional: Select "Random order"
   - Recommend enabling "Let slideshow run even when on battery power"

5. Optimize Settings
   - In "Choose a fit", select "Fill" or "Fit"
   - This ensures optimal display of UHD wallpapers

Windows will automatically cycle through wallpapers in the download directory at the specified interval. Since the program maintains the latest 5 images, the slideshow will always display the most recent Bing wallpapers.

## Notes

1. Ensure all file paths are correct
2. Make sure Python environment is properly configured
3. If file locations are changed, update paths in all related scripts
4. Regularly check log files to ensure proper operation 