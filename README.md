Dockerize YOLO Object Detection Service
===
Kenny Hsieh

<p align="center">
  <img src="https://i.imgur.com/6vAW0iM.png" width="500" />
</p>

## Usage
### Build from Dockerfile

```bash
docker build -t dockerize-yolo-service .
```

### Pull from Docker Hub
```bash
# Pull from Docker Hub
docker pull kennyhsieh1111/dockerize-yolo-service

# Start the Container with Images
docker run -d -p 5000:5000 --name yolo_service kennyhsieh1111/dockerize-yolo-service

# Open localhost:5000 in browser
```

## Interface

<p align="center">
  <img src="https://i.imgur.com/kpvRc75.jpg" width="500" />
  <img src="https://i.imgur.com/7jgbS0l.jpg" width="500" />
</p>