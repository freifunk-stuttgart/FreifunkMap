#requirement: ln peers-ffs (https://github.com/freifunk-stuttgart/peers-ffs) here.
import os, json, re

rootdir = './peers-ffs/'
output = {}
segments = []
reg_compile = re.compile("vpn\d{2}")
for dirpath, dirnames, filenames in os.walk(rootdir):
    segments = segments + [dirname for dirname in dirnames if  reg_compile.match(dirname)]

for segment in segments:
    if os.path.isdir(rootdir + segment +"/regions"):
        output[segment] = {}
        json_files = [pos_json for pos_json in os.listdir(rootdir + segment +"/regions/") if pos_json.endswith('.json')]
        for file in json_files:
            with open(rootdir + segment +"/regions/" + file) as data_file:
                data = json.load(data_file)
                if 'type' in data and data['type'] == "GeometryCollection":
                    output[segment][len(output[segment])] = data['geometries']

        with open(segment+'.json', 'w') as fp:
            json.dump(output, fp)