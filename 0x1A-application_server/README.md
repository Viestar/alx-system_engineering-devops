>>> ![ssh](./assets/Screenshot%20from%202023-10-18%2002-09-03.png)

## Description

The goal of this project is to install an application server (gunicorn) on our own servers and serve dynamic content with it.

# Table of contents

Task  | Code | Description
----- | ------ | -----------
[0x02] | [Serve a page with Nginx](./2-app_server-nginx_config) | Nginx config file setup to serve /airbnb-onepage/
[0x03] | [Add a route with query parameters](./3-app_server-nginx_config) | Nginx config file setup to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(integer) to a Gunicorn listening on port 5001
