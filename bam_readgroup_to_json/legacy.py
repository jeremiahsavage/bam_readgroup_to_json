#!/usr/bin/env python3


def header_rg_list_to_rg_dicts(header_rg_list):
    readgroups_list = list()
    for rg_list in header_rg_list:
        keys_values = (
            rg_list.lstrip('@RG').lstrip('\t').lstrip('@SQ').lstrip('\t').split('\t')
        )
        readgroup = dict()
        for key_value in keys_values:
            key_value_split = key_value.split(':')
            a_key = key_value_split[0]
            a_value = key_value_split[1]
            readgroup[a_key] = a_value
        if 'PL' not in readgroup.keys():
            readgroup['PL'] = 'ILLUMINA'
        readgroups_list.append(readgroup)
    return readgroups_list


def extract_readgroup_json(bam_path: str, _di=DI):
    bam_file = os.path.basename(bam_path)
    bam_name, bam_ext = os.path.splitext(bam_file)
    samfile = _di.pysam.AlignmentFile(bam_path, 'rb', check_sq=False)
    samfile_header = samfile.text
    header_list = samfile_header.split('\n')
    header_rg_list = [
        header_line for header_line in header_list if header_line.startswith('@RG')
    ]
    readgroup_dict_list = header_rg_list_to_rg_dicts(header_rg_list)
    if len(readgroup_dict_list) == 0:
        logger.info('len(readgroup_dict_list={}'.format(len(readgroup_dict_list)))
        readgroup_dict = dict()
        readgroup_dict['ID'] = 'default'
        readgroup_json_file = 'default.json'
        with _di.open(readgroup_json_file, 'w') as f:
            _di.json.dump(readgroup_dict, f, ensure_ascii=False)
    else:
        for readgroup_dict in readgroup_dict_list:
            logger.info('readgroup_dict=%s' % readgroup_dict)
            # legacy_check_readgroup(readgroup_dict, logger)
            readgroup_json_file = readgroup_dict['ID'] + '.json'
            readgroup_json_file = readgroup_json_file.replace('+', '')
            logger.info('readgroup_json_file=%s\n' % readgroup_json_file)
            with open(readgroup_json_file, 'w') as f:
                json.dump(readgroup_dict, f, ensure_ascii=False)
    return
