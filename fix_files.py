
import os
import shutil
import sys

def fix_files():
    base_dir = r"d:\multiagent\multi-agent-adk-assistant"
    
    # file 1: docs/images/streamlit_ui.png.png -> docs/images/streamlit_ui.png
    src1 = os.path.join(base_dir, "docs", "images", "streamlit_ui.png.png")
    dst1 = os.path.join(base_dir, "docs", "images", "streamlit_ui.png")
    
    if os.path.exists(src1):
        print(f"Renaming {src1} to {dst1}")
        try:
            if os.path.exists(dst1):
                os.remove(dst1)
            os.rename(src1, dst1)
            print("Success 1")
        except Exception as e:
            print(f"Error 1: {e}")
    else:
        print(f"Source 1 not found: {src1}")

    # file 2: docs/swagger_ui.png -> docs/images/swagger_ui.png
    src2 = os.path.join(base_dir, "docs", "swagger_ui.png")
    dst2 = os.path.join(base_dir, "docs", "images", "swagger_ui.png")
    
    if os.path.exists(src2):
        print(f"Moving {src2} to {dst2}")
        try:
            if os.path.exists(dst2):
                os.remove(dst2)
            shutil.move(src2, dst2)
            print("Success 2")
        except Exception as e:
            print(f"Error 2: {e}")
    else:
        print(f"Source 2 not found: {src2}")

if __name__ == "__main__":
    fix_files()
