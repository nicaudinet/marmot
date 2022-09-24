ARG FROM_IMAGE=ros:eloquent
ARG OVERLAY_WS=/opt/ros/overlay_ws

# multi-stage for caching
FROM $FROM_IMAGE AS cacher

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
ADD . ros2/code

# copy manifests for caching
WORKDIR /opt
RUN mkdir -p /tmp/opt && \
  find ./ -name "package.xml" | \
  xargs cp --parents -t /tmp/opt && \
  find ./ -name "COLCON_IGNORE" | \
  xargs cp --parents -t /tmp/opt || true

# multi-stage for building
FROM $FROM_IMAGE AS builder

ENV DEBIAN_FRONTEND=noninteractive

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
COPY --from=cacher /tmp/$OVERLAY_WS/src ./src

# build overlay source
COPY --from=cacher $OVERLAY_WS/src ./src
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
  colcon build \
  --packages-select \
  pi_control \
  --mixin $OVERLAY_MIXINS

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
  '$isource "$OVERLAY_WS/install/setup.bash"' \
  /ros_entrypoint.sh
