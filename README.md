# VLC_CAMERA_AUTOMATION
Automating VlC media player to play RSTP stream from a ipcamera. Steps inlcude:

- Opening vlc media player.
- Entering rstp url.
- Entering Camera Credentials.

# Steps to initialize

1) Add credentials for camera account in .env file
```
CAMERA_URL=rtsp://192.168.1.xx/stream
CAMERA_NAME=xxxxx
CAMERA_PASSWORD=xxx
```

2) Install dependencies
```
pip install -r requirements.txt
```

3) Run 
```
python app.py
```
