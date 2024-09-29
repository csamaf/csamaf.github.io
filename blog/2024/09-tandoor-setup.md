---
date: "2024-09-29"
category: today-i-learned
tags: Docker, Tandoor, Traefik
author: Felix
---

# Running Tandor with Traefik and rootless docker

# What's working

- start with
  ```bash
  wget https://raw.githubusercontent.com/vabene1111/recipes/develop/docs/install/docker/traefik-nginx/docker-compose.yml
  wget https://raw.githubusercontent.com/vabene1111/recipes/develop/.env.template -O .env
  ```
- Postgres does not play along with rootless docker (known issue, creates files as non-user on the host)
- replace postgres by sqlite (single file mount)

Final `.env` file is
```
SECRET_KEY=<some stuff here>
DB_ENGINE=django.db.backends.sqlite3
POSTGRES_HOST=db_recipes
POSTGRES_DB=djangodb
POSTGRES_PORT=5432
POSTGRES_USER=djangouser
POSTGRES_PASSWORD=<some stuff here>
```

Final `docker-compose.yml` is
```
services:
  web_recipes:
    restart: always
    image: vabene1111/recipes
    volumes:
      - staticfiles:/opt/recipes/staticfiles
      # Do not make this a bind mount, see https://docs.tandoor.dev/install/docker/#volumes-vs-bind-mounts
      - nginx_config:/opt/recipes/nginx/conf.d
      - mediafiles:/opt/recipes/mediafiles
      # We cannot make this a volume, as we need to mount a single file
      - /<path to your>/djangodb:/opt/recipes/djangodb
    networks:
      - recipes
    env_file:
      - .env

  nginx_recipes:
    image: nginx:mainline-alpine
    restart: always
    volumes:
      # Do not make this a bind mount, see https://docs.tandoor.dev/install/docker/#volumes-vs-bind-mounts
      - nginx_config:/etc/nginx/conf.d:ro
      - staticfiles:/static:ro
      - mediafiles:/media:ro
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.recipes.rule=Host(`<your hostname here>`)"
      - "traefik.http.routers.recipes.entrypoints=websecure"
      - "traefik.http.routers.recipes.tls=true"
      - "traefik.docker.network=traefik-net"
    depends_on:
      - web_recipes
    networks:
      - recipes
      - traefik-net
    env_file:
      - .env

networks:
  recipes:
  traefik-net:
    external: true
    name: traefik-net

volumes:
  nginx_config:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /<path to your>/nginx_config
  staticfiles:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /<path to your>/staticfiles
  mediafiles:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /<path to your>/mediafiles
```

## What's not working

Using Nextcloud as OAuth provider does not work at the moment.

- The required redirect URL to be entered in Nextcloud is undocumented.
  Using `https://<your hostname>/accounts/nextcloud/login/callback/` leads to a callback to Tandoor, but I still get an `Social Network Login Failure` there.
  Other variants found on the internet (like `.../accounts/login/callback/`, `.../accounts/oidc/nextcloud/login/callback/`, `.../accounts/social/login/callback/`) lead to a 404.

- Following the [allauth documentation for nextcloud](https://docs.allauth.org/en/latest/socialaccount/providers/nextcloud.html) does not work, but putting the server one layer up [did](https://github.com/TandoorRecipes/recipes/issues/3214#issuecomment-2381178171).
  Note that the json payload needs to be in one line and properly escaped for the `.env` (see below).

Final `.env` file (not working, to be continued ...) is
```
SECRET_KEY=<some stuff here>
DB_ENGINE=django.db.backends.sqlite3
POSTGRES_HOST=db_recipes
POSTGRES_DB=djangodb
POSTGRES_PORT=5432
POSTGRES_USER=djangouser
POSTGRES_PASSWORD=<some stuff here>
SOCIAL_PROVIDERS=allauth.socialaccount.providers.nextcloud
SOCIALACCOUNT_PROVIDERS={"nextcloud":{"SERVER":"<server>","APPS":[{"client_id":"<client id>","secret":"<secret>"}]}}
```
