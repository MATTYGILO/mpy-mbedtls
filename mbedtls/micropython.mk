# this file autodetected by py/py.mk based on its name

MBEDTLS_MOD_DIR := $(USERMOD_DIR)

SRC_USERMOD += $(MBEDTLS_MOD_DIR)/mod_mbedtls.c

CFLAGS_MOD += -DMBEDTLS_CONFIG_FILE='"mbedtls_config.h"'

