import os
import shutil

def setup_docs():
    base_dir = r"d:\multiagent\multi-agent-adk-assistant"
    docs_dir = os.path.join(base_dir, "docs")
    images_dir = os.path.join(docs_dir, "images")
    
    source_image = r"C:\Users\bhati\.gemini\antigravity\brain\tempmediaStorage\media__1770739686403.png"
    
    print(f"Creating directories: {images_dir}")
    os.makedirs(images_dir, exist_ok=True)
    
    if os.path.exists(source_image):
        print(f"Copying image from {source_image}")
        shutil.copy(source_image, os.path.join(images_dir, "streamlit_ui.png"))
        shutil.copy(source_image, os.path.join(images_dir, "swagger_ui.png"))
        print("Images copied successfully.")
    else:
        print(f"Source image not found at {source_image}")
        # Create dummy images if source is missing to avoid "file not found" errors
        with open(os.path.join(images_dir, "streamlit_ui.png"), "wb") as f:
            f.write(b"")
        with open(os.path.join(images_dir, "swagger_ui.png"), "wb") as f:
            f.write(b"")
        print("Created placeholder images.")

    # Verify
    if os.path.exists(images_dir):
        print("Directory setup verified.")
        print("Contents:", os.listdir(images_dir))
    else:
        print("Directory creation failed.")

if __name__ == "__main__":
    setup_docs()
