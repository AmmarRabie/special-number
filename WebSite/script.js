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
const highlight = "gold"

contactInfo = {
    phone: '01000000140',
    message: 'للإستعلام برجاء التواصل على',
}
async function update(){
    resetAnchColors()
    changeAnchorColor()
    setSpeciality()
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
    database.ref(`/${key}/${number}`).set('Available');
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
        availableNumbers.push({val:phone, vip:type==='vip'})
    });
    return availableNumbers
}



function numberElementString(number){
    return `<div class="card mx-auto mycard ${activeCompany}"><h5 class="mx-auto">${number.val}</h5>${vipNumberClarify(number.vip)}</div>`
}

function vipNumberClarify(isVip){
    if(!isVip) return ""
    return `<div class="card-badge">VIP</div>`
    return `<img alt="Card image cap" src="https://rlv.zcache.com/gold_and_black_laurel_vip_party_pass_classic_round_sticker-r37930bc448b745788b39d18a0b46c57b_v9wth_8byvr_307.jpg?rvtype=content" class="card-badge"></img>`
}

function displayNumbers(numbers){
    let columns = []
    for(let i = 1; i <= 2; i++){
        columns.push(document.getElementById(`col${i}`))
        columns[i - 1].innerHTML = ''
    }
    let currentCol = 0
    numbers.forEach(number => {
        columns[currentCol].innerHTML += numberElementString(number)
        currentCol = (currentCol + 1) % 2
    })
}


function resetAnchColors(){
    document.getElementById("weAnchor").style.color = "white";
    document.getElementById("vodafoneAnchor").style.color = "white";
    document.getElementById("orangeAnchor").style.color = "white";
    document.getElementById("etisalatAnchor").style.color = "white";
}

function changeAnchorColor(){
    if (activeCompany == "Orange")
        document.getElementById("orangeAnchor").style.color = highlight;
    else if (activeCompany == "Etisalat")
        document.getElementById("etisalatAnchor").style.color = highlight;
    else if (activeCompany == "Vodafone")
        document.getElementById("vodafoneAnchor").style.color = highlight;
    else
        document.getElementById("weAnchor").style.color = highlight;
}


function setSpeciality(){
    let speciality = "نوع التميز - الكل"

    if(activeFilter == "vip")
        speciality = "VIP - نوع التميز"
    else if (activeFilter == "special")
        speciality = "نوع التميز - مميزة"

    document.getElementById("navbarDropdown").innerHTML = speciality
}

async function setContactInfo(){
    const phoneSH = await database.ref(`/contact-info/phone`).once('value')
    contactInfo.phone = phoneSH.val()
    const messageSH = await database.ref(`/messages/contact-us`).once('value')
    contactInfo.message = messageSH.val()
    document.getElementById("contact_info").innerHTML = contactInfo.message + contactInfo.phone
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