docker build --platform="linux/amd64" -f Dockerfile --tag resumer-analyzer:3.0.0 .
docker tag resumer-analyzer:3.0.0 chan4lk/resumer-analyzer:3.0.0-linux
docker push chan4lk/resumer-analyzer:3.0.0-linux