l1 = [{u'ID': u'111', u'IconIndex': u'0', u'Par4': u'0', u'IconColour': u'0', u'IsBGImageSet': u'0', u'Par5': u'0',
       u'Module': u'0', u'Text2': u'', u'LabelColor': u'0', u'State': u'0', u'Text1': u'1', u'Par3': u'0',
       u'Par2': u'0', u'View': u'0', u'Icon': u'STATUSBAR_MISSED_CALL_COUNT'}, {u'ID': u'112', u'IconIndex': u'1',
                                                                                u'Par4': u'0', u'IconColour': u'0',
                                                                                u'IsBGImageSet': u'0', u'Par5': u'0',
                                                                                u'Module': u'0', u'Text2': u'',
                                                                                u'LabelColor': u'0', u'State': u'0',
                                                                                u'Text1': u'0', u'Par3': u'0',
                                                                                u'Par2': u'0', u'View': u'1',
                                                                                u'Icon': u'SOFT_LINE_IDLE_SIP'},
      {u'ID': u'113',u'IconIndex': u'2', u'Par4': u'0', u'IconColour': u'0', u'IsBGImageSet': u'0', u'Par5': u'0',
       u'Module': u'0', u'Text2': u'', u'LabelColor': u'0', u'State': u'0', u'Text1': u'0', u'Par3': u'0', u'Par2': u'0'
          , u'View': u'1', u'Icon': u'SOFT_LINE_IDLE_SIP'}, {u'ID': u'114', u'IconIndex': u'3', u'Par4': u'0',
                                                             u'IconColour': u'27', u'IsBGImageSet': u'0', u'Par5': u'0',
                                                             u'Module': u'0', u'Text2': u'', u'LabelColor': u'0',
                                                             u'State': u'0', u'Text1': u'0', u'Par3': u'0',
                                                             u'Par2': u'0', u'View': u'1', u'Icon': u'STATUS_BLF_GREEN'}
      ]

for item in l1:
    if item['Icon'] == 'STATUSBAR_MISSED_CALL_COUNT':
        flag = 1
        pkt_id = item['ID']
        break

for item in l1:
    if flag and item['Icon'] == 'STATUS_BLF_GREEN':
        flag2 = 1
        break
for item in l1:
    if flag2 and item['ID'] not in pkt_id:
        print(item)







