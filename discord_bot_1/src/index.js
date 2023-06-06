let botinfos = require("./botinfos.json")

const { Client, GatewayIntentBits, ActionRowBuilder, ButtonBuilder, ButtonStyle, EmbedBuilder } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});


let ratios = {
  boss : 1,
  ennemys : 5,
  chest:3,
  void:16
}

let ratios_list = []

for (let key in ratios ) {
  for (let i = 0; i< ratios[key] ; i++){
    ratios_list.push(key)
  } 
}

function dungeon_pattern() {
  return ratios_list.sort((a, b) => 0.5 - Math.random());
}


function percent_to_bar(percent){
  let str = ""

  let full = percent % 10
  let half = (percent-full) % 10/2


  for (let i=0; i< 10;i++){ 
    switch (Math.round(percent-i*10)/100) {
      case 1 : str += "<:progress2full:1022758798802300939>" 
      case 0.5 : str += "<:progress2half:1022758802040311849>"
      case 0 : str += "<:progress2empty:1022758795585273897>"
    }
  }

  return str
}


client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === 'ping') {
    let rows = []

    let pattern = dungeon_pattern()
    for ( let i=0; i<25;i++){
      if (i%5 === 0){
        rows.push( new ActionRowBuilder() )
      }
      let content = pattern[i]
      let btn = new ButtonBuilder()
          .setCustomId(`btn-${i}-${content}`)
					.setLabel('?')
					.setStyle(ButtonStyle.Secondary)

      rows.at(-1).addComponents( btn )
    }

		await interaction.reply({ content:percent_to_bar(96),components: rows });
  }

  else if (interaction.commandName === 'combat') {


		await interaction.reply({ content:percent_to_bar(96),components: rows });
  }
});

client.on('interactionCreate', async interaction => {
	if (!interaction.isButton()) return;

    let style 
    let label

    switch (interaction.component.data.custom_id.split("-").at(-1)) {
      case "boss" : {
        label="☠️"
        style="1"
        break
      }
      case "ennemys" : {
        label="💀"
        style="4"
        break
      }
      case "chest":{
        label="🪙"
        style="3"
        break
      }
      case "void":{
        label=" "
        style="2"
        break
      }
    }

    interaction.component["data"]["style"] = style;
    interaction.component["data"]["label"] = label;
    interaction.component["data"]["disabled"] = true;
    
    await interaction.message.edit({components: interaction.message.components});

    await interaction.deferUpdate();

});

client.login( botinfos.token );