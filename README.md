# FundiPythonTutorial
Python hands-on session for the 2021 Fundi tutorials

In this tutorial, we will discuss some of the common and useful packages for analysis of time-domain radio data. All the required software for the tutorial is bundled up into a docker/singularity container. You are free to use either and you will find instructions on how to use it below:

If you are using docker, note that you will need a docker installation on your laptop as you will likely not have permissions to run docker on the MPIfR machines. Assuming you have a working installation, which you can set up from [https://docs.docker.com/get-docker/][here], the easiest way to use it is to download the image from docker hub by doing:

```

docker pull vivekvenkris/fundi_python_tutorial:latest

```

In case you do not have a good internet connection and wish to build it from scratch, you can clone [https://github.com/vivekvenkris/pulsar_folder][this] repository, `cd` to the repository  and run

```
docker build -t fundi_python_tutorial .

```

Once this is done, you can run the container by doing:

```

docker run -p 8888:8888 -v <repo_location>:/<repo_location> vivekvenkris/fundi_python_tutorial

```
