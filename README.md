# EdgeVR

WIP.

## FFmpeg360

1. Clone git repo from FFmpeg360 `git clone https://github.com/bingsyslab/ffmpeg360.git`
2. Open the folder `cd ffmpeg360`
3. Check out the commit `git checkout 70d1a945213a298c588486270cac46196bd338d3`
4. Apply diff file `git apply ../ffmpeg360.diff`

## ijkplayer

1. Clone git repo from ijkplayer `git clone https://github.com/bilibili/ijkplayer.git`
2. Open the folder `cd ijkplayer`
3. Run `./init-android.sh`
4. Check out the commit `git checkout cced91e3ae3730f5c63f3605b00d25eafcf5b97b`
5. Apply diff file `git apply ../ijkplayer.patch`
6. Open ffmpeg folder `cd android/contrib/ffmpeg-armv7a`
7. Apply diff file `git apply ../../../../ijkplayer_ffmpeg.diff`
8. Follow instructions in ijkplayer
