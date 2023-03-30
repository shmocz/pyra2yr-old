PROTOC = protoc
proto_sources := $(wildcard ./protocol/ra2yrproto/*.proto)

protocol.status: $(proto_sources)
	$(PROTOC) -I=./protocol --pyi_out=. --python_out=. $^
	touch $@

protocol: protocol.status

format:
	isort pyra2yr --thirdparty ra2yrproto
	black $(FORMAT_ARGS) --line-length 80 pyra2yr

devinstall:
	pip install -e .

.PHONY: protocol devinstall format
