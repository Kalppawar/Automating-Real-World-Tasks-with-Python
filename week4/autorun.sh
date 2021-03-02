#!/usr/bin/env bash

sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
wait

tar xf ~/supplier-data.tar.gz
wait

echo "example description \n"
cat ~/supplier-data/descriptions/004.txt

sudo chmod +x example_upload.py

### Do All Tasks
./changeImage.py
wait
./example_upload.py
wait
./supplier_image_upload.py
wait
./run.py
wait
./report_email.py
wait
sudo apt install stress
wait
stress --cpu 8 &

./health_check.py

echo "all done \n now check the status"
