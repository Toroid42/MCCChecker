# MCC Checker

Link: [MCC Checker](https://toroid42.github.io/MCCChecker/)

The MCC Checker can be used to check for a given Merchant Category Code (or the text representation of the code) if any
of the given cashback card providers (Renegade, Plutus, Hi, Crypto.com and Nexo) provide cashback or blacklist the MCC

## Update mccData.csv

To update the MCC data download the latest version for the MCC list and update the csv

```bash
mccXlsxToCsv.py -i anhang-2-zahlungssysteme-mcc-liste-data.xlsx -o csv-data/availableMccData.csv
```

## Sources for MCC data and MCC Blacklist data

| Type      | Provider   | Update date | Source                                                                                                                         |
|-----------|------------|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| MCC Data  | Bundesbank | 2024-08-11  | https://www.bundesbank.de/de/service/meldewesen/anhang-2-zahlungssysteme-und-mcc-liste-858960                                  |
| Blacklist | Renega de  | 2024-08-09  | https://support.nexo.com/article/which-merchants-are-not-supported-by-the-nexo-card                                            |
| Blacklist | Plutus     | 2024-08-09  | https://www.plutus.it/help/transaction-types-not-eligible-for-plu-rewards                                                      |
| Blacklist | Hi.com     | ?           | Telegram                                                                                                                       |
| Blacklist | Crypto.com | 2024-08-09  | https://help.crypto.com/en/articles/4597450-restriction-of-cro-rewards-program-and-restricted-markets-for-crypto-com-visa-card |
| Blacklist | Nexo       | 2024-08-09  | https://support.nexo.com/article/what-transactions-are-ineligible-for-the-nexo-card-cashback                                   |
