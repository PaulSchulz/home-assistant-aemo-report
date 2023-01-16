"""
The aemo_report integration.
This component get the most recent AEMO Report for the Australian Electricity Grid
"""
from __future__ import annotations

import logging

_LOGGER = logging.getLogger(__name__)

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

# List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.SENSOR]

CONF_URL = "url"
DEFAULT_URL = "https://visualisations.aemo.com.au/aemo/apps/api/report/ELEC_NEM_SUMMARY"

async def async_setup(hass, config):
    """Setup the AEMO Report component. """
    # Get the URL from the configuration. Use DEFAULT_URL if none is provided

    url = config[DOMAIN].get(CONF_URL, DEFAULT_URL)

    hass.states.async_set("aemo_report.url", url)
    hass.states.async_set("aemo_report.status", "loading")
    hass.states.async_set("aemo_report.vic1_price", "70.8")
    hass.states.async_set("aemo_report.nsw1_price", "34.2")

    hass.states.async_set("aemo_report.status", "loaded")
    _LOGGER.info("The 'AEMO Report' component is ready!")
    # Return boolean to indicate that initialization was successful.
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up aemo_report from a config entry."""

    hass.data.setdefault(DOMAIN, {})
    # 1. Create API instance
    # 2. Validate the API connection (and authentication)
    # 3. Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
