mjpg_streamer -i "input_uvc.so -d /dev/video0 -yuv -r 640x480 -f 15" -o "output_http.so -p 8080 -w /www/webcam" &

