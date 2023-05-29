# Compiler

## Getting started

Python script gets *input.txt* file and returns the generated *output.ll* file with byte-code for LLVM

### How to use?
#### Build the container:
```
docker-compose up -d
```

Create the *input.txt* file in the "compiler/src/code/" directory.

#### Run the container:
```
docker run compiler:latest
```

#### Look at the result:
```
docker logs -f compiler
```

### Libraries

*rply* - allows to generate lexical and syntactic analyzers

*llvmlite* - generates byte-code for llvm
