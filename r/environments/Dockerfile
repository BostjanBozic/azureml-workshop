FROM mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu18.04

RUN conda install -c r -y pip=20.1.1 openssl=1.1.1c r-base rpy2 && \
  conda install -c conda-forge -y mscorefonts && \
    conda clean -ay && \
    pip install --no-cache-dir azureml-defaults tensorflow-gpu keras
    
ENV TAR="/bin/tar"

RUN R -e "install.packages(c('remotes', 'reticulate', 'optparse', 'caret', 'keras', 'DAAG'), dependencies = TRUE, repos = 'https://cloud.r-project.org/')"
RUN R -e "remotes::install_github('https://github.com/Azure/azureml-sdk-for-r')"
