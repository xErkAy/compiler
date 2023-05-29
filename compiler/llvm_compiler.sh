#!/bin/bash

llc -filetype=obj -relocation-model=pic src/code/output.ll
gcc src/code/output.o -o src/code/output