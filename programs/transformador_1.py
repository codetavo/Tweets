# -*- coding: utf-8 -*-
import json
from datetime import datetime, date, time, timedelta

def resta_hora(hora1,hora2):
    formato = "%H:%M:%S"
    lista = hora2.split(":")
    hora=int(lista[0])
    minuto=int(lista[1])
    segundo=int(lista[2])
    h1 = datetime.strptime(hora1, formato)
    dh = timedelta(hours=hora) 
    dm = timedelta(minutes=minuto)          
    ds = timedelta(seconds=segundo) 
    resultado1 =h1 - ds
    resultado2 = resultado1 - dm
    resultado = resultado2 - dh
    resultado=resultado.strftime(formato)
    return str(resultado)

def cargar_datos(ruta):
	with open(ruta) as contenido:
		abrir = json.load(contenido)
		#print(abrir['created_at'])
		# Tipo de dato a trabajar
		# print(type(abrir))
		# print(abrir['item'])
		# Recorrer todos los item
		# print(len(abrir['item']))
		cont = 0
		print('-----------------------------------------------------------------------------------------------------------------')
		for item in abrir['item']:
			cont = cont + 1
			print(cont)
			dato15 = item['user']['followers_count']
			dato16 = item['user']['favourites_count']

			print(json.dumps(dato15))
			print(json.dumps(dato16))
			if 'retweeted_status' in item:
				dato17 = item['retweeted_status']['retweet_count']
				dato18 = item['retweeted_status']['user']['name']

				print(json.dumps(dato17))
				print(json.dumps(dato18))
			else:
				print("NO")
			#temp = '"created_at":"'+item['created_at']+'",'
			#print(temp)
			#datos = item['created_at']
			#dia = datos[8]+datos[9]
			#mes = datos[4]+datos[5]+datos[6]
			#if str(mes) == "Jan":
				#mes_n = "01"
			#elif str(mes) == "Feb":
				#mes_n = "02"
			#elif str(mes) == "Mar":
				#mes_n = "03"
			#elif str(mes) == "Apr":
				#mes_n = "04"
			#elif str(mes) == "May":
				#mes_n = "05"
			#elif str(mes) == "Jun":
				#mes_n = "06"
			#elif str(mes) == "Jul":
				#mes_n = "07"
			#elif str(mes) == "Aug":
				#mes_n = "08"
			#elif str(mes) == "Sep":
				#mes_n = "09"
			#elif str(mes) == "Oct":
				#mes_n = "10"
			#elif str(mes) == "Nov":
				#mes_n = "11"
			#elif str(mes) == "Dec":
				#mes_n = "12"
			#else:
				#mes_n = "01"
			#year = datos[26]+datos[27]+datos[28]+datos[29]
			#hora = datos[11]+datos[12]+datos[13]+datos[14]+datos[15]+datos[16]+datos[17]+datos[18]
			#h = datos[11]+datos[12]
			#hora_final = resta_hora(hora,"03:00:00")

			#print(hora_final) 
			#print(dia)
			#print(mes_n)
			#print(year)

			#fecha = year+"-"+mes_n+"-"+dia+" "+hora_final
			#print(fecha)
			#if 'extended_tweet' in item:
				#print(item['extended_tweet']['entities']['hashtags'])
				#print(len(item['extended_tweet']['entities']['hashtags']))
				#if len(item['extended_tweet']['entities']['hashtags']) > 0:
					#print('"hashtags":["')
					#temp14 = '"hashtags":["'
					#conth = 0
					#for hs in item['extended_tweet']['entities']['hashtags']:
						#conth = conth + 1
						#if conth == len(item['extended_tweet']['entities']['hashtags']):
							#temp14 = temp14+hs['text']+'"]'
						#else:
							#temp14 = temp14+hs['text']+'","'
					#print(temp14)
			#else:
				#if 'retweeted_status' in item:
					#print(item['retweeted_status']['extended_tweet'])
					#if 'extended_tweet' in item['retweeted_status']:
						#print(item['retweeted_status']['extended_tweet']['full_text'])
						#print('si')
					#else:
						#print(item['retweeted_status']['text'])
				#else:
					#print(item['text'])
			# item anidados	
			#			print(item['user']['id'])
			#			print(type(item['extended_tweet']['extended_entities']))
			#Encontrar keys
			#print(item[0])
			#if 'display_text_range' and 'entities' in item['extended_tweet'].keys():
			#	print('Esta')
			#else:
			#	print('No esta')

