"""
Support for Selve switches
"""
import logging

import voluptuous as vol

from homeassistant.components.light import DEVICE_CLASS_SWITCH, SwitchEntity
from custom_components.selve import DOMAIN as SELVE_DOMAIN, SelveDevice

from homeassistant.const import ATTR_ENTITY_ID
import homeassistant.helpers.config_validation as cv

DEPENDENCIES = ["selve"]

_LOGGER = logging.getLogger(__name__)

SELVE_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Optional(ATTR_ENTITY_ID): cv.entity_ids,
    }
)

SELVE_CLASSTYPES = {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None,
    5: "light",
    6: "light",
    7: "light",
    8: None,
    9: None,
    10: None,
    11: None,
}
