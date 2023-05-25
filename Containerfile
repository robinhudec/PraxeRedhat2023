FROM registry.access.redhat.com/ubi9/nginx-120:1-39
RUN echo "It is pitch black" >> index.html
CMD nginx -g "daemon off;"
