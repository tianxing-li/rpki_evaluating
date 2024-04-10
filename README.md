# Data Collection
## Caida

collectCaida.py is used to download the caida data. We could input a date, and the script will download the caida data that day.

anaCaida.py: input a date and an ASN, output the child list, parent list, and p2p list of given asn

## Rovista
asRovInfo.py: input an ASN and output this ASN's info, like rank, organization, country, ROV ratio, cone size, and number of addresses.

asRovScore.py: input an ASN and date, output the ASN's ROV score on that day, and include the total and filter path numbers.

rovCountryRatios.py: input a country name and date, and output the country's as ratio with zero/hundred ROV on that day.

rovInference.py: input an ASN and date, output all the announcements the AS published on that day, and show if it is valid.

rovRatios.py: input a date, and output the world rov ratio with zero/hundred ROV on that day.

worldROVScore.py: input "cone-size" or "addresses" based on the current input list of all the country's ROV ratios.

## apnic roa and rpki

apnic roas: a summary of all ROAs from all over the world; use RP to see how many ROAs are valid

apnicRoas.py: input a date and a country name, output the ipv4/6 valid/invalid/unknown routes/address

Ps: 

Routes is the ratio of advertised routes an ROA covers to the total route count.

Address is the ratio of the span of advertised addresses that an ROA covers to the total address span.



apnic rpki: measure invalid ROV throw-away situation, check if the network is ROV-aware

apnicRpki.py: input a date and a country name, output the date last 1/10/30/60/90 day test results in number and percentage of routes\partial_validate_routes\validate_routes checked

## Ripe ROA data

dataDownload.py: input a date, and download afrinic/lacnic/apnic/arin/ripencc roa output.json on that date.

asnRipe.py: input an ASN and output all the prefixes the ASN can publish that are valid online.

prefixRipe.py: input a prefix, output the ASN who could publish the prefix in a valid state.


## RP Database

ip2version.py: input a date and an IP, output all the RP versions used by the IP on that day

version2ip.py: input a date and an RP version, and output all the IPs who still used that version of RP on that day. We could use a fuzzy search, such as "Routinator" or "Routinator/0.12.1."