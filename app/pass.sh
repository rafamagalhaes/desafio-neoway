#!/bin/bash

PASS="cjQyODgyNkBNCg=="

PASS=(`echo $PASS | base64 --decode`)

echo "PASSWORD=$PASS" >> $GITHUB_ENV