import requests
import os.path

filepath = 'C:/Users/lukka/Documents/Gabaritos/'
for i in range(14900, 100000):
	url = 'https://ulife-assessment.s3.amazonaws.com/AnswerKey/{}.pdf'.format(i)
	r = requests.get(url)
	if r.status_code != 403:
		if not os.path.isfile(filepath + str(i) + '.pdf'):
			open(f'C:/Users/lukka/Documents/Gabaritos/{i}.pdf', 'wb').write(r.content)
			open(f'C:/Users/lukka/Documents/Gabaritos/logNovoDownloadRealizado.txt', 'a').write(f'Novo Gabarito número: {i} encontrado, download realizado!\n')
			print(f'Gabarito novo encontrado! Número: {i}, download realizado!')
		else:
			open(f'C:/Users/lukka/Documents/Gabaritos/logExistente.txt', 'a').write(f'Gabarito número: {i} já existente!\n')
			print('Gabarito já existente! Indo para o próximo...')
	else:
		open(f'C:/Users/lukka/Documents/Gabaritos/logAcessoNegado.txt', 'a').write(f'Gabarito número: {i} com acesso NEGADO!\n')
		print(f'Gabarito número: {i} com acesso NEGADO!')