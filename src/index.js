var { token, prefix, supportServerInvite } = require("../config.json");

const { CommandoClient } = require("discord.js-commando");
const path = require("path");

var bot = new CommandoClient({
    commandPrefix: prefix,
    invite: supportServerInvite
});

bot.registry
    .registerGroups([
        ["general", "General"]
    ])
    .registerDefaults()
    .registerCommandsIn(path.join(__dirname, "commands"));
    
bot.on("ready", async () => {
    console.log(`${bot.user.username} is online!`);
    bot.user.setPresence({
        status: "online",
        activity: {
            name: "OG Squad",
            type: "WATCHING"
        }
    });
});

bot.login(token).catch(console.log);