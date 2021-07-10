#!/bin/bash

uniq -ic | tr -s [:blank:]  | sed "s/^ //"
