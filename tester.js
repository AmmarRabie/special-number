// testing purpose
function getFakeNumbers(min, max) {
    const count = Math.floor(Math.random() * (max - min)) + min;
    let numbers = []
    const providers = ['011', '012', '015', '010'] // from 0 to 3
    for (let i = 0; i < count; i++) {
        let phone = providers[Math.floor(Math.random() * 4)]; // rand int from 0 to 3
        for (let i = 0; i < 8; i++) {
            phone += String(Math.floor(Math.random() * 10)); // rand int from 0 to 9
        }
        numbers.push(phone)
    }
    return numbers
}

function writeNumber(number) {
    const provider = number.substring(0, 3)
    console.log(provider);
    const providerMatcher = { '011': 'Etisalat', '015': 'We', '010': 'Vodafone', '012': 'Orange' }
    // console.log(providerMatcher['011']);
    let type = ['vip', 'special'][Math.floor(Math.random() * 2)]; // rand int from 0 to 3
    key = providerMatcher[provider] + '-' + type
    database.ref(`/${key}/${number}`).set('Available');
}

function writeRandomNumbers(min, max) {
    numbers = getFakeNumbers(min, max)
    numbers.forEach(writeNumber)
}