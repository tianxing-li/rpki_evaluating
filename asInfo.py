import caida.collectCaida
import caida.anaCaida
import rovista.asRovInfo
import rovista.asRovScore
import rovista.rovInference
import ripe.dataDownload
import ripe.asnRipe
import apnic.apnicRoaAS
import apnic.apnicRpkiAS


def main():
    # date and asn input
    dataDate = input("please input a date in yyyy-mm-dd format：")
    inputASN = input("please input an AS number：")
    asn = int(inputASN)


    # caida data download
    caida.collectCaida.caidadata_download(dataDate)

    # caida data search
    child, parent, p2p = caida.anaCaida.as_Rel(dataDate, inputASN)
    print("Child List:", child)
    print("Parent List:", parent)
    print("P2P List:", p2p, "\n")

    # rovista as info
    asnInfo = rovista.asRovInfo.as_rov_info(inputASN)
    for item in asnInfo['data']:
        if item['asn'] == asn:
            print("ASN:", item['asn'])
            print("Rank:", item['rank'])
            print("Organization:", item['organization'])
            print("Country:", item['country'])
            print("Country ISO:", item['countryIso'])
            print("Ratio:", item['ratio'])
            print("Last Updated Date:", item['lastUpdatedDate'])
            print("Cone Size:", item['coneSize'])
            print("Number of Addresses:", item['numberOfAddresses'])
            break
    else:
        print("ASN not found:", asn)


    # rovista ROV Score
    rovScore = rovista.asRovScore.rov_ratios(inputASN, dataDate)
    print("\nrovista ROV Score:")
    for item in rovScore:
        if item['asnDateKey']['recordDate'] == dataDate:
            print(item)


    # rovista ROV Inference
    rovInf = rovista.rovInference.rov_inference(inputASN, dataDate)
    print("\nrovista ROV Inference:")
    for item in rovInf:
        print(item)

    # RIPE data download
    print("\nRIPE Data Download:")
    ripe.dataDownload.tal_loop(dataDate)

    # RIPE AS Information
    print("\nRIPE AS valid ROA information:")
    ripeROV = ripe.asnRipe.asn_all(inputASN)
    for item in ripeROV:
        print(item)

    # APNIC ROA Information
    print("\nAPNIC ROA Information:")
    apnicROA = apnic.apnicRoaAS.get_roa_as(dataDate, inputASN)
    for key in apnicROA:
        print(key, apnicROA[key])

    # APNIC invalid ROV throw-away situation
    print("\nAPNIC invalid ROV detection:")
    apnicRPKI = apnic.apnicRpkiAS.get_rpki_as(dataDate, inputASN)
    for item in apnicRPKI:
        print(item)












if __name__ == "__main__":
    main()