# Downloading this Code

To download this code, you can utilize the following command:

```bash
git clone https://github.com/ianhajra/DeIdentify.git
```

Ensure this is run in the location you want the DeIdentify folder containing this repository to live.

# Instructions for Running the Program via Python

1. **Ensure Python and Dependencies are Installed**:

Please see `Dependencies` below for information on what is required.

2. **Utilize Python**

   ```bash
   python deid.py
   ```

# Instructions for Running the Program inside a Docker container

The following instructions assume that you have Docker installed, and are more intended for anyone doing development on this repository.

After making changes to your code, or to simply run the program, follow these steps to build the Docker image and run the container:

1. **Rebuild the Docker Image**:

   ```bash
   docker build -t deidentify-image .
   ```

   This command creates a new Docker image with your latest code changes.

2. **Run the Container**:

   ```bash
   docker run -v <path_to_directory>/output:/app/output deidentify-image

   ```

# Dependencies

This program requires that you have `Python 3` or later, as well as the `pandas` and `openpyxl` libraries installed. 