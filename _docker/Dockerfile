FROM rhoerbe/py3_generic
LABEL maintainer="Rainer Hörbe <r2h2@hoerbe.at>" \
      version="0.0.0" \
      capabilites='--cap-drop=all'

# image for event fetcher

USER root

COPY install/scripts/start.sh /
RUN chmod +x /start.sh

ENV USERNAME=eventf
ENV CONTAINERUID=343030
ENV CONTAINERGID=0
RUN useradd --non-unique --gid $CONTAINERGID --uid $CONTAINERUID $USERNAME
VOLUME /output # ownership defined by volume mapping

USER $USERNAME
COPY event_fetcher.py /home/eventf/
COPY registration.template /home/eventf/

CMD /start.sh