#!/usr/bin/env python
# -*- coding: utf-8 -*-
import elementtree.ElementTree as ET
import csv
import random

tree = ET.parse("sample.xml")
root=tree.getroot()

output_places = open("PlacesXML/places.csv", "w+b")
places_csv_to=csv.writer(output_places)
output_location = open("PlacesXML/location.csv", "w+b")
location_csv_to=csv.writer(output_location)
output_streets = open("PlacesXML/streets.csv", "w+b")
streets_csv_to=csv.writer(output_streets)
output_geoposition = open("PlacesXML/geoposition.csv", "w+b")
geoposition_csv_to=csv.writer(output_geoposition)
output_admin = open("PlacesXML/admin.csv", "w+b")
admin_csv_to=csv.writer(output_admin)
output_contacts = open("PlacesXML/contacts.csv", "w+b")
contacts_csv_to=csv.writer(output_contacts)
output_category = open("PlacesXML/category.csv", "w+b")
category_csv_to=csv.writer(output_category)
output_name = open("PlacesXML/name.csv", "w+b")
name_csv_to=csv.writer(output_name)
output_stats = open("PlacesXML/stats.csv", "w+b")
stats_csv_to=csv.writer(output_stats)

fields=["Timestamp","PlaceID"]
places_csv_to.writerow(fields)
fields=["LocationID","PlaceID","StreetID","HouseNumber","CountryCode","PostalCode","AdminID","GeopositionID","LanguageCode"]
location_csv_to.writerow(fields)
fields=["StreetID","BaseName","StreetType","Suffix"]
streets_csv_to.writerow(fields)
fields=["GeoPositionID","Latitude","Longitude","Altitude"]
geoposition_csv_to.writerow(fields)
fields=["AdminID","AdminLevel1","AdminName1","AdminLevel2","AdminName2","AdminLevel3","AdminName3","AdminLevel4","AdminName4"]
admin_csv_to.writerow(fields)
fields=["ContactID","PlaceID","ContactType","ContactString"]
contacts_csv_to.writerow(fields)
fields=["CategoryID","PlaceID","CategorySystem","LanguageCode","CategoryText"]
category_csv_to.writerow(fields)
fields=["NameID","PlaceID","NameType","LanguageCode","BaseText"]
name_csv_to.writerow(fields)

PlaceId=0
LanguageCode=""
StreetId=0
BaseName=""
StreetType=""
Suffix=""
HouseNumber=""
CountryCode=""
PostalCode=""
AdminId=0
AdminLevel1=""
AdminName1=""
AdminLevel2=""
AdminName2=""
AdminLevel3=""
AdminName3=""
AdminLevel4=""
AdminName4=""
GeoPositionId=0
Latitude=""
Longitude=""
Altitude=""
ContactType=""

places_row=[]
location_row=[]
streets_row=[]
geoposition_row=[]
admin_row=[]
contacts_row=[]
category_row=[]
name_row=[]

quant_CategoryId=[]
CategoryIds=[]
NameTextslang=[]
quant_NameTextslang=[]

placeidline=tree.findall("/Place")
quantity_places=0
for p in placeidline:
   quantity_places+=1
