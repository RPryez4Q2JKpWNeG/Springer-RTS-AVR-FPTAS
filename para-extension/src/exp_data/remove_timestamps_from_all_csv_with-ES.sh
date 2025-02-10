#!/bin/bash

for x in *-ES*.csv; do cp "$x" "${x/-ES*}-ES.csv"; done