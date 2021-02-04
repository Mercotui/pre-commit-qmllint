#!/usr/bin/env bash

source activate_run.sh
qmllint "$@"
STATUS=$?
source deactivate_run.sh
exit $STATUS
