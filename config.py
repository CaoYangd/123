## 这是一个配置文件，包含了项目的配置信息，包括模型的列表和路径等。

from pathlib import Path
import sys
# 获取当前文件（config.py）的完整绝对路径，F:\2023\streamlit\config.py
file_path = Path(__file__).resolve()
print(file_path)
# 获取当前文件（config.py）的父级（上一级）路径，F:\2023\streamlit
root_path = file_path.parent
print(root_path)
# 为root_path加一个判断，如果root_path不在sys.path列表中，将root_path添加到sys.path列表。
# 这样假设config这个配置文件不在root_path路径下，可以将其添加进去
if root_path not in sys.path:
    sys.path.append(str(root_path))

## 计算`root_path`相对于当前工作目录的相对路径。如果`root_path`就是当前工作目录，那么相对路径就是`.`
Root = root_path.relative_to(Path.cwd())
print("root is：",Root)
##

DETECTION_MODEL_LIST = [
    "yolov8n.pt",
    "yolov8s.pt",
    "yolov8m.pt",
    "yolov8l.pt",
    "yolov8x.pt"]
SEGMENTION_MODEL_LIST = [
    "yolov8n.st",
    "yolov8s.st",
    "yolov8m.st",
    "yolov8l.st",
    "yolov8x.st"]

## 检测模型路径
DETECTION_MODEL_DIR = Root / 'weights' / 'detection'
YOLOv8n = DETECTION_MODEL_DIR / "yolov8n.pt"
YOLOv8s = DETECTION_MODEL_DIR / "yolov8s.pt"
YOLOv8m = DETECTION_MODEL_DIR / "yolov8m.pt"
YOLOv8l = DETECTION_MODEL_DIR / "yolov8l.pt"
YOLOv8x = DETECTION_MODEL_DIR / "yolov8x.pt"

## 分割模型路径
SEGMENTION_MODEL_DIR = Root / 'weights' / 'segmention'
print(DETECTION_MODEL_DIR)

# 源文件
SOURCES_LIST = ["Image", "Video", "Webcam"]