def cargar_datos2(ruta):
	with open(ruta) as contenido:
		abrir = json.load(contenido)
		# Muesta json de manera ordenada		
		abrir2 = json.dumps(abrir, indent=2)
		#print(abrir2)
		print(len(abrir['item']))
		for item in abrir['item']:
			print(json.dumps(item['user']['name']))

def cargar_datos3(ruta):
	with open(ruta) as contenido:
		abrir = json.load(contenido)
		total = len(abrir['item'])
		cont = 0
		count = 0
		#print('{"item":[{')
		archivo.write('{' + '\n')
		archivo.write('"items" : [' + '\n')
		for item in abrir['item']:
			if 'created_at' and 'id' and 'id_str' and 'text' in item.keys():
				if 'id' and 'id_str' and 'name' and 'screen_name' and 'location' and 'url' and 'description' and 'lang' in item['user'].keys():
					#
					temp = '"created_at":"'+item['created_at'].replace(' +0000', '')+'",'
					#
					temp2 = '"id":'+str(item['id'])+','
					#
					temp3 = '"id_str":"'+item['id_str']+'",'
					#
					dato = item['text']
					#dato2 = dato.replace('"', "'")
					#dato4 = dato2.replace('\n', " ")
					temp4 = '"text":'+json.dumps(dato)+','
					#
					temp5 = '"user_id":'+str(item['user']['id'])+','
					#
					temp6 = '"user_id_str":"'+item['user']['id_str']+'",'
					#
					temp7 = '"label":'+json.dumps(item['user']['name'])+','
					#
					temp8 = '"user_screen_name":"'+item['user']['screen_name']+'",'
					#
					if item['user']['location'] is None:
						temp9 = '"user_location":null,'
						temp20 = '"coordenadas":null,'
					else:
						dato2 = str(item['user']['location'])
					#
						if "Chile" in dato2:
							#print("Chile")
							temp9 = '"user_location":'+json.dumps("Santiago - Chile")+','
							temp20 = '"coordenadas":'+json.dumps("-33.45,-70.666667")+','
						elif "Colombia" in dato2:
							#print("Colombia")
							temp9 = '"user_location":'+json.dumps("Bogota - Colombia")+','
							temp20 = '"coordenadas":'+json.dumps("4.598889,-74.080833")+','
						elif "Ecuador" in dato2:
							#print("Ecuador")
							temp9 = '"user_location":'+json.dumps("Quito - Ecuador")+','
							temp20 = '"coordenadas":'+json.dumps("-0.218611,-78.509722")+','
						elif "Venezuela" in dato2:
							#print("Venezuela")
							temp9 = '"user_location":'+json.dumps("Caracas - Venezuela")+','
							temp20 = '"coordenadas":'+json.dumps("10.5,-66.933333")+','
						elif (("Bolivia" in dato2) or ("La Paz" in dato2)):
							#print("Bolivia")
							temp9 = '"user_location":'+json.dumps("La Paz - Bolivia")+','
							temp20 = '"coordenadas":'+json.dumps("-16.494167,-68.1475")+','
						elif "México" in dato2:
							if ("México." in dato2) == False:
								#print("México")
								temp9 = '"user_location":'+json.dumps("Cuidad de México - México")+','
								temp20 = '"coordenadas":'+json.dumps("19.419444,-99.145556")+','
							else:
								#print("Costa Rica")
								temp9 = '"user_location":'+json.dumps("San José - Costa Rica")+','
								temp20 = '"coordenadas":'+json.dumps("9.933333,-84.083333")+','
						elif "Washington," in dato2:
							#print("Washington")
							temp9 = '"user_location":'+json.dumps("EE. UU. - Washington - Olympia")+','
							temp20 = '"coordenadas":'+json.dumps("47.0425,-122.893056")+','
						elif "Panamá" in dato2:
							#print("Panamá")
							temp9 = '"user_location":'+json.dumps("Panamá - Panamá")+','
							temp20 = '"coordenadas":'+json.dumps("9,-79.5")+','
						elif "Honduras" in dato2:
							#print("Honduras")
							temp9 = '"user_location":'+json.dumps("Tegucigalpa - Honduras")+','
							temp20 = '"coordenadas":'+json.dumps("14.094167,-87.206667")+','
						elif "Costa Rica" in dato2:
							#print("Costa Rica")
							temp9 = '"user_location":'+json.dumps("San José - Costa Rica")+','
							temp20 = '"coordenadas":'+json.dumps("9.933333,-84.083333")+','
						elif "Brasília" in dato2:
							#print("Brasil")
							temp9 = '"user_location":'+json.dumps("Brasília - Brasil")+','
							temp20 = '"coordenadas":'+json.dumps("-15.793889,-47.882778")+','
						elif "El Salvador" in dato2:
							#print("El Saldavor")
							temp9 = '"user_location":'+json.dumps("San Salvador - El Salvador")+','
							temp20 = '"coordenadas":'+json.dumps("13.69,-89.19")+','
						elif "Argentina" in dato2:
							#print("Argentina")
							temp9 = '"user_location":'+json.dumps("Buenos Aires - Argentina")+','
							temp20 = '"coordenadas":'+json.dumps("-34.599722,-58.381944")+','
						elif "Guatemala" in dato2:
							#print("Guatemala")
							temp9 = '"user_location":'+json.dumps("Ciudad de Guatemala - Guatemala")+','
							temp20 = '"coordenadas":'+json.dumps("14.622778,-90.531389")+','
						elif (("PERU" in dato2) or ("Peru" in dato2) or ("Perú" in dato2)):
							#print("Perú")
							temp9 = '"user_location":'+json.dumps("Lima - Perú")+','
							temp20 = '"coordenadas":'+json.dumps("-12.05,-77.033333")+','
						elif "Uruguay" in dato2:
							#print("Uruguay")
							temp9 = '"user_location":'+json.dumps("Montevideo - Uruguay")+','
							temp20 = '"coordenadas":'+json.dumps("-34.866944,-56.166667")+','
						elif "Dominicana" in dato2:
							#print("República Dominicana")
							temp9 = '"user_location":'+json.dumps("Santo Domingo - República Dominicana")+','
							temp20 = '"coordenadas":'+json.dumps("18.476389,-69.893333")+','
						elif "Cuba" in dato2:
							#print("Cuba")
							temp9 = '"user_location":'+json.dumps("La Habana - Cuba")+','
							temp20 = '"coordenadas":'+json.dumps("23.116667,-82.383333")+','
						elif "Houston" in dato2:
							#print("Houston")
							temp9 = '"user_location":'+json.dumps("EE. UU. - Texas - Houston")+','
							temp20 = '"coordenadas":'+json.dumps("29.762778,-95.383056")+','
						elif "Países Bajos" in dato2:
							#print("Países Bajos")
							temp9 = '"user_location":'+json.dumps("La Haya - Países Bajos")+','
							temp20 = '"coordenadas":'+json.dumps("52.084167,4.3175")+','
						elif "New York" in dato2:
							#print("New York")
							temp9 = '"user_location":'+json.dumps("EE. UU. - New York - New York")+','
							temp20 = '"coordenadas":'+json.dumps("40.67,-73.94")+','
						elif "Paraguay" in dato2:
							#print("Paraguay")
							temp9 = '"user_location":'+json.dumps("Asunción - Paraguay")+','
							temp20 = '"coordenadas":'+json.dumps("-25.3,-57.633333")+','
						elif "Alagoas" in dato2:
							#print("Alagoas")
							temp9 = '"user_location":'+json.dumps("Maceió - Alagoas - Brasil")+','
							temp20 = '"coordenadas":'+json.dumps("-9.665833,-35.735")+','
						else:
							temp9 = '"user_location":'+json.dumps(dato2)+','
							temp20 = '"coordenadas":null,'
					#
					if item['user']['url'] is None:
						temp10 = '"user_url":null,'
					else:
						temp10 = '"user_url":"'+item['user']['url']+'",'
					#
					if item['user']['description'] is None:
						temp11 = '"user_description":null,'
					else:
						temp11 = '"user_description":'+json.dumps(item['user']['description'])+','
					#
					#temp12 = '"user_lang":"'+item['user']['lang']+'",'
					if item['user']['lang'] == "es":
						temp12 = '"user_lang":'+json.dumps("Español")+','
					elif item['user']['lang'] == "en":
						temp12 = '"user_lang":'+json.dumps("Inglés")+','
					elif item['user']['lang'] == "pt":
						temp12 = '"user_lang":'+json.dumps("Portugués")+','
					else:
						temp12 = '"user_lang":"'+item['user']['lang']+'",'
					#
					temp13 = '"'
					if 'extended_tweet' in item:
						dato3 = item['extended_tweet']['full_text']
						#dato4 = dato3.replace('"', "'")
						#dato5 = dato4.replace('\n', " ")
						temp13 = '"full_text":'+json.dumps(dato3)+','
					else:
						if 'retweeted_status' in item:
							if 'extended_tweet' in item['retweeted_status']:
								dato3 = item['retweeted_status']['extended_tweet']['full_text']
								#dato4 = dato3.replace('"', "'")
								#dato5 = dato4.replace('\n', " ")
								temp13 = '"full_text":'+json.dumps(dato3)+','
							else:
								dato3 = item['retweeted_status']['text']
								#dato4 = dato3.replace('"', "'")
								#dato5 = dato4.replace('\n', " ")
								temp13 = '"full_text":'+json.dumps(dato3)+','
						else:
							dato3 = item['text']
							#dato4 = dato3.replace('"', "'")
							#dato5 = dato4.replace('\n', " ")
							temp13 = '"full_text":'+json.dumps(dato3)+','
					#
					temp14 = '"hashtags":['
					if 'extended_tweet' in item:
						if len(item['extended_tweet']['entities']['hashtags']) > 0:
							temp14 = temp14
							conth = 0
							for hs in item['extended_tweet']['entities']['hashtags']:
								conth = conth + 1
								if conth == len(item['extended_tweet']['entities']['hashtags']):
									temp14 = temp14+json.dumps(hs['text'])+']'
								else:
									temp14 = temp14+json.dumps(hs['text'])+','
						else:
							temp14 = temp14+']'
					else:
						temp14 = temp14+']'
					#
					datos = item['created_at']
					dia = datos[8]+datos[9]
					mes = datos[4]+datos[5]+datos[6]
					if str(mes) == "Jan":
						mes_n = "01"
					elif str(mes) == "Feb":
						mes_n = "02"
					elif str(mes) == "Mar":
						mes_n = "03"
					elif str(mes) == "Apr":
						mes_n = "04"
					elif str(mes) == "May":
						mes_n = "05"
					elif str(mes) == "Jun":
						mes_n = "06"
					elif str(mes) == "Jul":
						mes_n = "07"
					elif str(mes) == "Aug":
						mes_n = "08"
					elif str(mes) == "Sep":
						mes_n = "09"
					elif str(mes) == "Oct":
						mes_n = "10"
					elif str(mes) == "Nov":
						mes_n = "11"
					elif str(mes) == "Dec":
						mes_n = "12"
					else:
						mes_n = "01"
					year = datos[26]+datos[27]+datos[28]+datos[29]
					hora = datos[11]+datos[12]+datos[13]+datos[14]+datos[15]+datos[16]+datos[17]+datos[18]
					h = datos[11]+datos[12]
					hora_final = resta_hora(hora,"04:00:00")
					fecha = year+"-"+mes_n+"-"+dia+" "+hora_final
					temp15 = '"fecha":"'+fecha+'",'
					#
					temp16 = '"followers_count":'+json.dumps(item['user']['followers_count'])+','
					#
					temp17 = '"favourites_count":'+json.dumps(item['user']['favourites_count'])+','
					#
					if 'retweeted_status' in item:
						temp18 = '"retweet_count":'+json.dumps(item['retweeted_status']['retweet_count'])+','
						temp19 = '"retweet_name":'+json.dumps(item['retweeted_status']['user']['name'])+','
					else:
						temp18 = '"retweet_count":null,'
						temp19 = '"retweet_name":null,'
					#
					print('----------Tweet N°'+str(cont+1)+'----------')
					#print(temp)
					#print(temp2)
					#print(temp3)
					#print(temp4)
					#print(temp5)
					#print(temp6)
					#print(temp7)
					#print(temp8)
					#print(temp9)
					#print(temp10)
					#print(temp11)
					#print(temp12)
					#print(temp13)
					#print(temp14)
					cont = cont+1
					#Paso para abrir otro object o cerrar json
					if cont == total:
						#print('}]')
						temp_total = temp + temp15 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp16 + temp17 + temp18 + temp19 + temp20 + temp14 + '}]'
						archivo.write('{' + '\n')
						archivo.write(temp + '\n')
						archivo.write(temp15 + '\n')
						archivo.write(temp2 + '\n')
						archivo.write(temp3 + '\n')
						archivo.write(temp4 + '\n')
						archivo.write(temp5 + '\n')
						archivo.write(temp6 + '\n')
						archivo.write(temp7 + '\n')
						archivo.write(temp8 + '\n')
						archivo.write(temp9 + '\n')
						archivo.write(temp10 + '\n')
						archivo.write(temp11 + '\n')
						archivo.write(temp12 + '\n')
						archivo.write(temp13 + '\n')
						archivo.write(temp16 + '\n')
						archivo.write(temp17 + '\n')
						archivo.write(temp18 + '\n')
						archivo.write(temp19 + '\n')
						archivo.write(temp20 + '\n')
						archivo.write(temp14 + '\n')
						archivo.write('}' + '\n')
						archivo.write(']' + '\n')
						archivo.write('}')
						#temp_json=json.dumps(temp_total)
						#print(temp_total)
					else:
						#print('},')
						#temp_total = temp + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + '},'
						archivo.write('{' + '\n')
						archivo.write(temp + '\n')
						archivo.write(temp15 + '\n')
						archivo.write(temp2 + '\n')
						archivo.write(temp3 + '\n')
						archivo.write(temp4 + '\n')
						archivo.write(temp5 + '\n')
						archivo.write(temp6 + '\n')
						archivo.write(temp7 + '\n')
						archivo.write(temp8 + '\n')
						archivo.write(temp9 + '\n')
						archivo.write(temp10 + '\n')
						archivo.write(temp11 + '\n')
						archivo.write(temp12 + '\n')
						archivo.write(temp13 + '\n')
						archivo.write(temp16 + '\n')
						archivo.write(temp17 + '\n')
						archivo.write(temp18 + '\n')
						archivo.write(temp19 + '\n')
						archivo.write(temp20 + '\n')
						archivo.write(temp14 + '\n')
						archivo.write('},' + '\n')
						#temp_json=json.dumps(temp_total)
						#print(temp_total)
				else:
					print('No existe usuario')
			else:
				print('No existe tweet')
		#print(count)

def primeralinea(archivo, texto_inicio, texto_final):
    with open(archivo, 'r+') as f:
        contenido = f.read()
        f.seek(0, 0)
        f.write(texto_inicio.rstrip('\r\n') + '\n' + contenido + '\n' + texto_final.rstrip('\r\n'))

if __name__ == '__main__':
	#
	#archivo = 'duro2.js'
	#texto_inicio = '{"item":'
	#texto_final = ']}'
	#primeralinea(archivo, texto_inicio, texto_final)
	#
	ruta = 'duro5.js'
	ruta2 = 'data_tweets3.js'
	archivo = open(ruta2,'a')
	cargar_datos3(ruta)
	archivo.close()
	#
	#f = open("prueba.txt","r+")
	#lineas = f.readlines()
	#f.seek(0)
	#cont = 1
	#print(len(lineas))
	#for linea in lineas:
		#if len(lineas) == cont:
			#print(cont)
		#cont = cont + 1
	#f.truncate()
	#f.close()