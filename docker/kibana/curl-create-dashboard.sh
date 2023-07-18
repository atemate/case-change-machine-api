#!/bin/sh
# Source: https://medium.com/develeap/kibana-objects-exporting-importing-c427a8eb92e9
set -euxo pipefail

DATA_VIEW_CONFIG_NDJSON="${DATA_VIEW_CONFIG_NDJSON:-}"
DASHBOARD_CONFIG_JSON="${DASHBOARD_CONFIG_JSON:-}"

echo KIBANA_URL="$KIBANA_URL"


#Wait for Kibana to be available & healthy
function wait_for_kibana {
    echo "Testing connection to Kibana"
    until $(curl "${KIBANA_URL}/_cluster/health/"); do
        sleep 5
    done
}

#Import data view
function import_data_view {
    echo "Importing data_view..."
    OUTPUT=$(curl -X POST "${KIBANA_URL}/api/saved_objects/_import" -H "kbn-xsrf: true" --form file=@"$DATA_VIEW_CONFIG_NDJSON" | tee /dev/stderr | jq .success)
    if [[ "${OUTPUT}" == "true" ]]; then
        printf "\n########## Imported data view successfully! #############################\n"
    else
        printf "\n########## Failure while importing data view #############\n"
    fi
    echo ${OUTPUT}
}

#Import dashboards
function import_dashboards {
    echo "Importing dashboards..."
    OUTPUT=$(curl -X POST "${KIBANA_URL}/api/kibana/dashboards/import?exclude=index-pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d @"$DASHBOARD_CONFIG_JSON" | tee /dev/stderr | jq .success)
    if [[ "${SUCCESS}" == "true" ]]; then
        printf "\n########## Imported dashboards successfully! #############################\n"
    else
        printf "\n########## Failure while importing dashboards #############\n"
    fi
    echo ${OUTPUT}
}

wait_for_kibana

if [[ "$DATA_VIEW_CONFIG_NDJSON" ]]; then
    import_data_view
fi

if [[ "$DASHBOARD_CONFIG_JSON" ]]; then
    import_dashboards
fi
