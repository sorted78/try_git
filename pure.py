#!python 

from purestorage import FlashArray

storage = FlashArray(target='172.16.128.20',username='purevcenter',password='$W.gWN6^j')

volume_detail = storage.get_volume("HRC-PURE-DS-ADMC-DR-01")

print('Name: {} Size: {}'.format(volume_detail['name'], volume_detail['size']))

for volume in storage.list_volumes():
    print(volume)
