# Use an official Python runtime as an image
FROM python:3.7.10

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
# optional: for bcp and sqlcmd
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN export PATH="$PATH:/opt/mssql-tools/bin"
RUN export PATH="$PATH:/opt/mssql-tools/bin"

RUN apt-get install -y unixodbc-dev
RUN apt-get install -y libgssapi-krb5-2

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY . /app
# CMD [ "./start.sh" ]
# CMD ["/bin/bash"]