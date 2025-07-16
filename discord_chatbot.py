import discord

token='entry_you_token'

intends = discord.Intents.default()
intends.message_content = True
client = discord.Client(intents=intends)    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if "TK" in message.content:
        await message.channel.send('TK je glup!')
        await message.author.kick(reason="TK je glup!")

    if message.content.startswith('$poll'):
        question = message.content[len('$poll'):].strip()
        if question:
            poll_message = await message.channel.send(f'Poll: {question}')
            await poll_message.add_reaction('👍')
            await poll_message.add_reaction('👎')
        else:
            await message.channel.send('Please provide a question for the poll.')   

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$bye'):
        await message.channel.send('Bye!')

    if message.content.startswith('$help'):
        await message.channel.send('Commands: $hello, $bye, $help') 

client.run(token)
