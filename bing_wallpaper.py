import os
import json
import requests
from datetime import datetime, timedelta
import glob
import sys


# 配置变量
CONFIG = {
    "download_dir": "E:\\WallPapers",  # 默认下载目录
    "keep_images": 5,  # 保留最新的图片数量
    "check_days": 5    # 检查最近几天的图片（包括今天）
}

class BingWallpaperDownloader:
    def __init__(self, download_dir=None):
        self.bing_api = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx={idx}&n=1&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
        self.bing_url = "https://cn.bing.com"
        # 使用传入的下载目录或配置中的默认值
        self.download_dir = download_dir or CONFIG["download_dir"]
        
        # 创建下载目录（如果不存在）
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
            print(f"创建下载目录: {self.download_dir}")
    
    def cleanup_old_images(self):
        """清理旧图片，只保留最新的几张"""
        # 获取所有jpg文件
        files = glob.glob(os.path.join(self.download_dir, "*.jpg"))
        # 按文件名排序（因为文件名是日期）
        files.sort(reverse=True)
        
        # 删除多余的文件
        if len(files) > CONFIG["keep_images"]:
            for file in files[CONFIG["keep_images"]:]:
                try:
                    os.remove(file)
                    print(f"删除旧图片: {os.path.basename(file)}")
                except Exception as e:
                    print(f"删除文件失败 {file}: {str(e).encode('utf-8').decode('utf-8')}")
    
    def get_wallpaper_url(self, idx=0):
        """获取指定日期的壁纸URL，idx为0表示今天，1表示昨天，以此类推"""
        try:
            response = requests.get(self.bing_api.format(idx=idx))
            response.encoding = 'utf-8'  # 设置响应编码为utf-8
            data = response.json()
            image_data = data["images"][0]
            
            # 打印完整的图片数据信息
            print(f"\n=== 图片数据信息 (idx={idx}) ===")
            for key, value in image_data.items():
                try:
                    print(f"{key}: {value}")
                except UnicodeEncodeError:
                    # 如果遇到编码错误，尝试使用UTF-8编码
                    print(f"{key}: {str(value).encode('utf-8').decode('utf-8')}")
            print("==================\n")
            
            url = self.bing_url + image_data["url"]
            print(f"获取到的壁纸URL: {url}")
            return url, image_data["enddate"]
        except Exception as e:
            print(f"获取壁纸URL时出错: {str(e).encode('utf-8').decode('utf-8')}")
            return None, None
    
    def download_wallpaper(self, idx=0):
        """下载指定日期的壁纸"""
        wallpaper_url, enddate = self.get_wallpaper_url(idx)
        if not wallpaper_url:
            return False
        
        # 检查文件是否已存在
        filename = f"{enddate}.jpg"
        file_path = os.path.join(self.download_dir, filename)
        if os.path.exists(file_path):
            print(f"图片已存在，跳过下载: {filename}")
            return True
        
        try:
            # 获取图片内容
            print(f"开始下载壁纸...")
            response = requests.get(wallpaper_url, stream=True)
            response.raise_for_status()
            
            print(f"保存文件名: {filename}")
            print(f"完整保存路径: {file_path}")
            
            # 保存图片
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            print(f"壁纸下载完成!")
            return True
            
        except Exception as e:
            print(f"下载壁纸时出错: {str(e).encode('utf-8').decode('utf-8')}")
            return False
    
    def check_and_download_recent(self):
        """检查并下载最近几天的图片"""
        print(f"开始检查最近 {CONFIG['check_days']} 天的图片...")
        for idx in range(CONFIG["check_days"]):
            print(f"\n检查 {idx} 天前的图片...")
            self.download_wallpaper(idx)
        
        # 下载完成后清理旧图片
        self.cleanup_old_images()

def main():
    # 你可以在这里指定自定义的下载目录
    # 例如: custom_dir = "D:\\WallPapers"
    # downloader = BingWallpaperDownloader(custom_dir)
    downloader = BingWallpaperDownloader()
    downloader.check_and_download_recent()

if __name__ == "__main__":
    main() 