# Japanese Carrier Metadata Generator
Japanese communication carrier metadata generator for `google/libphonenumber`

## Getting Started
### Prerequisites
* python3
* pip
* git

### Install

```sh
pip install git+https://github.com/tuntunkun/jpcgen
```

### How to use

Just type the command as follows to generate carrier mapping data in Japanese.
```sh
jpcgen 81-ja.txt
```

Or You can generate English translated version with `--translate` or `-t` option.
```sh
jpcgen --translate 81-en.txt
```

If output file is omitted, standard output is used.

### License
This project is licensed under the MIT License - see the LICENSE file for details

### Notice
This mapping generator is based on the data published by Ministry of Internal Affairs and Communications in Japan.
The company names in this code are generally registered trademarks or trademarks of each company.

Though the company names are represented in Full-width (Zenkaku) alphabet, Left as is, based on the original data is.
English version of company names are translated, based on the official website for each company.

### Reference
* https://www.soumu.go.jp/main_sosiki/joho_tsusin/top/tel_number/number_shitei.html
