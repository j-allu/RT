#!/bin/sh
echo "Some pre-task..."
robot --name Example --dotted $*
echo "Some post-task..."
