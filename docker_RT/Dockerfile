# YOLOv5 🚀 by Ultralytics, AGPL-3.0 license
# Builds ultralytics/yolov5:latest image on DockerHub https://hub.docker.com/r/ultralytics/yolov5
# Image is CUDA-optimized for YOLOv5 single/multi-GPU training and inference

# Start FROM PyTorch image https://hub.docker.com/r/pytorch/pytorch
#FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
ARG CUDA_MAJOR_VERSION
ARG CUDA_MINOR_VERSION
ENV CUDA_MAJOR_VERSION=11
ENV CUDA_MINER_VERSION=8
ENV CUDA_VERSION=$CUDA_MAJOR_VERSION.$CUDA_MINER_VERSION
RUN update-alternatives --set cuda /usr/local/cuda-11.8

# Downloads to user config dir
ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/

# Install linux packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN TZ=Etc/UTC apt-get install -y tzdata
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y gcc git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg

# Security updates
# https://security.snyk.io/vuln/SNYK-UBUNTU1804-OPENSSL-3314796
RUN apt upgrade -y openssl

# Create working directory
#RUN rm -rf /usr/src/weld_rt && mkdir -p /yolov5/weld_rt
RUN git clone https://github.com/ultralytics/yolov5.git
WORKDIR ./yolov5
RUN mkdir weld_rt

RUN mkdir  /yolov5/weld_rt/data_rt
RUN mkdir  /yolov5/weld_rt/data_rt/images
RUN mkdir  /yolov5/weld_rt/data_rt/json 
RUN mkdir  /yolov5/weld_rt/data_rt/labels
RUN mkdir  /yolov5/weld_rt/data_rt/labels2

RUN mkdir  /yolov5/weld_rt/custom_rt
RUN mkdir  /yolov5/weld_rt/custom_rt/images
RUN mkdir  /yolov5/weld_rt/custom_rt/json 
RUN mkdir  /yolov5/weld_rt/custom_rt/labels

COPY test/images/*.jpg /yolov5/weld_rt/data_rt/images
COPY test/validation/*.json /yolov5/weld_rt/data_rt/json
COPY data_transform.py /yolov5/weld_rt/data_rt
COPY custom_data_transform.py /yolov5/weld_rt/custom_rt

#COPY txt.py /yolov5
COPY metrics.py /yolov5
COPY val.py /yolov5
COPY best.pt /yolov5
COPY segment/metrics.py /yolov5/weld_rt


COPY dataRT.yaml /yolov5/weld_rt
COPY custom_dataRT.yaml /yolov5/weld_rt
COPY requirements.txt /yolov5/weld_rt

COPY entrypoint.sh /yolov5
#RUN chmod +x /yolov5/entrypoint.sh

# 엔트리포인트 설정
#CMD ["entrypoint.sh"]

# Copy contents
#COPY . /usr/src/app

# Install pip packages
RUN apt-get update && apt-get install -y python3-all python3-pip
RUN python3 -V
#RUN pip install --no-cache -r requirements.txt albumentations comet gsutil notebook \
#    coremltools onnx onnx-simplifier onnxruntime 'openvino-dev>=2023.0'
    # tensorflow tensorflowjs \

# Set environment variables
ENV OMP_NUM_THREADS=1

# Cleanup
ENV DEBIAN_FRONTEND teletype
RUN pip install -r /yolov5/weld_rt/requirements.txt
#CMD ["pip", "install", "-r", "/yolov5/weld_rt/requirements.txt"]
#ENTRYPOINT [ "executable" ]
# Usage Examples -------------------------------------------------------------------------------------------------------

# Build and Push
# g

# Pull and Run
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all $t

# Pull and Run with local directory access
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all -v "$(pwd)"/datasets:/usr/src/datasets $t

# Kill all
# sudo docker kill $(sudo docker ps -q)

# Kill all image-based
# sudo docker kill $(sudo docker ps -qa --filter ancestor=ultralytics/yolov5:latest)

# DockerHub tag update
# t=ultralytics/yolov5:latest tnew=ultralytics/yolov5:v6.2 && sudo docker pull $t && sudo docker tag $t $tnew && sudo docker push $tnew

# Clean up
# sudo docker system prune -a --volumes

# Update Ubuntu drivers
# https://www.maketecheasier.com/install-nvidia-drivers-ubuntu/

# DDP test
# python -m torch.distributed.run --nproc_per_node 2 --master_port 1 train.py --epochs 3

# GCP VM from Image
# docker.io/ultralytics/yolov5:latest
