#!/usr/bin/env bash

# settings for docker build, run and exec

main() {
    SCRIPTDIR=$(cd $(dirname $BASH_SOURCE[0]) && pwd)
    source $SCRIPTDIR/dscripts/conf_lib.sh  # load library functions

    init_sudo
    set_volume_root
    set_image_and_container_name
    set_users
    #set_buildargs
    set_run_args
    #set_network
    set_vol_mapping
}


set_volume_root() {
    DOCKERVOL_ROOT='/docker_volumes'
}


set_image_and_container_name() {
    # This IMGID qualifies image, container, user and IP adddress; this is helpful for managing
    # processes on the docker host etc.
    IMGID='30'  # range from 02 .. 99; must be unique per node
    PROJSHORT='eventfetcher'
    export IMAGENAME="rhoerbe/$PROJSHORT"  # [a-z_0-9]
    export CONTAINERNAME="${IMGID}${PROJSHORT}"
}


set_users() {
    export CONTAINERUSER="eventf"   # hard coded in container
    export CONTAINERUID="3430${IMGID}"
    export START_AS_ROOT=      # 'True' (e.g. for apache to fall back to www user)
}


#set_buildargs() {
#    export BUILDARGS=""
#}


set_run_args() {
    export ENVSETTINGS=""
    get_capabilities
    export STARTCMD='/start.sh'  # unset or blank to use image default
}


#set_network() {
#}


set_vol_mapping() {
    create_user $CONTAINERUSER $CONTAINERUID # required for host dir mapping
    export VOLROOT="${DOCKERVOL_ROOT}/$CONTAINERNAME"  # container volumes on docker host
    map_host_directory  "$VOLROOT/output" '/output' 'rw'
    map_host_directory  "$VOLROOT/token" '/token' 'ro'
}


main
