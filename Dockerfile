FROM gdiener/kong-with-oidc
USER root
# Example for GO:
# COPY oauth2-plugin/bin/oauth2-plugin /usr/local/bin/oauth2-plugin

# reset back the defaults
USER kong
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000 8443 8001 8444
STOPSIGNAL SIGQUIT
HEALTHCHECK --interval=10s --timeout=10s --retries=10 CMD kong health
CMD ["kong", "docker-start"]
