import telebot
import datetime

API_KEY = ""
bot = telebot.TeleBot(API_KEY)
pedido = {
    "nome_cliente": "",
    "pedido": "",
    "hora_pedido": "",
    "total": "",
    "pagamento": ""
}
cardapio = """ \n 
    /pizzas 🍕 \n
    /hamburger 🍔\n
    /sorvetes 🍦\n
    /massas 🍝\n
    /batata_frita 🍟\n
    /carnes  🍖\n
    /prato_do_dia 🍛\n

"""
help_message = """\n
    /pedido  🗒- lista os tipos de pedidos que temos \n
    /tempo  ⏰- mostra o tempo que falta para finalizar seu pedido\n
    /entrega 🛵 - mostra se o seu pedido saiu para entrega\n
    /nota  💯 - serve para avaliar nosso serviço de atendimento\n
"""
@bot.message_handler(commands=['help'])
def resposta1(message):
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['pedido'])
def resposta_pedidos(message):
    bot.reply_to(message, cardapio)

pizzas = {
    'calabresa': 30.00,
    'portuguesa': 34.50,
    'quatro_queijos': 38.50,
    'frango_catup': 28.50,
    'bacon': 30.50,
    'mussarela': 28.00,
    'charque_queijo': 38.90,
    'palmito': 34.80
}
sabores_pizzas ="""\

/calabresa - queijo mussarela, calabresa sadia, oregano, cebola, tomate e molho de tomate R$ 30,00 \n
/portuguesa - tomate, ovos cozidos, presunto defumado, queijo mussarela, oregano  R$ 34,50\n
/quatro_queijos - queijo brie, queijo provolone, queijo gorgonzola, queijo mussarela R$ 38,50\n
/frango_catup - frango desfiado, queijo catupiry  R$ 28,50\n
/bacon - bacon fatiado, queijo mussarela, molho especial  R$ 30,00\n
/mussarela - mussarela, tomate fatiado R$ 28,00\n
/charque_queijo - charque fatiada, queijo coalho, pimentão, cebola caramelizada, tomate R$ 38,90 \n
/palmito - palmito em conserva, queijo provolone, molho especial  R$ 34,80\n
"""
taxa_entrega = 4.50

@bot.message_handler(commands=['pizzas'])
def resposta_pizzas(message):
    bot.reply_to(message, 'Oba pizza, tudo fica muito melhor com pizza, olha os sabores que nos temos.')
    pedido["nome_cliente"] = f'{message.json["chat"]["first_name"]} {message.json["chat"]["last_name"] }'
    bot.reply_to(message,sabores_pizzas)

@bot.message_handler(commands=['calabresa','portuguesa', 'quatro_queijos', 'frango_catup', 'bacon', 'mussarela', 'charque_queijo', 'palmito'])
def resposta_pedido_pizza(message):
    pedido['pedido'] = message.text.replace('/', '')
    pedido['total'] = pizzas[pedido['pedido']] + taxa_entrega
    bot.reply_to(message, 'Oba, legal, para completar o seu pedido deseja adicionar algo a pizza? ou quem sabe algo para beber, Não acredito que você vai tomar água comendo pizza -_- \n /bebidas - listar nossas bebidas \n /adicional - bordas recheadas, mais Bacon S2, queijo extra, frango extra, etc... \n /finalizar - finalizar o pedido')



@bot.message_handler(commands=['finalizar'])
def finalizar(message):
    if pedido['pedido'] == '':
        bot.reply_to(message, 'Precisa ter um pedido, ou selecionar algo para poder finalizar.')
    else:
        pedido['hora_pedido'] = str(datetime.datetime.now()).split(' ')[1].split('.')[0]
        bot.reply_to(message, f"Finalizamos seu pedido {pedido['nome_cliente']}, você comprou {pedido['pedido']}, no valor de {pizzas[pedido['pedido']]}, com acrescimo de R4,50 da entrega, o total é de R${pedido['total']}, em até 40 minutos seu pedido será Entregue 👍. \n")

    return True

bot.infinity_polling()


