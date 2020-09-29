const { Command } = require("discord.js-commando");

module.exports = class EightBallCommand extends Command {
    constructor(client) {
        super(client, {
            name: "8ball",
            group: "general",
            memberName: "8ball",
            description: "Tells the future."
        });

        this.responses = [
            "It is certain",
            "Without a doubt",
            "Definitely",
            "Most likely",
            "Outlook good",
            "Yes!",
            "Try again",
            "Reply hazy",
            "Can't predict",
            "No!",
            "Unlikely",
            "Sources say no",
            "Very doubtful"
        ];
    }

    /**
     * Executes when the command is executed by the user
     * @param {string} message allows the bot to send and access messages
     * @param {string} args the arguments provided by the 
     */
    run(message, args) {
        if (args.trim() == "") message.say("Please ask a question");
        else message.say(this.responses[Math.floor(Math.random() * 13)]);
    }
};