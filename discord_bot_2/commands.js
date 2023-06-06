const fs = require('fs');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { guildId, token } = require('./config.json');
 
// commands

var commands = [];
var commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (var file of commandFiles) {
  var command = require(`./commands/${file}`);
	commands.push(command.data);
}

//

var test_commands = [];
var commandFiles = fs.readdirSync('./guild').filter(file => file.endsWith('.js'));

for (var file of commandFiles) {
  var command = require(`./guild/${file}`);
	test_commands.push(command.data);
}

var rest = new REST({ version: '9' }).setToken(token);

async function load_commands(clientId){
    try {
      console.log(commands)
  
      await rest.put(
        Routes.applicationCommands(clientId),{ body: commands },
      );

      console.log(test_commands)

      await rest.put(
        Routes.applicationGuildCommands(clientId, guildId),{ body: test_commands },
      );
  
      console.log('Successfully reloaded application (/) commands.');
    } catch (error) {
      console.error(error);
    }
}

exports.load_commands = load_commands