for i in range(0,quantity_places):
    for p in placeidline[i]:
        if p.tag=="CategoryList":
            CategoryIdline=placeidline[i].findall(".///Category")
            for x in CategoryIdline:
                for z in x:
                    if z.tag=="CategoryId":
                        if len(CategoryIds)==0:
                            CategoryIds.append(z.text)
                            quant_CategoryId.append(1)
                        else:
                            for k in range(0,len(CategoryIds)):
                                if z.text==CategoryIds[k]:
                                    quant_CategoryId[k]+=1
                                    break
                                elif k==len(CategoryIds)-1:
                                    CategoryIds.append(z.text)
                                    quant_CategoryId.append(1)
                                else:
                                    continue
        for dat in p:
            if dat.tag=="TimeStamp":
                places_row.append(dat.text)
            elif dat.tag=="PlaceId":
                PlaceId=dat.text
                places_row.append(PlaceId)
            elif dat.tag=="Location":
                location_row.append(dat.attrib.setdefault("locationId"))
                location_row.append(PlaceId)
                locationline=placeidline[i].find(".//Address")
                for x in locationline:
                    if x.tag=="Parsed":
                        LanguageCode=x.attrib.setdefault("languageCode")
                locationline=placeidline[i].find(".////StreetName")
                for x in locationline:
                    StreetId=random.randint(0,32768)
                    if x.tag=="BaseName":
                        BaseName=x.text
                    elif x.tag=="StreetType":
                        StreetType=x.text
                    elif x.tag=="Suffix":
                        Suffix=x.text
                streets_row.append(StreetId)
                streets_row.append(BaseName)
                streets_row.append(StreetType)
                streets_row.append(Suffix)
                streets_csv_to.writerow(streets_row)
                streets_row=[]
                location_row.append(StreetId)
                BaseName=""
                StreetType=""
                Suffix=""
                locationline=placeidline[i].find(".///Parsed")
                for x in locationline:
                    if x.tag=="HouseNumber":
                        HouseNumber=x.text
                    elif x.tag=="CountryCode":
                        CountryCode=x.text
                    elif x.tag=="PostalCode":
                        PostalCode=x.text
                location_row.append(HouseNumber)
                location_row.append(CountryCode)
                location_row.append(PostalCode)
                HouseNumber=""
                CountryCode=""
                PostalCode=""
                AdminId=random.randint(0,32768)
                locationline=placeidline[i].find("./////AdminLevel")
                for x in locationline:
                    if x.tag=="Level1":
                        AdminLevel1=x.text
                    elif x.tag=="Level2":
                        AdminLevel2=x.text
                    elif x.tag=="Level3":
                        AdminLevel3=x.text
                    elif x.tag=="Level4":
                        AdminLevel4=x.text
                locationline=placeidline[i].find("./////AdminName")
                for x in locationline:
                    if x.tag=="Level1":
                        AdminName1=x.text
                    elif x.tag=="Level2":
                        AdminName2=x.text
                    elif x.tag=="Level3":
                        AdminName3=x.text
                    elif x.tag=="Level4":
                        AdminName4=x.text
                admin_row.append(AdminId)
                admin_row.append(AdminLevel1)
                admin_row.append(AdminName1)
                admin_row.append(AdminLevel2)
                admin_row.append(AdminName2)
                admin_row.append(AdminLevel3)
                admin_row.append(AdminName3)
                admin_row.append(AdminLevel4)
                admin_row.append(AdminName4)
                admin_csv_to.writerow(admin_row)
                admin_row=[]
                location_row.append(AdminId)
                AdminLevel1=""
                AdminName1=""
                AdminLevel2=""
                AdminName2=""
                AdminLevel3=""
                AdminName3=""
                AdminLevel4=""
                AdminName4=""
                locationline=placeidline[i].find(".//GeoPositionList")
                for x in locationline:
                    if x.tag=="GeoPosition":
                        coordinates=locationline.find("./GeoPosition")
                        GeoPositionId=random.randint(0,32768)
                        for z in coordinates:
                            if z.tag=="Latitude":
                                Latitude=z.text
                            elif z.tag=="Longitude":
                                Longitude=z.text
                            else:
                                Altitude=z.text
                        location_row.append(GeoPositionId)
                        geoposition_row.append(GeoPositionId)
                        geoposition_row.append(Latitude)
                        geoposition_row.append(Longitude)
                        geoposition_row.append(Altitude)
                        geoposition_csv_to.writerow(geoposition_row)
                        geoposition_row=[]
                        Latitude=""
                        Longitude=""
                        Altitude=""
                location_row.append(LanguageCode)
                location_csv_to.writerow(location_row)
                location_row=[]
            elif dat.tag=="Contact":
                contactline=placeidline[i].find(".///Contact")
                for p in contactline:
                    ContactId=random.randint(0,32768)
                    contacts_row.append(ContactId)
                    contacts_row.append(PlaceId)
                    ContactType=dat.attrib.setdefault("type")
                    contacts_row.append(ContactType)
                    contactlinestr=dat.getchildren()
                    for z in contactlinestr:
                        ContactString=z.text
                        contacts_row.append(ContactString)
                        ContactString=""
                    contacts_csv_to.writerow(contacts_row)
                    contacts_row=[]
                    ContactType=""
            elif dat.tag=="Name":
                nameline=placeidline[i].find(".///BaseText")
                NameId=random.randint(0,32768)
                NameType=nameline.attrib.setdefault("type")
                LanguageCode=nameline.attrib.setdefault("languageCode")
                BaseText=nameline.text
                name_row.append(NameId)
                name_row.append(PlaceId)
                name_row.append(NameType)
                name_row.append(LanguageCode)
                name_row.append(BaseText)
                name_csv_to.writerow(name_row)
                name_row=[]
                NameTextline=placeidline[i].findall(".///TextList")
                for x in NameTextline:
                    for z in x:
                        if z.tag=="Text":
                            if len(NameTextslang)==0:
                                NameTextslang.append(z.attrib.setdefault("languageCode"))
                                quant_NameTextslang.append(1)
                            else:
                                for k in range(0,len(NameTextslang)):
                                    if z.attrib.setdefault("languageCode")==NameTextslang[k]:
                                        quant_NameTextslang[k]+=1
                                        break
                                    elif k==len(NameTextslang)-1:
                                        NameTextslang.append(z.attrib.setdefault("languageCode"))
                                        quant_NameTextslang.append(1)
                                    else:
                                        continue
            elif dat.tag=="Category":
                CategorySystem=dat.attrib.setdefault("categorySystem")
                categoryidline=dat.find("./CategoryId")
                CategoryId=categoryidline.text
                categorytextline=dat.find(".//Text")
                try:
                    LanguageCode=categorytextline.attrib.setdefault("languageCode")
                    CategoryText=categorytextline.text
                except:
                    LanguageCode=""
                    CategoryText=""
                category_row.append(CategoryId)
                category_row.append(PlaceId)
                category_row.append(CategorySystem)
                category_row.append(LanguageCode)
                category_row.append(CategoryText)
                category_csv_to.writerow(category_row)
                category_row=[]

    places_csv_to.writerow(places_row)
    places_row=[]
stats_row=["Quantity of places","CategoryId: quantity","languageCode: quantity"]
stats_csv_to.writerow(stats_row)
lenCat= len(CategoryIds)
lenName=len(NameTextslang)
for i in range(0,max(lenCat,lenName)):
    if i==0:
        if i > len(CategoryIds):
            stats_row=[quantity_places,"",NameTextslang[i]+':'+str(quant_NameTextslang[i])]
        elif i > len(NameTextslang)-1:
            stats_row=[quantity_places,CategoryIds[i]+':'+str(quant_CategoryId[i]),""]
        else:
            stats_row=[quantity_places,CategoryIds[i]+':'+str(quant_CategoryId[i]),NameTextslang[i]]
    elif i > len(CategoryIds)-1:
        stats_row=["","",NameTextslang[i]+':'+str(quant_NameTextslang[i])]
    elif i > len(NameTextslang)-1:
        stats_row=["",CategoryIds[i]+':'+str(quant_CategoryId[i]),""]
    else:
        stats_row=["",CategoryIds[i]+':'+str(quant_CategoryId[i]),NameTextslang[i]]
    stats_csv_to.writerow(stats_row)
