#/bin/bash

read -p "Enter jsonweb version :" NEW_VERSION
podman build -t jsonweb:${NEW_VERSION} .

podman tag jsonweb:${NEW_VERSION} git.anuraj.site/anurajk/jsonweb:${NEW_VERSION}
podman tag jsonweb:${NEW_VERSION} git.anuraj.site/anurajk/jsonweb:latest


podman push git.anuraj.site/anurajk/jsonweb:${NEW_VERSION}
podman push git.anuraj.site/anurajk/jsonweb:latest