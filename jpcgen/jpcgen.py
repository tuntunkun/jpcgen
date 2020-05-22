#!/usr/bin/env python
import requests
import locale
import click
import xlrd
import sys
import io

# only for mobile numbers
urls = {
	'070': 'https://www.soumu.go.jp/main_content/000200622.xls',
	'080': 'https://www.soumu.go.jp/main_content/000124110.xls',
	'090': 'https://www.soumu.go.jp/main_content/000124111.xls',
}

# these translated names are based on the official website for each company
en_company_names = {
	'ＮＴＴドコモ': 'NTT DOCOMO',
	'ソフトバンク': 'SoftBank ',
	'ＫＤＤＩ': 'KDDI',
	'沖縄セルラー電話': 'Okinawa Cellular',
	'楽天モバイル': 'Rakuten Mobile',
}

def generate(OXO, output=sys.stdout, translate=False, encoding='utf-8'):
	wbook = xlrd.open_workbook(file_contents=requests.get(urls[OXO]).content)
	wsheet = wbook.sheet_by_name(OXO)

	# carrier definition starts on line 8
	for j in range(7, wsheet.nrows):
		for i in range(0, 9):
			prefix = wsheet.cell(j, 0).value

			# skip unused prefix numbers
			if wsheet.cell(j,i+1).value:
				carrier = wsheet.cell(j, i+1).value

				if translate:
					print('%s%d|%s' % (prefix, i, en_company_names[carrier]), file=output)
				else:
					print('%s%d|%s' % (prefix, i, carrier), file=output)



@click.command()
@click.argument('OUTPUT', type=click.File('w'), default=sys.stdout)
@click.option('--translate', '-t', is_flag=True, help='Translate carrier names into English.')
@click.option('--encoding', '-e', default=None, metavar='ENCODING', help='Output encoding.')
def main(output, translate, encoding):
	if encoding is None:
		if output is sys.stdout:
			encoding = locale.getpreferredencoding()
		else:
			encoding = 'utf-8'

	output = io.TextIOWrapper(output.buffer, encoding=encoding)
	for prefix in urls:
		generate(prefix, output, translate, encoding)
