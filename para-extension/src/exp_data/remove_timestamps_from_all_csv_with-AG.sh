#!/bin/bash

for x in *-AG*.csv; do cp "$x" "${x/-AG*}-AG.csv"; done