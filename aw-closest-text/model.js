const fs = require("fs");

const Papa = require("papaparse");
const sw = require("stopword");

process.on('unhandledRejection', r => {throw r;});

const tokenize = (text) => sw.removeStopwords(
    text.toLowerCase().split(/[^a-zA-Z]/).filter(t => t),
    sw.fr);

const jaccard_distance = (tokens1, tokens2) => 
    tokens1.filter(v => -1 !== tokens2.indexOf(v)).length
    / (new Set([...tokens1, ...tokens2])).size;

const data = Papa.parse(fs.readFileSync('data/15ke_clean.csv', 'utf8')).data;
const tokenized = data.map(([id, text]) => ([id, tokenize(text)]));
const result = tokenized.map(([id, text]) => {
    tokenized.sort((a, b) => jaccard_distance(a[1], text) - jaccard_distance(b[1], text));
    
    return {
        id,
        closest: tokenized[0][0],
        distance: jaccard_distance(tokenized[0][1], text)
    }
});

fs.writeFileSync("result.json", JSON.stringify(result));