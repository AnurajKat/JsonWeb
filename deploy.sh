#/bin/bash

echo "Enter jsonweb version"
read NEW_VERSION

podman build -t jsonweb:${NEW_VERSION} .

podman tag jsonweb:${NEW_VERSION} git.anuraj.site/anurajk/jsonweb:${NEW_VERSION}

podman push git.anuraj.site/anurajk/jsonweb:${NEW_VERSION}