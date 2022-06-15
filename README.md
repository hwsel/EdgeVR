# EdgeVR

In this project, we developed an edge offloading-based approach to minimize the on-device computation and the power consumption in the live VR streaming system. Please read and refer to our recently accepted NOSSDAV '22 paper for more details about this project: 

> Zichen Zhu, Xianglong Feng, Zhongze Tang, Nan Jiang, Tian Guo, Lisong Xu, and Sheng Wei, “Power-Efficient Live Virtual Reality Streaming Using Edge,” Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV), Jun. 2022.

## System Setup

### Edge Server

#### Renderer and Viewport Predictor

1. Clone the repo from FFmpeg360 `git clone https://github.com/bingsyslab/ffmpeg360.git`
2. Open the folder `cd ffmpeg360`
3. Check out the commit `git checkout 70d1a945213a298c588486270cac46196bd338d3`
4. Apply changes from our work `git apply ../renderer_and_viewport_predictor.diff`

#### RTMP Server

1. Install Dokcer with instructions from Docker: https://docs.docker.com/engine/install/
2. Run the RTMP server `docker run --name nginx-rtmp -p 1935:1935 -p 8080:8080 -d jasonrivers/nginx-rtmp`

### Client - Video Player

1. Clone git repo from ijkplayer `git clone https://github.com/bilibili/ijkplayer.git`
2. Open the folder `cd ijkplayer`
3. Run `./init-android.sh`
4. Check out the commit `git checkout cced91e3ae3730f5c63f3605b00d25eafcf5b97b`
5. Apply diff file `git apply ../ijkplayer.patch`
6. Open ffmpeg folder `cd android/contrib/ffmpeg-armv7a`
7. Apply diff file `git apply ../../../../ijkplayer_ffmpeg.diff`
8. Follow instructions in ijkplayer

### Dataset

Please download from https://wuchlei-thu.github.io/

## Cite Our Work

Zichen Zhu, Xianglong Feng, Zhongze Tang, Nan Jiang, Tian Guo, Lisong Xu, and Sheng Wei, “Power-Efficient Live Virtual Reality Streaming Using Edge,” Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV), Jun. 2022.
