var config = {
    apiKey: "AIzaSyCiKxvAk3jiMZ4jp5tTlHp8oH-TjFyk86s",
    authDomain: "special-number.firebaseapp.com",
    databaseURL: "https://special-number.firebaseio.com/",
};
firebase.initializeApp(config);

let database = firebase.database();
let activeCompany = 'Etisalat' // one of Etisalat, Vodafone, We, Orange
let activeFilter = 'all' // one of vip, special, all
const highlight = "gold"

contactInfo = {
    phone: '01000000140',
    message: 'للإستعلام برجاء التواصل على',
}
async function update() {
    resetAnchColors()
    changeAnchorColor()
    setSpeciality()
    let numbers = []
    if (activeFilter === "all") {
        const nsList = [await fetchPhoneNumbers(activeCompany, 'vip'), await fetchPhoneNumbers(activeCompany, 'special')]
        const flatten = n => numbers.push(n)
        nsList.forEach(ns => ns.forEach(flatten))
    } else {
        numbers = await fetchPhoneNumbers(activeCompany, activeFilter)
    }
    displayNumbers(numbers)
    animateToNumbers()
    // document.getElementById("company-selectors-container").scrollTo();
}

function animateToNumbers() {
    intervalId = setInterval(() => window.scrollBy(0, 10), 10)
    setTimeout(() => clearInterval(intervalId), 1000)
}

function setActiveFilter(who) {
    activeFilter = who
    update()
}

function setActiveCompany(who) {
    activeCompany = who
    update()
}

async function fetchPhoneNumbers(company, type) {
    let availableNumbers = []
    phonesSH = await database.ref(`/${company}-${type}`).once('value')
    phonesSH.forEach(phoneSH => {
        phone = phoneSH.key
        status = phoneSH.val()
        if (status.toUpperCase() !== 'available'.toUpperCase()) return
        availableNumbers.push({ val: phone, vip: type === 'vip' })
    });
    return availableNumbers
}

function numberElementString(number) {
    return `<div class="card mx-auto mycard ${activeCompany}"><h5 class="mx-auto">${number.val}</h5>${vipNumberClarify(number.vip)}</div>`
}

function vipNumberClarify(isVip) {
    if (!isVip) return ""
    return `<div class="card-badge">VIP</div>`
}

function displayNumbers(numbers) {
    let columns = []
    for (let i = 1; i <= 2; i++) {
        columns.push(document.getElementById(`col${i}`))
        columns[i - 1].innerHTML = ''
    }
    let currentCol = 0
    numbers.forEach(number => {
        columns[currentCol].innerHTML += numberElementString(number)
        currentCol = (currentCol + 1) % 2
    })
}

function resetAnchColors() {
    const ids = ["weAnchor", "vodafoneAnchor", "orangeAnchor", "etisalatAnchor"]
    ids.forEach(id => document.getElementById(id).style.color = "white")
}

function changeAnchorColor() {
    const idMapper = { Orange: "orangeAnchor", Etisalat: "etisalatAnchor", Vodafone: "vodafoneAnchor", We: "weAnchor" }
    document.getElementById(idMapper[activeCompany]).style.color = highlight
}

function setSpeciality() {
    let speciality = "الــكل"
    if (activeFilter == "vip")
        speciality = "VIP"
    else if (activeFilter == "special")
        speciality = "ممــيزة"
    document.getElementById("speciality").innerHTML = speciality
}

async function setContactInfo() {
    const phoneSH = await database.ref(`/contact-info/phone`).once('value')
    contactInfo.phone = phoneSH.val()
    const messageSH = await database.ref(`/messages/contact-us`).once('value')
    contactInfo.message = messageSH.val()
    if (contactInfo.message && contactInfo.phone)
        document.getElementById("contact_info").innerHTML = contactInfo.message + contactInfo.phone
}