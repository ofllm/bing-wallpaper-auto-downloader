@echo off
chcp 65001 >nul

:: 设置日志文件路径
set "log_file=E:\Proj\WallPaper\wallpaper_log.txt"

:: 检查日志文件大小
for %%A in ("%log_file%") do set "log_size=%%~zA"
if %log_size% gtr 1048576 (
    :: 如果日志文件大于1MB，则清空它
    echo ============================================== > "%log_file%"
    echo %date% %time% 日志文件过大，已清理 >> "%log_file%"
    echo ============================================== >> "%log_file%"
)

echo ============================================== >> "%log_file%"
echo %date% %time% 开始执行 >> "%log_file%"

:check_network
ping -n 1 cn.bing.com >nul 2>nul
if errorlevel 1 (
    echo %date% %time% 等待网络连接... >> "%log_file%"
    timeout /t 10 /nobreak >nul
    goto check_network
) else (
    echo %date% %time% 网络已连接，开始下载壁纸 >> "%log_file%"
    python -X utf8 "E:\Proj\WallPaper\bing_wallpaper.py" >> "%log_file%" 2>&1
    echo ============================================== >> "%log_file%"
) 