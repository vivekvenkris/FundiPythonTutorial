# FundiPythonTutorial
Python hands-on session for the 2021 Fundi tutorials

In this tutorial, we will discuss some of the common and useful packages for analysis of time-domain radio data. All the required software for the tutorial is bundled up into a docker/singularity container. You are free to use either and you will find instructions on how to use it below:

## Use Docker

If you are using docker, note that you will need a docker installation on your laptop as you will likely not have permissions to run docker on the MPIfR machines. Assuming you have a working installation, which you can set up from [here](https://docs.docker.com/get-docker/), the easiest way to use it is to download the image from docker hub by doing:

```
docker pull vivekvenkris/fundi_python_tutorial:latest
```

In case you do not have a good internet connection and wish to build it from scratch, you can clone [this](https://github.com/vivekvenkris/pulsar_folder) repository, `cd` to the repository  and run

```
docker build -t fundi_python_tutorial .
```

Once this is done, you can run the container by doing:

```
docker run -p <your_port_number>:<your_port_number> -v <repo_location>:/<repo_location> vivekvenkris/fundi_python_tutorial
```


## Use Singularity

If you are using singularity, you can use either your personal machine or one of the MPIfR machines that has singularity installed (E.g: dogmatix0). You can install singularity on your local machine using instructions from [here](https://sylabs.io/guides/3.0/user-guide/installation.html). The singularity image can either be downloaded from google drive [here](https://drive.google.com/drive/folders/1ASX0Qhl7V39wlefxK_FGmo7luV648Chc?usp=sharing) or from the FPRA meerkat partition here: `/fpra/mkat/01/users/vivek/singularity_images/vivekvenkris_fundi_python_tutorial-2021-10-03-5dd4a33d25e1.sif`. Note that not all will have permissions to access this directory, so revert to downloading from Google Drive if you cant download from here. 

Once you have downloaded or copied the singularity image, you can run it by doing 
```
singularity shell -B <repo_location>:/<repo_location> /fpra/mkat/01/users/vivek/singularity_images/vivekvenkris_fundi_python_tutorial-2021-10-03-5dd4a33d25e1.sif
```
## Using Jupyter notebook

Once you are inside your docker or singularity container, you can start a jupyter notebook by doing the following

```
cd <repo_location>
jupyter lab --port <your_port_number> --no-browser 
```

Your port number here and everywhere else can in principle be anything (although needs to be the same everywhere, but since there might be unconscious overlaps, please choose a random number between 10000 and 11000.

If you are running docker, you need to also add `--allow_root --ip 0.0.0.0` to your jupyter lab command. 
If you are running singularity, you need to forward the port you are using to your localhost. You can do that by requesting a port forward by doing:
```
ssh <your_user_name>@<your_machine> -J <gateway machine> -L <your_port_number>:localhost:<your_port_number>
```
For instance, `ssh vkrishnan@dogmatix1 -J portal.mpifr-bonn.mpg.de -L 10034:localhost:10034` forwards the port `10034` from `dogmatix1` to my localhost (my laptop) via the `portal` gateway. 
