# Instructions for Running the Program in Docker

After making changes to your code, follow these steps to rebuild the Docker image and run the container:

1. **Rebuild the Docker Image**:

   ```bash
   docker build -t deidentify-image .
   ```

   This command creates a new Docker image with your latest code changes.

2. **Run the Container**:

   ```bash
   docker run -v <path_to_directory>/output:/app/output deidentify-image

   ```

   The `--rm` flag ensures the container is removed after it stops, keeping your system clean.


# Dependencies

This program requires that you have `Python 3` or later, as well as the `pandas` and `openpyxl` libraries installed. 