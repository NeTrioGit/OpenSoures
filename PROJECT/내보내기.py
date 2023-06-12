from ultralytics import YOLO

# Load a model
model = YOLO('/opt/homebrew/runs/detect/train2/weights/best.pt')  # load a custom trained

# Export the model
model.export(format='tfjs')

# PyTorch	-	yolov8n.pt	✅	-
# TorchScript	torchscript	yolov8n.torchscript	✅	imgsz, optimize
# ONNX	onnx	yolov8n.onnx	✅	imgsz, half, dynamic, simplify, opset
# OpenVINO	openvino	yolov8n_openvino_model/	✅	imgsz, half
# TensorRT	engine	yolov8n.engine	✅	imgsz, half, dynamic, simplify, workspace
# CoreML	coreml	yolov8n.mlmodel	✅	imgsz, half, int8, nms
# TF SavedModel	saved_model	yolov8n_saved_model/	✅	imgsz, keras
# TF GraphDef	pb	yolov8n.pb	❌	imgsz
# TF Lite	tflite	yolov8n.tflite	✅	imgsz, half, int8
# TF Edge TPU	edgetpu	yolov8n_edgetpu.tflite	✅	imgsz
# TF.js	tfjs	yolov8n_web_model/	✅	imgsz
# PaddlePaddle	paddle	yolov8n_paddle_model/	✅	imgsz