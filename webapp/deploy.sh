 docker build -t parla-stadtparlament-webapp .
 docker tag parla-stadtparlament-webapp stadtparlamentsdashboardregistry.azurecr.io/parla-stadtparlament-webapp:latest
 docker push stadtparlamentsdashboardregistry.azurecr.io/parla-stadtparlament-webapp:latest