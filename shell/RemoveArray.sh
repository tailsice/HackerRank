#!/bin/bash

LIST=($(cat))
echo ${LIST[@]/[:A-Z:]/.}

