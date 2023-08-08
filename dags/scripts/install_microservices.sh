#!/bin/bash

git clone https://github.com/amitsatpute-pyjs/micro-shop-setup.git

cd ./micro-shop-setup

bash setRegCluster.sh

bash  deployAllRepo.sh

bash runServices.sh
