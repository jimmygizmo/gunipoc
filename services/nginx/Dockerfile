FROM nginx:1.19-alpine
# TODO: This is newer than the version I use in Nucleus: nginx:1.15.8-alpine
# TODO: Update Nucleus with at least 1.19 or higher.

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

