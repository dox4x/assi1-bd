# Use the official Ubuntu image as the base
FROM ubuntu:20.04

# Update the package list and install necessary packages
RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip

# Install Python packages using pip
RUN pip3 install pandas numpy matplotlib seaborn scikit-learn scipy

# Set the working directory in the container
WORKDIR /home/doc-bd-a1

COPY games.csv .
# Open the bash shell upon container startup
CMD [ "bash" ]

# Expose port 8080 if your application requires it (optional)
EXPOSE 8080
