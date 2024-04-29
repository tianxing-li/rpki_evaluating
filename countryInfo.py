import rovista.rovCountryRatios
import rovista.worldROVScore
import apnic.apnicRoas
import apnic.apnicRpki


def main():
    # date and country/region input
    dataDate = input("please input a date in yyyy-mm-dd format：")
    cn = input("please input a country/region name like Germany:")

    # rovista/rovCountryRatios
    print("\nrovista ROV Country Ratios: ")
    cnRatios = rovista.rovCountryRatios.rov_country_ratios(cn, dataDate)
    for key in cnRatios:
        print(key, cnRatios[key])


    # rovista/worldROVScore currently country side ROV score
    print("\nCurrently country ROV score:")
    cnAddressSpace = rovista.worldROVScore.world_ROV_Score("0", cn)
    cnConeSize = rovista.worldROVScore.world_ROV_Score("1", cn)
    print("Based on Address Space:")
    print(cnAddressSpace) 
    print("Based on Cone Size:")
    print(cnConeSize)

    # apnic ROA data
    print("\nAPNIC ROAs Data:")
    apnicROA = apnic.apnicRoas.get_roa(dataDate, cn)
    for key, value in apnicROA.items():
        print(key + ": " + str(value))

    # apnic invalid ROV throw-away situation
    print("\nAPNIC invalid ROV detection:")
    apnicRPKI = apnic.apnicRpki.get_rpki(dataDate, cn)
    for key, value in apnicROA.items():
        print(key + ": " + str(value))


 



if __name__ == "__main__":
    main()