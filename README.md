# AEMO Report

  ![National Energy Network (AEMO)](images/national-energy-network.png)

This Home Assistant Integration retrieves the National Energy Market (NEM)
Reports from Australia

This sensor uses the official API to get the the current report on the status of the
Electricity Grid on the east coast of Australia, including South Australia. This report is available from https://visualisations.aemo.com.au/aemo/apps/api/report/ELEC_NEM_SUMMARY

Specifically, the report contains the current energy pricing in the various submarkets, and the production and consumption values and any network notices which are currently active.

## Development Status
The initial (and current) development uses existing Home Assistant integrations
(RESTful and Template) to poll the API for the report, import and process the
data and create entities for monitoring and displaying the data.

### Installation
Copy the configuration file (config/aemo_report.yaml) into the site Home Assistant
configuration file. (A file access tool may be required to do this.)

A dashboard definition file which has some suitable cards already defined can be
found in 'dashboards/', with individual cards defined in 'cards/'.

### Current Issues and Future Development

- The import of the various State(Market) parameters explicitly depends on the
  order listed int he JSON report. If this order ever changes, the data will be
  incorrectly reported.

- The JSON report contains more information (eg. Network Notices, Interconnector
  Power Transfers). It would be good to display more of these details.

- Further development of this configuration into an integration (AEMO Report)
  which can be easily installed without manually editing YAML files.

## Notes

On a Linux host, the AEMO JSON report can be downloaded with the following
command (if you have wget and jq installed):

    wget https://visualisations.aemo.com.au/aemo/apps/api/report/ELEC_NEM_SUMMARY -O - \
      | jq
