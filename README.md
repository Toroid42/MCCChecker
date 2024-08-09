# MCCMapper

Link: [MCC Mapper](https://toroid42.github.io/MCCMapper/)

The MCC Mapper can be used to check for a given Merchant Category Code (or the text representation of the code) if any
of the given cashback card providers (Renegade, Plutus, Hi, Crypto.com and Nexo) provide cashback or blacklist the MCC

## Update mccData.csv

To update the MCC data download the latest version for the MCC list and update the csv

```bash
mccXlsxToCsv.py -o anhang-2-zahlungssysteme-mcc-liste-data.xlsx -o csv-data/availableMccData.csv
```

## Sources for MCC data and MCC Blacklist data

| Provider   | Update date        | Source                                                                                                                         |
|------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Renegade   | 2024-08-09         | https://support.nexo.com/article/which-merchants-are-not-supported-by-the-nexo-card                                            |
| Plutus     | 2024-08-09         | https://www.plutus.it/help/transaction-types-not-eligible-for-plu-rewards                                                      |
| Hi.com     | ?                  | Telegram                                                                                                                       |
| Crypto.com | 2024-08-09         | https://help.crypto.com/en/articles/4597450-restriction-of-cro-rewards-program-and-restricted-markets-for-crypto-com-visa-card |
| Nexo       | 2024-08-09         | https://support.nexo.com/article/what-transactions-are-ineligible-for-the-nexo-card-cashback                                   |
