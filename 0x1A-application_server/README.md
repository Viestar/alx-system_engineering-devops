>>> ![ssh](./assets/Screenshot%20from%202023-10-18%2002-09-03.png)

## Description

The goal of this project is to install an application server (gunicorn) on our own servers and serve dynamic content with it.

# Table of contents

Task  | Code | Description
----- | ------ | -----------
[0x02] | [Serve a page with Nginx](./2-app_server-nginx_config) | Nginx config file setup to serve /airbnb-onepage/
[0x03] | [Add a route with query parameters](./3-app_server-nginx_config) | Nginx config file setup to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(integer) to a Gunicorn listening on port 5001.
[0x04] | [Let's do this for your API](./4-app_server-nginx_config) | Nginx config file setup so that the route /api/ points to a Gunicorn instance listening on port 5002 basing on what we built for AirBnB clone v3 - RESTful API on web-01.
[0x05] | [5-app_server-nginx_config](./5-app_server-nginx_config) | Nginx config file  so that it properly serves the static assets found in web_dynamic/static/ and the route / points to the Gunicorn instance.
