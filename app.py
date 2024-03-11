##
from pathlib import Path
import streamlit as st
import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# setting page layout
st.set_page_config(
    page_title="Interactive Interface for YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
    )
## 设置一个主页标题
st.title("用YOLOv8实现人脸检测")
## 在侧边栏（sidebar）部分添加一个标题（header）
st.sidebar.header("aaa")
## 选择模型
task_type = st.sidebar.selectbox(
    "选择任务",
    ["目标检测","目标分割"]
)
## ---------------------------------- ##
## 任务条件判断
model_type = None
if task_type == "目标检测":
    model_type = st.sidebar.selectbox(
    "请选择模型",
    config.DETECTION_MODEL_LIST
    )

elif task_type == "目标分割":
    model_type = st.sidebar.selectbox(
    "请选择模型",
    config.SEGMENTION_MODEL_LIST
    )
# 其他任务类别
# elif task_type == "XXX":
#     model_type = st.sidebar.selectbox(
#     "请选择模型",
#     config.XXX
#     )
else:
    st.error("这里只有检测和分割功能哦")
## ---------------------------------- ##
## 创建一个置信度的滑动条
confidence = st.sidebar.slider(
    "请选择一个置信度",
    30,
    100,
    50
)
confidence = float(confidence)/100
model_path = ""
if model_type:
    model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
else:
    st.error("Please Select Model in Sidebar")
## 上传一个模型
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Unable to load model. Please check the specified path: {model_path}")
## 上传被检测图片、视频模块
st.sidebar.header("打开图片或视频")
source_selectbox = st.sidebar.selectbox(
    "选择文件类型",
    config.SOURCES_LIST
)
##
source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(confidence, model)
else:
    st.error("Currently only 'Image' and 'Video' source are implemented")