# Data Collection
## Caida
collectCaida.py is used to download the caida data, we could input a date, and the script will download the caida data on that day.
anaCaida.py: input a date and an ASN, output the child list, parent list and p2p list of given asn

## Rovista
asRovInfo.py: input an ASN, output this ASN's info, like rank, organization, country, ROV ratio, cone size and number of addresses.
asRovScore.py: input an ASN and date, output the ASN's ROV score on that day, include total path number and filter path number.
rovCountryRatios.py: input a country name and date, output the country's as ratio with zero/hundred ROV on that day.
rovInference.py: input an ASN and date, output all the annoucement the AS published on that day and show if it is valid.
rovRatios.py: input a date, output the world rov ratio with zero/hundred ROV on that day.
worldROVScore.py: input cone-size or number of addresses, based on the input list all the countries ROV ratio currently.

## apnic roa and rpki
apnic roas: a summary of all ROAs from all over the world, use RP to see how many ROA is valid
apnicRoas.py: input a date and a country name, output the ipv4/6 valid/invalid/unknown routes/address
ps: 
routes is the ratio of advertised  routes that are covered by a ROA to the total route count
address is the ratio of the span of advertised addresses that are coverd by a ROA to the total address span

apnic rpki: measure invalid ROV throw-away situation, check if the network is ROV-aware
apnicRpki.py: input a date and a country name, output the date last 1/10/30/60/90 day test results in number and percentage of routes\partial_validate_routes\validate_routes checked

## Ripe ROA data
dataDownload.py: input a date, download afrinic/lacnic/apnic/arin/ripencc roa output.json on that date.
asnRipe.py: input an ASN, output all the prefix that the ASN can published valid in the Internet.
prefixRipe.py: input a prefix, output the ASN who could published the prefix in a valid state.


## RP Database
ip2version.py: input a date and an IP, output all the RP version used by the IP on that day
version2ip.py: input a date and an RP version, output all the IP who still used that version of RP on that day. Could use Fuzzy search, like "Routinator" or "Routinator/0.12.1"