#!/usr/bin/env python3
"""
安装arkitect包的脚本
"""
import subprocess
import sys
import os
import tempfile
import shutil

def install_arkitect():
    """安装arkitect包"""
    print("开始安装arkitect包...")
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    print(f"临时目录: {temp_dir}")
    
    try:
        # 克隆仓库
        print("克隆ai-app-lab仓库...")
        subprocess.run([
            "git", "clone", 
            "https://github.com/volcengine/ai-app-lab.git",
            temp_dir
        ], check=True)
        
        # 切换到指定版本
        print("切换到v0.2.4版本...")
        subprocess.run([
            "git", "checkout", "v0.2.4"
        ], cwd=temp_dir, check=True)
        
        # 安装包
        print("安装arkitect包...")
        subprocess.run([
            sys.executable, "-m", "pip", "install", "."
        ], cwd=temp_dir, check=True)
        
        print("arkitect安装成功!")
        
    except subprocess.CalledProcessError as e:
        print(f"安装失败: {e}")
        sys.exit(1)
    finally:
        # 清理临时目录
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print("清理临时文件完成")

if __name__ == "__main__":
    install_arkitect() 