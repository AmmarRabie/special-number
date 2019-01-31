var config = {
    apiKey: "AIzaSyDsPtVdNNbBZGXwTW2x61z7Y4ZrUn9PWMY",
    authDomain: "special-numbers.firebaseapp.com",
    databaseURL: "https://special-numbers.firebaseio.com/",
};
// storageBucket: "bucket.appspot.com"
firebase.initializeApp(config);

let database = firebase.database();
let activeCompany = 'Etisalat' // one of Etisalat, Vodafone, We, Orange
let activeFilter = 'all' // one of vip, special, all


async function update(){
    let numbers = []
    if(activeFilter === "all"){
        const nsList = [await fetchPhoneNumbers(activeCompany, 'vip'), await fetchPhoneNumbers(activeCompany, 'special')]
        const flatten = n => numbers.push(n)
        nsList.forEach(ns => ns.forEach(flatten))
    } else {
        numbers = await fetchPhoneNumbers(activeCompany, activeFilter)
    }
    displayNumbers(numbers)
}

function setActiveFilter(who){
    activeFilter = who
    update()
}

function setActiveCompany(who){
    activeCompany = who
    update()
}

function writeNumber(number){
    const provider = number.substring(0,3)
    console.log(provider);
    const providerMatcher = {'011': 'T_Etisalat', '015': 'T_We', '010': 'T_Vodafone', '012': 'T_Orange'}
    // console.log(providerMatcher['011']);
    let type = ['vip', 'special'][Math.floor(Math.random() * 2)]; // rand int from 0 to 3
    key = providerMatcher[provider] + '-' + type
    firebase.database().ref(`/${key}/${number}`).set('Available');
}


async function fetchPhoneNumbers(company, type){
    let availableNumbers = []
    phonesSH = await database.ref(`/T_${company}-${type}`).once('value')
    phonesSH.forEach(phoneSH => {
        phone = phoneSH.key
        status = phoneSH.val()
        // console.log(phone);            
        // console.log(status);
        if(status !== 'Available') return
        availableNumbers.push(phone)
    });
    return availableNumbers
}


function numberElementString(number){
    return `<div class="card mx-auto mycard ${activeCompany}"><h5 class="mx-auto">${number}</h5></div>`
}


function displayNumbers(numbers){
    let columns = []
    for(let i = 1; i <= 3; i++){
        columns.push(document.getElementById(`col${i}`))
        columns[i - 1].innerHTML = ''
    }
    let currentCol = 0
    numbers.forEach(number => {
        columns[currentCol].innerHTML += numberElementString(number)
        currentCol = (currentCol + 1) % 3
    })
}




// testing purpose
function getFakeNumbers(min, max){
    const count = Math.floor(Math.random() * (max - min)) + min;
    let numbers = []
    const providers = ['011', '012','015','010'] // from 0 to 3
    for(let i = 0; i< count;i++){
        let phone = providers[Math.floor(Math.random() * 4)]; // rand int from 0 to 3
        for (let i = 0; i<8;i++){
            phone += String(Math.floor(Math.random() * 10)); // rand int from 0 to 9
        }
        numbers.push(phone)
    }
    return numbers
}

function writeRandomNumbers(min, max){
    numbers = getFakeNumbers(min, max)
    numbers.forEach(writeNumber)
}