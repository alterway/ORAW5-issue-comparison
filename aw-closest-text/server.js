const fs = require("fs");

const Hapi=require('hapi');
const Papa = require("papaparse");
const sw = require("stopword");

process.on('unhandledRejection', r => {throw r;});

const tokenize = (text) => sw.removeStopwords(
    text.toLowerCase().split(/[^a-zA-Z]/).filter(t => t),
    sw.fr);

const jaccard_distance = (tokens1, tokens2) => 
    tokens1.filter(v => -1 !== tokens2.indexOf(v)).length
    / (new Set([...tokens1, ...tokens2])).size;

const tickets = Papa.parse(fs.readFileSync('tickets.csv', 'utf8')).data;
const server = Hapi.server({ host:'0.0.0.0', port:8000 });

server.route({
    method:'POST',
    path:'/getClosestTicket',
    handler: function (req) {
        const reqText = req.payload.content;
        const reqTokens = tokenize(reqText);
        const reqTicketId = req.payload.ticketId;
        const reqTreshold = req.payload.treshold;
        const reqCount = req.payload.count;
        const reqProject = req.payload.project;

        tickets.sort((a, b) => jaccard_distance(a[1], reqTokens) - jaccard_distance(b[1], reqTokens));

        const closest = {
            id: tickets[0][0],
            distance: jaccard_distance(tickets[0][1], reqTokens)
        };

        const project_closests = tickets
            .filter(([id, tokens, project]) => project == reqProject)
            .slice(0, reqCount)
            .filter(([id, tokens]) => jaccard_distance(tokens, reqTokens) < reqTreshold)
            .map(([id, tokens]) => ({ id, distance: jaccard_distance(tokens, reqTokens) }));

        //save the new ticket
        tickets.push({ id: reqTicketId, text: reqTokens, project: reqProject });
        const csv_data = Papa.unparse(tickets);
        fs.writeFileSync('tickets.csv', csv_data);

        return { closest, project_closests };
    }
});

server.route({
    method:'GET',
    path:'/health',
    handler: () => 'OK'
});

try {
    await server.start();
}
catch (err) {
    console.log(err);
    process.exit(1);
}

console.log('Server running at:', server.info.uri);
process.on("SIGINT", () => process.exit(0));