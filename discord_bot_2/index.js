const { Client, Intents, MessageEmbed, MessageAttachment,MessageButton,MessageActionRow } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]});
const { token } = require('./config.json');
const { load_commands } = require("./commands")

client.on('ready', async() => {
    console.log(`Logged in as ${client.user.tag}!`);
    await load_commands(client.user.id)
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isCommand()) return;
  
  if (interaction.commandName === 'salot') {
    var grille = [[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]]
    var image = affiche_grille(grille)
    const buf = new Buffer.from(image, 'base64');
    const file = new MessageAttachment(buf, 'img.svg');

    console.log(buf)
    console.log(file)

    const exampleEmbed = new MessageEmbed().setColor('#0099ff').setTitle('Puissance 4')
    
    const row = new MessageActionRow().addComponents(
      new MessageButton()
        .setCustomId('p4-0')
        .setLabel('0')
        .setStyle('PRIMARY'),
      ).addComponents(
        new MessageButton()
          .setCustomId('p4-1')
          .setLabel('1')
          .setStyle('PRIMARY'),
      ).addComponents(
        new MessageButton()
          .setCustomId('p4-2')
          .setLabel('2')
          .setStyle('PRIMARY'),
      ).addComponents(
        new MessageButton()
          .setCustomId('p4-3')
          .setLabel('3')
          .setStyle('PRIMARY'),
      ).addComponents(
        new MessageButton()
          .setCustomId('p4-4')
          .setLabel('4')
          .setStyle('PRIMARY'),
      )
    await interaction.reply({ content: "salut", components: [row]  });
  }
});

client.login(token);



function affiche_grille(grille){
  var str = '<svg width="240" height="228" viewBox="0 0 120 114" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="32.5" y="38.5" width="87" height="75" fill="#00AAFF" stroke="black"/>'
  var lignes = [41.5,53.5,65.5,77.5,89.5,101.5]
  var colonnes = [35.5,47.5,59.5,71.5,83.5,95.5,107.5]

  lignes.reverse()

  for (var lin = 0; lin<6; lin++){
    for (var col = 0; col<7; col++){
      var color = "white"
      var joueur = grille[lin][col]
      if (joueur == 1){
        color = "red"
      }
      else if (joueur == 2){
        color = "yellow"
      }
      str += '<rect x="' + colonnes[col] + '" y="' + lignes[lin] + '" width="9" height="9" rx="4.5" fill="' + color + '" stroke="black"/>'
    }
  }

  str += '</svg>'

  return (btoa(str))
}

//"data:image/svg+xml;base64," + 