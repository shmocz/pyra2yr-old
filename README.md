# pyra2yr

Python interface for Red Alert 2: Yuri's Revenge, utilizing the [ra2yrcpp](https://github.com/CnCNet/ra2yrcpp) library and [ra2yrproto](https://github.com/shmocz/ra2yrproto) protocol definitions.

## Setup

Clone sources:
```
$ git clone --recurse-submodules https://github.com/shmocz/pyra2yr
```

In a suitable Python environment, invoke:

```bash
$ cd pyra2yr
$ python3 -m pip install -r requirements.txt .
```

Generate protobuf definitions (requires the protobuf compiler `protoc`):

```bash
$ make protocol
```

## Usage

See `pyra2yr/test_*.py` files for example usage.
