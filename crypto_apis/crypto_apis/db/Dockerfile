FROM mcr.microsoft.com/mssql/server:2019-latest


USER root
RUN mkdir /var/opt/sqlserver
RUN chown mssql /var/opt/sqlserver

ENV MSSQL_BACKUP_DIR="/var/opt/sqlserver"
ENV MSSQL_DATA_DIR="/var/opt/sqlserver"
ENV MSSQL_LOG_DIR="/var/opt/sqlserver"
USER mssql

CMD /opt/mssql/bin/sqlservr
