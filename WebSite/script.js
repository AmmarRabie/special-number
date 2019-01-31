var config = {
    apiKey: "AIzaSyDsPtVdNNbBZGXwTW2x61z7Y4ZrUn9PWMY",
    authDomain: "special-numbers.firebaseapp.com",
    databaseURL: "https://special-numbers.firebaseio.com/",
};
// storageBucket: "bucket.appspot.com"
firebase.initializeApp(config);

let database = firebase.database();
let activeCompany = 'E' // one of Etisalat, Vodafone, We, Orange
let activeFilter = 'vip' // one of vip, special, all

function writeUserData(userId, name, email, imageUrl) {
    firebase.database().ref('users/' + userId).set({
      username: name,
      email: email,
      profile_picture : imageUrl
    });
  }

function writeNumber(number) {
    const provider = number.substring(0,3)
    console.log(provider);
    const providerMatcher = {'011': 'T_Etisalat', '015': 'T_We', '010': 'T_Vodafone', '012': 'T_Orange'}
    // console.log(providerMatcher['011']);
    let type = ['vip', 'special'][Math.floor(Math.random() * 2)]; // rand int from 0 to 3
    key = providerMatcher[provider] + '-' + type
    firebase.database().ref(`/${key}/${number}`).set('Available');
}


async function getPhoneNumbers(company, type){
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

function vipOnly(){
    writeUserData(123, 'ammar', 'ammaralsayed55@gmail.com', 'https://avatars1.githubusercontent.com/u/23727296?s=460&v=4')
    writeUserData('5wab', 'omar samir', 'omarsamir@gmail.com', 'https://avatars1.githubusercontent.com/u/23727296?s=460&v=4')
}

async function setActiveFilter(who){
    // writeRandomNumbers(5, 10)
    // const numbers = await getPhoneNumbers('Etisalat', 'vip')
    // displayNumbers(numbers)
    activeFilter = who
    const numbers = []
    if(activeFilter === "all"){
        const p1 = getPhoneNumbers(activeCompany, 'vip')
        const p2 = getPhoneNumbers(activeCompany, 'special')
        const listNumbers = await Promise.all(p1, p2)
        numbers.push(listNumbers[0],listNumbers[1])
    }
    else{
        numbers = await getPhoneNumbers(activeCompany, activeFilter)
    }
    displayNumbers(numbers)
}

async function setActiveCompany(who){
    activeCompany = who
    const numbers = await getPhoneNumbers(activeCompany, activeFilter)
    displayNumbers(numbers)


    document.getElementById("navbar").classList.remove('o','w','e','v', 'bg-light')
    document.getElementById("navbar").classList.add(who)
}

function vipAndSpecial(){
    const numbers = getFakeNumbers(40,80)
    return displayNumbers(numbers)
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

function numberElementString(number){
    s = `<div class="card mx-auto mycard"><h5 class="mx-auto">${number}</h5></div>`
    return s
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

var appConfig = {
    companyColors: {
        'o': '#006699',
        'e': '#446699',
        'w': '#123456',
        'v': '#789456',
    },
}