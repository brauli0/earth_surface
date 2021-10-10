# How to

### You only need to have Docker installed. These are the steps:

Build image:
```
docker build -t earthsurface .
```

Run container (and wait a few seconds):
```
docker run -p 80:80 -d --name server earthsurface
```

Test it:
```
curl "http://localhost/getsurface?lat=42.985699&lon=-7.837807"
```

Stop container:
```
docker stop server
```

Remove all containers:
```
docker container prune
```

Remove image:
```
docker rmi earthsurface
```