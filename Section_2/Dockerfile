# Getting base image from postgres
FROM postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=car-dealership

# https://stackoverflow.com/questions/38713597/create-table-in-postgresql-docker-image
COPY create_database.sql /docker-entrypoint-initdb.d/