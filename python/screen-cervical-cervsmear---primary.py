# Matthew Carr, Evan Kontopantelis, Tim Doran, Christine Campbell, Lorraine Lipscombe, Emma Crosbie, Anothony Howell, Iain E Buchan, Andrew G Renehan, 2024.

import sys, csv, re

codes = [{"code":"9O81.00","system":"readv2"},{"code":"4K33.00","system":"readv2"},{"code":"685E.00","system":"readv2"},{"code":"4K34.00","system":"readv2"},{"code":"4K36.00","system":"readv2"},{"code":"4K2C.00","system":"readv2"},{"code":"685..12","system":"readv2"},{"code":"4K26.00","system":"readv2"},{"code":"4K22.11","system":"readv2"},{"code":"4K2..12","system":"readv2"},{"code":"R150000","system":"readv2"},{"code":"4K25.00","system":"readv2"},{"code":"7E2A211","system":"readv2"},{"code":"L9162PP","system":"readv2"},{"code":"L9162PQ","system":"readv2"},{"code":"L9162PJ","system":"readv2"},{"code":"L9162","system":"readv2"},{"code":"L9162BA","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('screen-cervical-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["screen-cervical-cervsmear---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["screen-cervical-cervsmear---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["screen-cervical-cervsmear---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
