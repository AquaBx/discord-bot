const { REST, Routes } = require('discord.js');

const botinfos = require("./botinfos.json")
const commands = require("./commands.json")

const rest = new REST({ version: '10' }).setToken( botinfos.token );

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationCommands( botinfos.CLIENT_ID ), { body: commands });

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();