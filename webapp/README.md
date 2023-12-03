# Webapp
Webapp to visualize some of our results for a non-specialists.
The app is hosted at [https://parlerment.azurewebsites.net/](https://parlerment.azurewebsites.net)

![Webapp UI](/webapp/webapp_ui.png)

## Installation

Before installation, ensure you have at least node.js version 20 installed. 

```bash
# Clone the repository
git clone https://github.com/sstratemeier/parlerStadtparlament.git

# Navigate to the repository directory
cd parlerStadtparlament

# Install npm packages
npm i
```

## Development
Run the following command to start a local development server:


```bash
# Run vite live server
npm run dev
```

The app will be available at http://localhost:80.



## Deploying to production

To update the online version:

- Push changes to the main branch.
- Or run npm run deploy. Ensure you are logged in with Azure (az login and az acr login --name stadtparlamentsdashboardregistry).
