 docker build build -t stadtparlaments-dashboard .
 docker tag stadtparlaments-dashboard stadtparlamentsdashboardregistry.azurecr.io/stadtparlaments-dashboard:latest
 docker push stadtparlamentsdashboardregistry.azurecr.io/stadtparlaments-dashboard:latest