![Screenshot from 2023-01-13 11-23-03](https://user-images.githubusercontent.com/30196830/212247524-3cc7d7a7-82a2-4383-bf3e-21d895874249.png)

# VLC_CAMERA_AUTOMATION
Automating VlC media player to play RSTP stream from a ipcamera. Steps inlcude:

- Opening vlc media player.
- Entering rstp url.
- Entering Camera Credentials.

![Screenshot from 2023-01-13 11-19-55](https://user-images.githubusercontent.com/30196830/212247102-0bd73765-64db-4cd9-85d8-d0a01996e50c.png)

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

Goals

- [ ] Create a executable for linux
- [ ] Create a executable for windows


