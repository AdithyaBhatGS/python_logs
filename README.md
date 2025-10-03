# python_logs
A simple python script to log every 3 seconds. The main goal is to test the concept of named volumes in docker.

## Steps:
1. Fork/clone the above repo using
   - ```bash
     git clone https://github.com/AdithyaBhatGS/python_logs/
2. Go into the cloned repository
3. Build the image
   - ```bash
     docker build -t <img_name> .
4. Run the image in background by mounting it to a named volume
   - ```bash
     docker run -d --name <container_name> -v <host_path>:/app/logs <img_name>
5. Check the status of the container
   - ```bash
     docker ps -a
6. Get into the container and check the logs
   - ```bash
     docker exec -it py_log_container /bin/bash
   - Go to the /app/logs
     - ```bash
       cd /app/logs
     - Check the log file by **cat** command
7. Inspect the path of the named volume
   - ```bash
     docker volume inspect <host_path>
   - Now just check the Mountpoint
     - "Mountpoint": "/var/lib/docker/volumes/feyman/_data"
8. Now stop and remove the container
   - ```bash
     docker stop <container_name> && docker rm <container_name>
9. Go to the named volume
   - ```bash
     cd ~/var/lib/docker/volumes/feyman/_data
   - ```bash
     cat file_name.log
10. Since the data persists we can confirm that the volumes are working perfectly
