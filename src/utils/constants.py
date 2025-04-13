"""Constants used across the Tardis codebase."""

import os

# Installation paths and configuration
CONFIG_DIR = "/etc/tardis"
CONFIG_PATH = os.path.join(CONFIG_DIR, "tardis.env")
STATE_DIR = "/var/lib/tardis/state"
DEFAULT_CHECKPOINT_PATH = "/var/lib/tardis/checkpoint"

# Environment variables
ENV_REAL_RUNC_CMD = "TARDIS_REAL_RUNC_CMD"

# Runc command related
INTERCEPTABLE_COMMANDS = {'create', 'start', 'checkpoint', 'resume', 'delete'}

# Add this constant for the event listener PID file
EVENT_LISTENER_PID_FILE = "/var/lib/tardis/event_listener.pid"

# List of boolean flags for runc subcommands that don't take values
RUNC_SUBCMD_BOOLEAN_FLAGS = [
    # From runc-checkpoint
    "--leave-running", "--tcp-established", "--ext-unix-sk", 
    "--shell-job", "--lazy-pages", "--file-locks", 
    "--pre-dump", "--auto-dedup",
    # From runc-create
    "--no-pivot", "--no-new-keyring",
    # Global options
    "--debug", "--systemd-cgroup", "--help", "-h", "--version", "-v",
    # Other common flags
    "--detach",
    # Additional global options
    "--rootless",
    # Additional checkpoint options
    "--manage-cgroups-mode", "--empty-ns", "--status-fd", "--page-server"
]

# No need for SHORT_OPTION_MAP since we don't use bundle value for special handling 

# Container config paths
CONTAINER_CONFIG_PATHS = [
    "/run/containerd/io.containerd.runtime.v2.task/{namespace}/{container_id}/config.json",
    "/run/containerd/runc/{namespace}/{container_id}/config.json",
    "/run/runc/{namespace}/{container_id}/config.json"
] 

CONTAINER_ROOTFS_PATHS = [
    "/run/containerd/io.containerd.runtime.v2.task/{namespace}/{container_id}/rootfs",
    "/run/containerd/runc/{namespace}/{container_id}/rootfs",
    "/run/runc/{namespace}/{container_id}/rootfs"
] 

# Logging
LOG_FILE = "logs/tardis.log"
