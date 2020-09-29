from django.http import HttpResponse
import os
import webbrowser

def index(request):
    os.system('cmd /c "gcloud beta dataproc clusters create abdallah-test-cluster --bucket vf-atesio-nwp-nonlive-qa --region europe-west1 --zone europe-west1-b --subnet projects/vf-atesio-nwp-nonlive/regions/europe-west1/subnetworks/dev-restricted-zone --tags allow-internal-dataproc-dev,allow-ssh-from-management-zone,allow-ssh-from-net-to-bastion --project vf-atesio-nwp-nonlive --service-account vf-ates-nwp-dev-dp-ds-sa@vf-atesio-nwp-nonlive.iam.gserviceaccount.com --master-machine-type n1-standard-16 --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n1-standard-16 --worker-boot-disk-size 100 --max-idle 240m --metadata enable-oslogin=true --properties core:fs.gs.implicit.dir.repair.enable=false,core:fs.gs.status.parallel.enable=true --no-address --optional-components=ANACONDA,JUPYTER,ZEPPELIN --enable-component-gateway"')
    webbrowser.open("https://console.cloud.google.com/dataproc/clusters/abdallah-test-cluster/interfaces?region=europe-west1&project=vf-atesio-nwp-nonlive")
    return HttpResponse("Hello, Atesio Cluster has been created, enjoy:)")
