#!/usr/bin/env bash

printf "create SAP1 policy:\n"
curl http://localhost:6543/policy -H "Content-Type: application/json" \
-X POST -d '{"name": "SAP1", "type": "SAP"}'

printf "\n\ncreate SAP2 policy:\n"
curl http://localhost:6543/policy -H "Content-Type: application/json" \
-X POST -d '{"name": "SAP2", "type": "SAP"}'

printf "\n\ncreate EB1 policy:\n"
curl http://localhost:6543/policy -H "Content-Type: application/json" \
-X POST -d '{"name": "EBS1", "type": "EBS"}'

printf "\n\ncreate and fetch module mod1_SAP1:\n"
curl http://localhost:6543/module -H "Content-Type: application/json" \
-X POST -d '{"name": "mod1_SAP1", "type": "SAP", "policy_id": 1, "description": "ASD module"}'
printf "\n"
curl http://localhost:6543/module/1

printf "\n\ncreate and fetch module mod2_SAP1:\n"
curl http://localhost:6543/module -H "Content-Type: application/json" \
-X POST -d '{"name": "mod2_SAP1", "type": "SAP", "policy_id": 1}'
printf "\n"
curl http://localhost:6543/module/2

printf "\n\ncreate and fetch module mod1_SAP2:\n"
curl http://localhost:6543/module -H "Content-Type: application/json" \
-X POST -d '{"name": "mod1_SAP2", "type": "SAP", "policy_id": 2}'
printf "\n"
curl http://localhost:6543/module/3

printf "\n\ncreate and fetch module mod1_EBS1:\n"
curl http://localhost:6543/module -H "Content-Type: application/json" \
-X POST -d '{"name": "mod1_EBS1", "type": "EBS", "policy_id": 3}'
printf "\n"
curl http://localhost:6543/module/4

printf "\n\ncreate and fetch module mod2_EBS1:\n"
curl http://localhost:6543/module -H "Content-Type: application/json" \
-X POST -d '{"name": "mod2_EBS1", "type": "EBS", "policy_id": 3}'
printf "\n"
curl http://localhost:6543/module/5

printf "\n\nretrieve SAP1 policy:\n"
curl http://localhost:6543/policy/1

printf "\n\nretrieve EBS1 policy:\n"
curl http://localhost:6543/policy/3

printf "\n\nretrieve SAP2 policy:\n"
curl http://localhost:6543/policy/2

printf "\n\nretrieve SAPs policies:\n"
curl http://localhost:6543/policies/SAP

printf "\n\nretrieve EBSs policies:\n"
curl http://localhost:6543/policies/EBS

printf "\n\nretrieve SAP1's modules:\n"
curl http://localhost:6543/policy/1/modules

printf "\n\nretrieve EBS1's modules:\n"
curl http://localhost:6543/policy/3/modules

printf "\n\nretrieve SAP2's modules:\n"
curl http://localhost:6543/policy/2/modules

printf "\n\n"