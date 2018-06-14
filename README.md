Dockerize YOLO Object Detection Service
===
Kenny Hsieh

![](https://i.imgur.com/6vAW0iM.png =500x)

## Usage
### Build from Dockerfile

```console=
docker build -t dockerize-yolo-service .
```

### Pull from Docker Hub
```console=
# Pull from Docker Hub
docker pull kennyhsieh1111/dockerize-yolo-service

# Start the Container with Images
docker run -d -p 5000:5000 --name yolo_service kennyhsieh1111/dockerize-yolo-service

# Open localhost:5000 in browser
```

## Interface

![](https://i.imgur.com/kpvRc75.jpg =500x)