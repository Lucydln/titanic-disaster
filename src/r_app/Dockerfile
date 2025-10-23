# src/r_app/Dockerfile

FROM r-base:4.3.1

# Set working directory inside the container
WORKDIR /app

# Copy installation script and install packages
COPY install_packages.R .
RUN Rscript install_packages.R

# Copy your R script
COPY main.R .

# Run your R script by default when the container starts
CMD ["Rscript", "main.R"]
