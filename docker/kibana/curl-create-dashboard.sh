#!/bin/sh
# Source: https://medium.com/develeap/kibana-objects-exporting-importing-c427a8eb92e9
set -euxo pipefail

DATA_VIEW_CONFIG_NDJSON="${1}"
DASHBOARD_CONFIG_JSON="${2}"

echo KIBANA_URL="$KIBANA_URL"
echo KIBANA_PORT="$KIBANA_PORT"


#Wait for Kibana to be available & healthy
function wait_for_kibana {
    echo "Testing connection to Kibana"
    until $(curl -k -X GET https://${KIBANA_URL}:${KIBANA_PORT}/_cluster/health); do sleep 5; done
    until [ "$(curl -k -X GET https://${KIBANA_URL}:${KIBANA_PORT}/_cluster/health | wc -l)" == "0" ]
    do sleep 5
    done
}

#Import data view
function import_data_view {
    echo "Importing data_view..."
    OUTPUT=$(curl -k --user user:pwd -X POST https://${KIBANA_URL}:${KIBANA_PORT}/api/saved_objects/_import -H "kbn-xsrf: true" --form file=@$DATA_VIEW_CONFIG_NDJSON)
    SUCCESS=$(echo ${OUTPUT} | grep -o '"successCount":1' | wc -l)
    if [[ ${SUCCESS} == "1" ]]; then
        printf "\n########## Imported data view successfully! #############################\n"
    else
        printf "\n########## Failure while importing data view #############\n"
    fi
    echo ${OUTPUT}
}

#Import dashboards
function import_dashboards {
    echo "Importing dashboards..."
    OUTPUT=$(curl --user user:pwd -X POST https://${KIBANA_URL}:${KIBANA_PORT}/api/kibana/dashboards/import?exclude=index-pattern -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d @$DASHBOARD_CONFIG_JSON)
    SUCCESS=$(echo ${OUTPUT} | grep -o '"successCount":1' | wc -l)
    if [[ ${SUCCESS} == "1" ]]; then
        printf "\n########## Imported dashboards successfully! #############################\n"
    else
        printf "\n########## Failure while importing dashboards #############\n"
    fi
    echo ${OUTPUT}
}

wait_for_kibana
import_data_view
import_dashboards
